import numpy as np
from stl import mesh

def mesh_location_zero(my_mesh):
    midPosRel = (my_mesh.max_ - my_mesh.min_)/2
    my_mesh.x = my_mesh.x - (midPosRel[0] + my_mesh.min_[0])
    my_mesh.y = my_mesh.y - (midPosRel[1] + my_mesh.min_[1])
    my_mesh.z = my_mesh.z - (midPosRel[2] + my_mesh.min_[2])
    return my_mesh