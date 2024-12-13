import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.integrate import quad
from sympy.abc import x
from IPython.display import *
sp.init_printing(use_latex=True)

expr = (x*x + 1)**(-1/2)

#Calculation of derivative
derivative3 = sp.diff(expr, x)

# Create a function that can evaluate derivatives at points
derivative_function = sp.lambdify(x, derivative3, "numpy")

# Calculate derivatives at specified points
result5 = derivative_function(1)
result6 = derivative_function(-1/2)

print(derivative3, result5, result6)

fig, ax = plt.subplots(figsize=(15, 10))
# Move the left and bottom columns to x = 0 and y = 0, respectively.
ax.spines[["left", "bottom"]].set_position(("data", 0))

# Hide top and right line
ax.spines[["top", "right"]].set_visible(False)

# Draw arrows (as black triangles: "> k "/" ^k") at the ends of the axes.
# Also turn off the clipping (clip_on=False) arrows.
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Add intermediate lines
ax.grid(True, linestyle='-.')

# x, y = sp.symbols('x y')
x = sp.Symbol('x')

f = x**4 + 5*x**3 - 10*x
# f = (x-1)**3 + 20
df = f.diff()

x1 = np.linspace(-5, 3, 50)
f_lambd = sp.lambdify(x, f, 'numpy')
# y = [f.subs(x, i) for i in x1]
y = f_lambd(x1)

df_lambd = sp.lambdify(x, df, 'numpy')
dy = df_lambd(x1)

x_max = np.array([float(sp.expand_complex(i)) for i in sp.solve(df, x)])
y_max = f_lambd(x_max)

sns.lineplot(x=x1, y=y, ax=ax, color='orange')
sns.lineplot(x=x1, y=dy, ax=ax, color='blue')
sns.scatterplot(x=x_max, y=y_max, ax=ax, color='red')