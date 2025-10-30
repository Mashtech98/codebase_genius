# py_modules/ccg_builder.py
import networkx as nx
import os
import glob
from py_modules.parser_wrapper import parse_python_file

def build_ccg(repo_root: str, target_files: list = None) -> nx.DiGraph:
    """
    Build a Code Context Graph (CCG) of functions and classes across all Python files in a repo.
    Nodes = functions/classes
    Edges = inheritance or naive call relationships
    """
    G = nx.DiGraph()

    # Get Python files
    if target_files:
        python_files = [os.path.join(repo_root, f) for f in target_files]
    else:
        python_files = glob.glob(os.path.join(repo_root, "**", "*.py"), recursive=True)

    for p in python_files:
        info = parse_python_file(p)
        if info.get("error"):
            continue

        mod = os.path.relpath(p, repo_root)

        # Add functions as nodes
        for f in info.get("functions", []):
            node_name = f"{mod}::{f['name']}"
            G.add_node(node_name, type="function", file=mod, doc=f.get("doc"))

        # Add classes as nodes and their methods as connected nodes
        for c in info.get("classes", []):
            class_node = f"{mod}::{c['name']}"
            G.add_node(class_node, type="class", file=mod, doc=c.get("doc"))
            # Add edges for inheritance
            for base in c.get("bases", []):
                G.add_edge(class_node, f"base::{base}", relation="inherits")

            # Connect class -> its methods
            for m in c.get("methods", []):
                method_node = f"{class_node}::{m['name']}"
                G.add_node(method_node, type="method", file=mod, doc=m.get("doc"))
                G.add_edge(class_node, method_node, relation="contains")

    return G
