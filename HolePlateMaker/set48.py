import numpy as np
from stl import mesh
from HolePlateMaker import mesh_scale as m_s
from HolePlateMaker import mesh_update as m_u
from HolePlateMaker import mesh_location_zero as m_l_z
from HolePlateMaker import resourcePath as rp

def set48(xPoint,yPoint,zPoint,filepath,way=0):
    your_mesh = mesh.Mesh.from_file(rp.resourcePath(filepath))
    if(way==2):
        your_mesh.rotate(np.array([0,0,1]),np.deg2rad(180))
    elif(way==3):
        your_mesh.rotate(np.array([0,0,1]),np.deg2rad(90))
    elif(way==4):
        your_mesh.rotate(np.array([0,0,1]),np.deg2rad(270))
    your_mesh = m_l_z.mesh_location_zero(your_mesh)
    your_mesh = m_u.mesh_update(your_mesh)
    your_mesh.translate(np.array([xPoint*7.97,yPoint*7.97,zPoint*6]))
    your_mesh = m_u.mesh_update(your_mesh)

    return your_mesh