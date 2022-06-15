import numpy as np
from stl import mesh

def cube_model(scaleX=1, scaleY=1, scaleZ=1):
    scaleX = scaleX / 2
    scaleY = scaleY / 2
    scaleZ = scaleZ / 2

    # Define the 8 vertices of the cube
    vertices = np.array([\
        [-1*scaleX, -1*scaleY, -1*scaleZ],
        [+1*scaleX, -1*scaleY, -1*scaleZ],
        [+1*scaleX, +1*scaleY, -1*scaleZ],
        [-1*scaleX, +1*scaleY, -1*scaleZ],
        [-1*scaleX, -1*scaleY, +1*scaleZ],
        [+1*scaleX, -1*scaleY, +1*scaleZ],
        [+1*scaleX, +1*scaleY, +1*scaleZ],
        [-1*scaleX, +1*scaleY, +1*scaleZ]])
    # Define the 12 triangles composing the cube
    faces = np.array([\
        [0,3,1],
        [1,3,2],
        [0,4,7],
        [0,7,3],
        [4,5,6],
        [4,6,7],
        [5,1,2],
        [5,2,6],
        [2,3,6],
        [3,7,6],
        [0,1,5],
        [0,5,4]])

    # Create the mesh
    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    cube.remove_duplicate_polygons=True
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j],:]

    return cube