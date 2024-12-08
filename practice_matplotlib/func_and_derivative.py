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
fx = x**6+2*x**5-30*x**4+16*x**3-12*x**2+x+3
# We calculate the derivative of the function
dx = diff((fx))
k = []
n = []
l = []

for i in range(1000):
    j = ((i)*0.001)+3 # We set the interval - starting from 3 - a thousand times one thousandth - will be 1, so the search will go to 4.
    k.append(j)
    n.append(dx.subs(x,j))
    l.append(fx.subs(x,j))

ax.plot(k,n)
ax.plot(k,l)

# Start drawing graphics
plt.show()
