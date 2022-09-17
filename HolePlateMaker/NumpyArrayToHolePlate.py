import string
import sys,os
import numpy as np
from stl import mesh
from HolePlateMaker import set32 as s32
from HolePlateMaker import set48 as s48
from HolePlateMaker import addBlock as ab

import pyqtgraph.opengl as gl

def mesh_location_zero(my_mesh):
    my_mesh.x = my_mesh.x * 0.1
    my_mesh.y = my_mesh.y * 0.1
    my_mesh.z = my_mesh.z * 0.1

    midPosRel = (my_mesh.max_ - my_mesh.min_)/2
    tr_x = (midPosRel[0] + my_mesh.min_[0])
    tr_y = (midPosRel[1] + my_mesh.min_[1])
    tr_z = (midPosRel[2] + my_mesh.min_[2])

    my_mesh.x = my_mesh.x * 10
    my_mesh.y = my_mesh.y * 10
    my_mesh.z = my_mesh.z * 10

    return tr_x,tr_y,tr_z


class OP:
    row:int
    column:int
    rowMax:int
    columnMax:int
    value:int
    hashValue:int
    glMesh:gl.GLMeshItem
    blockSetting:dict
    type:string
    way:int

    def __init__(self,plateData,color,row,column,blockSetting:dict,type,way=0):
        size = plateData.shape
        self.rowMax = size[0]-1
        self.columnMax = size[1]-1
        self.row = row
        self.column = column
        self.value = plateData[column][row]
        self.hashValue = self.hashCalc()
        self.color = color
        self.blockSetting = blockSetting
        self.type = type
        self.way=way

        self.createMesh()


    def createMesh(self):

        OFFSET = [[-round(5*self.columnMax/2),-round(5*self.rowMax/2)],\
        [-round(7.97*self.columnMax/2),-round(7.97*self.rowMax/2)]]

        if(self.value>0):
            if(self.type=='3mm'):
                if(self.value>0 and self.value<len(self.blockSetting["datas3mm"])+1):
                    newMesh = s32.set32(self.row,self.column,0,self.blockSetting["datas3mm"][self.value-1],self.way)
                else:
                    sys.exit('Type \'3mm\' only support 0,1,2,3.')
                newMesh.translate(np.array([OFFSET[0][0],OFFSET[0][1],0]))

            elif(self.type=='4.8mm'):
                if(self.value>0 and self.value<len(self.blockSetting["datas48mm"])+1):
                    newMesh = s48.set48(self.row,self.column,0,self.blockSetting["datas48mm"][self.value-1],self.way)                
                else:
                    sys.exit('Type \'4.8mm\' only support 0,1,2,3.')
                newMesh.translate(np.array([OFFSET[1][0],OFFSET[1][1],0]))
        
            shape = newMesh.points.shape
            points = newMesh.points.reshape(-1, 3)
            faces = np.arange(points.shape[0]).reshape(-1, 3)
            meshdata = gl.MeshData(vertexes=points, faces=faces)
            self.glMesh = gl.GLMeshItem(meshdata=meshdata, smooth=True,\
                        drawFaces=True, drawEdges=False, edgeColor=(0, 0, 0, 1), shader='edgeHilight')
            self.glMesh.setColor(self.color)
            #print(f"color={self.color[self.value}")
            self.glMesh.scale(0.1,0.1,0.1)

    def hashCalc(self):
        return  self.row + self.columnMax*self.column
    
    def hashCalcValue(self,row,column):
        return  row +  self.columnMax*column
    
    def hashCheck(self,row,column):
        return  self.hashValue == self.hashCalcValue(row,column)
    
    def changeType(self,type):
        self.type = type
        self.createMesh()

class GLViewOperation:
    setting:dict
    color:list[tuple[float,float,float,float]]

    def __init__(self,setting,color):
        self.setting = setting
        self.color = color

    def GLViewDataPush(self, plateData,OPlist,row,column,type,way):
        if(not (type=='3mm' or type=='4.8mm')):
            sys.exit('Type support only \'3mm\' or \'4.8mm\'.')
        if(not (way==0 or way==1 or way==2 or way==3 or way==4)):
            sys.exit("Way support only 0,1,2,3,4")
        
        addData = OP(plateData,self.color[plateData[column][row]],row,column,self.setting["block"],type,way)
        OPlist.append(addData)
        return addData,OPlist
        
    def GLViewDataPop(self, OPlist,row,column): 
        changeData = list(filter(lambda op: op.hashCheck(row,column),OPlist))[0]
        pos = OPlist.index(changeData)
        deleteData = OPlist.pop(pos)
        return deleteData,OPlist

    def GLViewDataChange(self, plateData, OPlist, row, column, type="", way=-1):        
        beforeData = list(filter(lambda op: op.hashCheck(row,column),OPlist))[0]
        pos = OPlist.index(beforeData)
        
        # typeに関する引数がない（変化が無い）場合
        if(not type):
            type = OPlist[pos].type

        if(not (type=='3mm' or type=='4.8mm')):
            sys.exit('Type support only \'3mm\' or \'4.8mm\'.')

        # wayに関する引数がない（変化が無い）場合
        if(way<0):
            way = OPlist[pos].way

        afterData = OP(plateData,self.color[plateData[column][row]],row,column,self.setting["block"],type,way)
        OPlist[pos] = afterData
        return afterData,beforeData,OPlist

# STLファイル専用
def NumpyArrayToPlate(plateData,type,blockSetting:dict):
    if(not (type=='3mm' or type=='4.8mm')):
        sys.exit('Type support only \'3mm\' or \'4.8mm\'.')

    size = plateData.shape
    curMesh = mesh.Mesh(np.array([], dtype=mesh.Mesh.dtype))

    for i in np.arange(0,size[0]):
        for j in np.arange(0,size[1]):
            if(plateData[i][j]>0):
                if(type=='3mm'):
                    if(plateData[i][j]>0 and plateData[i][j]<len(blockSetting["datas3mm"])+1):
                        newMesh = s32.set32(i,j,0,blockSetting["datas3mm"][plateData[i][j]-1])
                    else:
                        sys.exit('Type \'3mm\' only support 0,1,2,3.')
                    
                elif(type=='4.8mm'):
                    if(plateData[i][j]>0 and plateData[i][j]<len(blockSetting["datas48mm"])+1):
                        newMesh = s48.set48(i,j,0,blockSetting["datas48mm"][plateData[i][j]-1])
                    else:
                        sys.exit('Type \'4.8mm\' only support 0,1,2,3.')

                
                curMesh = ab.addBlock(curMesh, newMesh)
    
    return curMesh