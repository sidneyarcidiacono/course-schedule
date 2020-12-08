"""Define our graph structure as a class."""
from vertex import Vertex
from edge import Edge


class Graph:
    """Create our graph."""

    def __init__(self):
        """Initialize nodes and edges."""
        self.nodes = {}
        self.edges = []

    def add_vertex(self, id, value):
        """Add vertex to graph."""
        new_node = Vertex(id, value)
        if self.nodes[new_node.id]:
            return "This node already exists."
        self.nodes[new_node.id] = new_node.value

    def add_edge(self, start_node, end_node):
        """Add edge (connection) between two vertices."""
        if not self.nodes[start_node] or not self.nodes[end_node]:
            return "Start or end node does not exist."
        new_edge = Edge(start_node, end_node)
        self.edges.append(new_edge)
