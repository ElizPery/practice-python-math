import matplotlib.pyplot as plt
import numpy as np

def draw_vectors(vectors, colors=None, title=None):
    """
    Function for drawing multiple vectors on a plane using library tools Matplotlib.

    Params:
    - vectors: List of tuples (start_point, end_point), where start_point and end_point - these are the coordinates of the start and end points of the vector.
    - colors: Color list for vectors (default is 'blue' for all vectors).
    """
    num_vectors = len(vectors)

    if colors is None:
        colors = ['blue'] * num_vectors

    if title is None:
        title = 'Multiple vectors on plane'

    # Create a new drawing and axes
    fig, ax = plt.subplots()

    for i in range(num_vectors):
        start_point, end_point = vectors[i]

        # Definition of vector and its length
        vector = np.array([end_point[0] - start_point[0], end_point[1] - start_point[1]])
        length = np.linalg.norm(vector)

        # Vector normalization
        # normalized_vector = vector / length
        normalized_vector = vector

        # Add an arrow to axes
        ax.arrow(start_point[0], start_point[1], normalized_vector[0], normalized_vector[1],
            head_width=0.1, head_length=0.1, fc=colors[i], ec=colors[i])

    # Setting of view of the graph
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

    # Show graph
    plt.show()

# Example of using a function with multiple vectors and colors
vectors = [((1, 2), (4, 6)), ((2, 3), (5, 2)), ((0, 0), (-2, 4))]
colors = ['green', 'red', 'purple']

draw_vectors(vectors, colors)