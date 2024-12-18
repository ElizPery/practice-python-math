import numpy as np
import matplotlib.pyplot as plt
import random

N=1000 # sample size
X = [] # Empty array for filling

# A cycle of 1000 iterations, on each of which we add 1 random element with a normal distribution, with an average of 10 and a standard deviation of 5
for i in range(N):
    X.append(random.normalvariate(10,5))

# 2 arrays are formed: n - number of elements falling into the interval, x - array of interval boundaries
print(np.histogram(X, bins=10))
n,x=np.histogram(X, bins=10)

# array of interval beginnings (removed last, largest value)
xmin=x[:-1]

# interval width (difference of two consecutive columns)
dx=x[1]-x[0]

# empirical reduced frequency: the proportion of the number of elements in the interval and the total number of elements
y=n/N

# array of interval centers
xmid=xmin+dx/2
# derive an empirical histogram of reduced frequencies
plt.bar(xmid, y, width=dx, color='y')

# Display signatures on axes
plt.xlabel('x')
plt.ylabel('Frequency (probability)')

# Draw a grid and histogram
plt.grid()
plt.show()