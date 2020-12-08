"""Define our edges and their properties."""


class Edge:
    """Define edge."""

    def __init__(self, start_node, end_node):
        """Define properties to define direction of edge."""
        self.start_node = start_node
        self.end_node = end_node
