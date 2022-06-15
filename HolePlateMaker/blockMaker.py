import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from HolePlateMaker import mesh_scale as ms
from HolePlateMaker import mesh_scale as ms
from HolePlateMaker import mesh_scale as ms
from HolePlateMaker import mesh_update as mu
from HolePlateMaker import cube_model as c_m
from HolePlateMaker import mesh_location_zero as m_l_z
from HolePlateMaker import setBU32 as sbu32
from HolePlateMaker import addBlock as ab


curMesh = sbu32.setBU32(0,0,0)
for i in range(1,10):
    for j in range(0,i+1):
        newMesh = sbu32.setBU32(i,j,0)
        curMesh = ab.addBlock(curMesh, newMesh)

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(curMesh.vectors))

# Auto scale to the mesh size
scale = curMesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()

curMesh.save('myPlate.stl')