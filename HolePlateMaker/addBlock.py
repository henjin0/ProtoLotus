import numpy as np
from stl import mesh

def addBlock(curMesh, newMesh):
    curMesh = mesh.Mesh(np.concatenate([
        curMesh.data.copy(),
        newMesh.data.copy(),
    ]))
    return curMesh
