import sys
import numpy as np
from stl import mesh
from HolePlateMaker import setBU32 as sbu32
from HolePlateMaker import setBU48 as sbu48
from HolePlateMaker import setABU48 as sabu48
from HolePlateMaker import addBlock as ab


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
