# -*- coding:utf-8 -*-

import graphviz as gv

from graphviznotes import add_nodes, add_edges

graph = gv.Digraph(format='png')

nodes = ["main", "parse", "execute", "init", "cleanup", "make_string", "printf", "compare"]
edge_relative = {
    "main": ["parse", "execute", "init", "cleanup", "printf"],
    "execute": ["printf", "make_string", "compare"],
    "init": ["make_string"]
}

def make_edges_definitions(nodes=[]):
    pass


def make_edges(edge_relationship={}):
    edge_result = []
    if len(edge_relationship) == 0:
        return
    for start_node, child_nodes in edge_relationship.items():
        for child_node in child_nodes:
            edge_result.append((start_node, child_node))
    return edge_result

print(make_edges(edge_relative))

add_nodes(graph,nodes=nodes)
add_edges(graph,edges=make_edges(edge_relative))
print(graph.source)
graph.render("guide_files/attr_graph")

