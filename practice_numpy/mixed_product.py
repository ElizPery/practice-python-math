import numpy as np

# Vectors
a = np.array([1, 1/3, 0])
b = np.array([0, 2, 1/4])
c = np.array([1/2, 1/2, 1])

# Mixed product a, b і c
mixed_dot_product = np.linalg.det(np.dstack([a,b,c]))
print(mixed_dot_product)
