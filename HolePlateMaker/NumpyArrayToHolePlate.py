import sys,os
import numpy as np
from stl import mesh
from HolePlateMaker import setBU32 as sbu32
from HolePlateMaker import setBU48 as sbu48
from HolePlateMaker import setABU48 as sabu48
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

    def __init__(self,plateData,color,type,row,column):
        size = plateData.shape
        self.rowMax = size[0]-1
        self.columnMax = size[1]-1
        self.row = row
        self.column = column
        self.value = plateData[column][row]
        self.hashValue = self.hashCalc()
        self.color = color

        self.createMesh(type)


    def createMesh(self,type):

        OFFSET = [[-round(5*self.columnMax/2),-round(5*self.rowMax/2)],\
        [-round(7.97*self.columnMax/2),-round(7.97*self.rowMax/2)]]

        if(self.value>0):
            if(type=='3mm'):
                newMesh = sbu32.setBU32(self.row,self.column,0)
                newMesh.translate(np.array([OFFSET[0][0],OFFSET[0][1],0]))
            elif(type=='4.8mm'):
                if(self.value==1):
                    newMesh = sbu48.setBU48(self.row,self.column,0)                
                elif(self.value==2):
                    newMesh = sabu48.setABU48(self.row,self.column,0)
                else:
                    sys.exit('Type \'4.8mm\' only support 0,1,2.')
                newMesh.translate(np.array([OFFSET[1][0],OFFSET[1][1],0]))
        
            shape = newMesh.points.shape
            points = newMesh.points.reshape(-1, 3)
            faces = np.arange(points.shape[0]).reshape(-1, 3)
            meshdata = gl.MeshData(vertexes=points, faces=faces)
            self.glMesh = gl.GLMeshItem(meshdata=meshdata, smooth=True,\
                        drawFaces=True, drawEdges=False, edgeColor=(0, 0, 0, 1), shader='edgeHilight')
            self.glMesh.setColor(self.color[self.value])
            #print(f"color={self.color[self.value}")
            self.glMesh.scale(0.1,0.1,0.1)

    def hashCalc(self):
        return  self.row + self.columnMax*self.column
    
    def hashCalcValue(self,row,column):
        return  row +  self.columnMax*column
    
    def hashCheck(self,row,column):
        return  self.hashValue == self.hashCalcValue(row,column)
    
    def changeType(self,type):
        self.createMesh(type)

  
def GLViewDataPush(plateData,type,color,OPlist,row,column):
    if(not (type=='3mm' or type=='4.8mm')):
        sys.exit('Type support only \'3mm\' or \'4.8mm\'.')
    
    addData = OP(plateData,color,type,row,column)
    OPlist.append(addData)
    return addData,OPlist
    
def GLViewDataPop(plateData,type,color,OPlist,row,column):
    if(not (type=='3mm' or type=='4.8mm')):
        sys.exit('Type support only \'3mm\' or \'4.8mm\'.')
    
    changeData = list(filter(lambda op: op.hashCheck(row,column),OPlist))[0]
    pos = OPlist.index(changeData)
    deleteData = OPlist.pop(pos)
    return deleteData,OPlist

def GLViewDataChange(plateData,type,color,OPlist,row,column):
    if(not (type=='3mm' or type=='4.8mm')):
        sys.exit('Type support only \'3mm\' or \'4.8mm\'.')
    
    beforeData = list(filter(lambda op: op.hashCheck(row,column),OPlist))[0]
    pos = OPlist.index(beforeData)
    afterData = OP(plateData,color,type,row,column)
    OPlist[pos] = afterData
    return afterData,beforeData,OPlist

def NumpyArrayToPlate(plateData,type):
    if(not (type=='3mm' or type=='4.8mm')):
        sys.exit('Type support only \'3mm\' or \'4.8mm\'.')

    size = plateData.shape
    curMesh = mesh.Mesh(np.array([], dtype=mesh.Mesh.dtype))
    for i in np.arange(0,size[0]):
        for j in np.arange(0,size[1]):
            if(plateData[i][j]>0):
                if(type=='3mm'):
                    newMesh = sbu32.setBU32(i,j,0)
                elif(type=='4.8mm'):
                    if(plateData[i][j]==1):
                        newMesh = sbu48.setBU48(i,j,0)
                    elif(plateData[i][j]==2):
                        newMesh = sabu48.setABU48(i,j,0)
                    else:
                        sys.exit('Type \'4.8mm\' only support 0,1,2.')

                
                curMesh = ab.addBlock(curMesh, newMesh)
    
    return curMesh