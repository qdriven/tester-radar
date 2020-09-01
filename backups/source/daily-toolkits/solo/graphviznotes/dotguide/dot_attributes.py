# -*- coding:utf-8 -*-
"""
http://www.graphviz.org/doc/info/attrs.html
"""
import graphviz as gv
from graphviznotes import add_nodes, add_edges

graph = gv.Digraph(format='png')

nodes = ["main", "parse", "execute", "init", "cleanup", "make_string", "printf", "compare"]
edge_relative = {
    "main": ["parse", "execute", "init", "cleanup", "printf"],
    "execute": ["printf", "make_string", "compare"],
    "init": ["make_string"]
}

