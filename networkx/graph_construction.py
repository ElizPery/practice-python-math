import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add vertices
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges (connections between vertices)
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])

# Graph visualization
pos = nx.spring_layout(G)  # Defining Vertex Positions
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10, edge_color='gray')
plt.show()