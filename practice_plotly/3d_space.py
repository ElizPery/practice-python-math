import plotly.graph_objects as go
import numpy as np

# Generate points
num_points = 10
points_x = np.random.rand(num_points) * 10
points_y = np.random.rand(num_points) * 10
points_z = np.random.rand(num_points) * 10

# Create object "Figure" for 3D graph
fig = go.Figure()

# Add points in 3D space
fig.add_trace(go.Scatter3d(
    x=points_x,
    y=points_y,
    z=points_z,
    mode='markers',
    marker=dict(
        size=5,
        color='blue',
        opacity=0.8
    ),
    name='Random Points'
))


# Setting of view of the graph
fig.update_layout(
    scene=dict(
        xaxis=dict(title='Axis X'),
        yaxis=dict(title='Axis Y'),
        zaxis=dict(title='Axis Z')
    ),
    title='3D space with points',
)


# Show graph
fig.show()