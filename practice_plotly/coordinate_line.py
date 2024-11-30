import plotly.graph_objects as go
import numpy as np

# Generate points
num_points = 10
points_x = np.random.randint(-10, 10, num_points)
points_y = np.zeros(num_points)

# Create object "Figure" for graph
fig = go.Figure()

# Add horizontal axis X
fig.add_trace(go.Scatter(x=[-10, 10], y=[0, 0], mode='lines', name='X-axis'))

# Add points to coordinate line
fig.add_trace(go.Scatter(x=points_x, y=points_y, mode='markers', name='Points'))


# Setting of view of the graph
fig.update_layout(
    title='Coordinate line with points',
    xaxis=dict(title='Axis X'),
    yaxis=dict(title='Axis Y'),
    showlegend=True
)


# Show graph
fig.show()
