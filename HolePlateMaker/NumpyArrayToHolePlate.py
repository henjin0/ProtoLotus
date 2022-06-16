import sys
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


def NumpyArrayToPlate(plateData,type,color):
    if(not (type=='3mm' or type=='4.8mm')):
        sys.exit('Type support only \'3mm\' or \'4.8mm\'.')

    size = plateData.shape
    curMesh = mesh.Mesh(np.array([], dtype=mesh.Mesh.dtype))
    glAllMesh = []
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

                shape = newMesh.points.shape
                points = newMesh.points.reshape(-1, 3)
                faces = np.arange(points.shape[0]).reshape(-1, 3)
                meshdata = gl.MeshData(vertexes=points, faces=faces)
                glMesh = gl.GLMeshItem(meshdata=meshdata, smooth=True,\
                        drawFaces=True, drawEdges=False, edgeColor=(0, 0, 0, 1))
                glMesh.setColor(color[plateData[i][j]])
                #print(f"color={color[plateData[i][j]]}")
                glMesh.scale(0.1,0.1,0.1)
                glAllMesh.append(glMesh)
                
                curMesh = ab.addBlock(curMesh, newMesh)
    
    x,y,z = mesh_location_zero(curMesh)

    for i in range(len(glAllMesh)):
        glAllMesh[i].translate(-x,-y,-z)

    return curMesh,glAllMesh
