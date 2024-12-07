import sympy as sp
from sympy.abc import x

expr = (x*x + 1)**(-1/2)

#Calculation of derivative
derivative3 = sp.diff(expr, x)

# Create a function that can evaluate derivatives at points
derivative_function = sp.lambdify(x, derivative3, "numpy")

# Calculate derivatives at specified points
result5 = derivative_function(1)
result6 = derivative_function(-1/2)

derivative3, result5, result6