import numpy as np
from stl import mesh
from HolePlateMaker import setBU32 as sbu32
from HolePlateMaker import addBlock as ab


def NumpyBoolArrayToPlate(plateData):
    size = plateData.shape
    curMesh = mesh.Mesh(np.array([], dtype=mesh.Mesh.dtype))
    for i in np.arange(0,size[0]):
        for j in np.arange(0,size[1]):
            if(plateData[i][j]):
                newMesh = sbu32.setBU32(i,j,0)
                curMesh = ab.addBlock(curMesh, newMesh)
    
    return curMesh
