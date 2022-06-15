import numpy as np
from stl import mesh

def mesh_update(my_mesh):
    my_mesh.update_areas()
    my_mesh.update_max()
    my_mesh.update_min()
    my_mesh.update_units()
    return my_mesh