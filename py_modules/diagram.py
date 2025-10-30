# py_modules/diagram.py
import os
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph

def draw_ccg(G, out_dir: str, out_name="ccg", fmt="png"):
    """
    Draw a Code Context Graph (CCG) and save it as an image.
    Requires Graphviz installed on the system.
    """
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    # Convert to Graphviz AGraph
    A = to_agraph(G)

    # Simplify node labels (remove long file paths)
    for node in G.nodes:
        n = A.get_node(node)
        label = node.split("::")[-1]
        n.attr['label'] = label

    # Render and save
    output_path = os.path.join(out_dir, f"{out_name}.{fmt}")
    A.layout('dot')  # use the DOT layout engine (hierarchical)
    A.draw(output_path)

    return output_path
