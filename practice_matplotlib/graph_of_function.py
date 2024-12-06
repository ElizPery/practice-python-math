import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Move the left and bottom columns to x = 0 and y = 0, respectively
ax.spines[["left", "bottom"]].set_position(("data", 0))

# Hide the top and right line
ax.spines[["top", "right"]].set_visible(False)

# Draw arrows (as black triangles: "> k "/" ^k") at the ends of the axes
# Also turn off the clipping (clip_on=False) arrows
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Form a series of values of x. 100 elements from -10 to 10
x = np.linspace(-10, 10., 100)

# Add intermediate lines
ax.grid(True, linestyle='-.')

# Let's form a function y = x**2+2
ax.plot(x, x**2+2)

# Start drawing graphics
plt.show()
