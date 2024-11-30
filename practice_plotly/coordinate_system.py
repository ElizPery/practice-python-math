import plotly.graph_objects as go
import numpy as np

# Create object "Figure" for graph
fig = go.Figure()

# Add horizontal axis X
fig.add_trace(go.Scatter(x=[-10, 10], y=[0, 0], mode='lines', name='X-вісь'))

# Add vertical axis Y
fig.add_trace(go.Scatter(x=[0, 0], y=[-10, 10], mode='lines', name='Y-вісь'))

# Elevation for origin
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=8, color='red'), name='Початок координат'))

# Add a coordinate grid
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

# Image of some points
points_x = np.random.randint(-8, 8, 5)
points_y = np.random.randint(-8, 8, 5)

fig.add_trace(go.Scatter(x=points_x, y=points_y, mode='markers', marker=dict(size=10, color='blue'), name='Точка'))

# Setting of view of the graph
fig.update_layout(
    title='Координатна система на площині з точками',
    xaxis=dict(title='Вісь X'),
    yaxis=dict(title='Вісь Y'),
    showlegend=True
)

# Show graph
fig.show()