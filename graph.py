"""Define our graph structure as a class."""
from vertex import Vertex
from edge import Edge


class Graph:
    """Create our graph."""

    def __init__(self):
        """Initialize nodes and edges."""
        self.nodes = []
        self.edges = []

    def add_vertex(self, id, value):
        """Add vertex to graph."""
        new_node = Vertex(id, value)
        self.nodes.append((new_node.id, new_node.value))

    def add_edge(self, start_node, end_node):
        """Add edge (connection) between two vertices."""
        if not self.nodes[start_node] or not self.nodes[end_node]:
            return "Start or end node does not exist."
        new_edge = Edge(start_node, end_node)
        edge_tuple = (new_edge.start_node, new_edge.end_node)
        self.edges.append(edge_tuple)

    def print_graph(self):
        """Print nodes and edges in graph."""
        print(f"Nodes: {self.nodes}")
        print(f"Edges: {self.edges}")
