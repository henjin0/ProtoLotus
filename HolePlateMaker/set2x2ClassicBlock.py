import numpy as np
from stl import mesh
from HolePlateMaker import mesh_scale as m_s
from HolePlateMaker import mesh_update as m_u
from HolePlateMaker import mesh_location_zero as m_l_z
from HolePlateMaker import resourcePath as rp

def set2x2ClassicBlock(xPoint,yPoint,zPoint,filepath):
    your_mesh = mesh.Mesh.from_file(rp.resourcePath(filepath))
    your_mesh = m_l_z.mesh_location_zero(your_mesh)
    your_mesh = m_u.mesh_update(your_mesh)
    
    # CBNSはスタッドが無いためオフセットをかける必要がある。
    if(filepath == "setting/blocks/2x2CBNS.stl"):
        your_mesh.translate(np.array([xPoint*15.972,yPoint*15.972,zPoint*4.8944 - 1.7/2])) # 4.8944=Stad*2/5(block height)
    else:
        your_mesh.translate(np.array([xPoint*15.972,yPoint*15.972,zPoint*4.8944])) # 4.8944=Stad*2/5(block height) + 1.7(Stad height)
    
    your_mesh = m_u.mesh_update(your_mesh)

    return your_mesh