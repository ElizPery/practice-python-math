import matplotlib.pyplot as plt
from sympy import diff, symbols

fig, ax = plt.subplots()

# Move the left and bottom columns to x = 0 and y = 0, respectively
ax.spines[["left", "bottom"]].set_position(("data", 0))

# Hide top and right line
ax.spines[["top", "right"]].set_visible(False)

# Draw arrows (as black triangles: "> k "/" ^k") at the ends of the axes
# Also turn off the clipping (clip_on=False) arrows
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Add intermediate lines
ax.grid(True, linestyle='-.')

# We form a series of values of x. 100 elements from -2 to 2.

x, y = symbols('x y')
# We set the function
fx = -3*x*x + 30*x
# We calculate the derivative of the function
dx = diff((fx))
k = []
n = []
l = []

for i in range(1000):
    j = (i)*0.01
    k.append(j)
    n.append(dx.subs(x,j))
    l.append(fx.subs(x,j))

# We visualize the graphs of the function and its derivative
ax.plot(k,n)
ax.plot(k,l)

# Visualize the maximum point
x_element = [5]
y_element = [75]
ax.scatter(x_element, y_element, c="red")

# Start drawing graphics
plt.show()
