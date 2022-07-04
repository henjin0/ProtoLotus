import numpy as np
from stl import mesh
from HolePlateMaker import mesh_scale as m_s
from HolePlateMaker import mesh_update as m_u
from HolePlateMaker import mesh_location_zero as m_l_z
from HolePlateMaker import resourcePath as rp

def setNU32(xPoint,yPoint,zPoint):
    your_mesh = mesh.Mesh.from_file(rp.resourcePath('HolePlateMaker/NU3.2mm.stl'))
    your_mesh = m_l_z.mesh_location_zero(your_mesh)
    your_mesh = m_u.mesh_update(your_mesh)
    your_mesh.translate(np.array([xPoint*5,yPoint*5,zPoint*3]))
    your_mesh = m_u.mesh_update(your_mesh)

    return your_mesh