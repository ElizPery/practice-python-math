import numpy as np

def normal_vector(u, v):
    # Calculate cross product
    n = np.cross(u, v)

    return n

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

normal = normal_vector(u, v)
print("Plane normal vector:", normal)