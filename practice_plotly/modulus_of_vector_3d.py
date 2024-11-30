import plotly.graph_objects as go
import numpy as np

# Function to calculate modulus of vector
def compute_vector_magnitude(vector):
    return np.sqrt(np.sum(vector ** 2))

# Create vector
vector_a = np.array([2, 5, 4])

# Calculate modulus of vector
magnitude_a = compute_vector_magnitude(vector_a)

# Show result
print(f"Vector A: {vector_a}")
print(f"Modulus of vector A: {magnitude_a:.2f}")

# Visualization vector in plane
fig = go.Figure()

# Add vector to the graph
fig.add_trace(go.Scatter3d(x=[0, vector_a[0]], y=[0, vector_a[1]], z=[0, vector_a[2]],
    mode='lines+markers', marker=dict(size=5), line=dict(color='blue'), name='Vector A'))


# Add signature with vector modulus
fig.add_trace(go.Scatter3d(x=[vector_a[0] / 2], y=[vector_a[1] / 2], z=[vector_a[2] / 2],
    mode='text', text=[f'Modulus: {magnitude_a:.2f}'], textposition='bottom center', name='Modulus'))

# Setting of view of the graph
fig.update_layout(scene=dict(aspectmode='data'))
fig.update_layout(scene=dict(xaxis_title='Axis X', yaxis_title='Axis Y', zaxis_title='Axis Z'))
fig.update_layout(title='Vector modulus and visualization in 3D space')

# Show graph
fig.show()