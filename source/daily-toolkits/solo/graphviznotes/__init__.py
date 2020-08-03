# -*- coding:utf-8 -*-

"""
1. www.graphviz.org/doc/info/shapes.html
2. www.graphviz.org/doc/info/arrows.html
3. www.graphviz.org/doc/info/colors.html
4. www.graphviz.org/doc/info/attrs.html#k:color

Usage: 
add_edges(
    add_nodes(gd, [
        ('A', {'label': 'Node A'}),
        ('B', {'label': 'Node B'}),
        'C'
    ]),
    [
        (('A', 'B'), {'label': 'Edge 1'}),
        (('A', 'C'), {'label': 'Edge 2'}),
        ('B', 'C')
    ]
).render('img/g5')
"""


def apply_styles(graph, styles):
    """
    style applied:
     styles = {
        'graph': {
            'label': 'A Fancy Graph',
            'fontsize': '16',
            'fontcolor': 'white',
            'bgcolor': '#333333',
            'rankdir': 'BT',
        },
        'nodes': {
            'fontname': 'Helvetica',
            'shape': 'hexagon',
            'fontcolor': 'white',
            'color': 'white',
            'style': 'filled',
            'fillcolor': '#006699',
        },
        'edges': {
            'style': 'dashed',
            'color': 'white',
            'arrowhead': 'open',
            'fontname': 'Courier',
            'fontsize': '12',
            'fontcolor': 'white',
        }
    }
    """
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph
