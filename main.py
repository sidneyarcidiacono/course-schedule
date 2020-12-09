"""Write our JSON file and use our graph to print our schedule."""
import json
from graph import Graph

f = open("course_prerequisites.json")
course_prereqs = json.load(f)


def json_to_graph(json, graph):
    """Take in JSON and create graph based on data."""
    for d in json:
        graph.add_vertex(d["name"], d["prerequisites"])
        if d["prerequisites"]:
            for prereq in d["prerequisites"]:
                graph.add_edge(d, graph.find_node(prereq))
    for v in graph.nodes:
        print(f"{v[0]} has {len(v[1])} prerequisites")
    return graph.print_graph()


graph = Graph()
json_to_graph(course_prereqs, graph)
