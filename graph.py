"""Define our graph structure as a class."""
from vertex import Vertex
from edge import Edge


class Graph:
    """Create our graph."""

    def __init__(self):
        """Initialize nodes and edges."""
        self.nodes = None
        self.edges = []

    def add_vertex(self, id, value):
        """Add vertex to graph."""
        new_node = Vertex(id, value)
        if self.nodes is not None and new_node.id in self.nodes:
            return "This node already exists."
        elif self.nodes is None:
            self.nodes = {new_node.id: new_node.value}
        elif new_node.id not in self.nodes and self.nodes is not None:
            self.nodes[new_node.id] = new_node.value

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


graph = Graph()
graph.add_vertex(1, "hello")
graph.add_vertex(2, "sid")
graph.add_vertex(3, "starlight")

graph.add_edge(1, 2)
graph.add_edge(2, 3)

graph.print_graph()
