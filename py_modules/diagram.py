# py_modules/diagram.py
import os
from graphviz import Digraph

def draw_ccg(G, out_dir: str, out_name="ccg", fmt="png"):
    """
    Draw a Code Context Graph (CCG) and save it as an image using Graphviz.
    Works without requiring pygraphviz — Streamlit and cloud safe.
    """
    os.makedirs(out_dir, exist_ok=True)

    graph = Digraph(format=fmt)
    graph.attr(rankdir="LR", splines="spline")

    # Add nodes
    for node in G.nodes:
        label = node.split("::")[-1]
        graph.node(node, label=label, shape="box", style="rounded,filled", fillcolor="lightgrey")

    # Add edges
    for u, v, data in G.edges(data=True):
        relation = data.get("relation", "")
        graph.edge(u, v, label=relation)

    # Save file
    output_path = os.path.join(out_dir, out_name)
    graph.render(output_path, cleanup=True)

    return f"{output_path}.{fmt}"
