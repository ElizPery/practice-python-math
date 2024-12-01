import matplotlib.pyplot as plt
import numpy as np

# Function to calculate module of vector
def compute_vector_magnitude(vector):
    return np.sqrt(np.sum(vector ** 2))

# Function to calculate guide cosines
def compute_direction_cosines(vector):
    magnitude = compute_vector_magnitude(vector)
    cosine_alpha = vector[0] / magnitude
    cosine_beta = vector[1] / magnitude
    cosine_gamma = vector[2] / magnitude
    return cosine_alpha, cosine_beta, cosine_gamma

# Create vector
vector_a = np.array([2, 3, 4])

# Calculate guide cosines
cosine_alpha, cosine_beta, cosine_gamma = compute_direction_cosines(vector_a)

# Show result
print(f"Vector A: {vector_a}")
print(f"Guide cosines: α={cosine_alpha:.2f}, β={cosine_beta:.2f}, γ={cosine_gamma:.2f}")

# Visualize a vector on a plane
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, vector_a[0], vector_a[1], vector_a[2], color='b', label='Vector A')

# Add captions with guide cosines
ax.text(vector_a[0] / 2, vector_a[1] / 2, vector_a[2] / 2, f'α={cosine_alpha:.2f}\nβ={cosine_beta:.2f}\nγ={cosine_gamma:.2f}',
    color='r')

# Setting of view of the graph
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])
ax.set_xlabel('Axis X')
ax.set_ylabel('Axis Y')
ax.set_zlabel('Axis Z')
ax.set_title('Vector direction cosines on plane')

plt.legend()
plt.show()
