# py_modules/docgen.py
import os
import markdown2
from py_modules.file_tree import build_file_tree
from py_modules.parser_wrapper import parse_python_file
from py_modules.ccg_builder import build_ccg
from py_modules.diagram import draw_ccg

def generate_markdown_doc(repo_path: str, out_dir: str = "outputs") -> str:
    """
    Generate a Markdown documentation file summarizing:
    - Repository structure
    - Classes and functions
    - CCG diagram
    Returns path to the Markdown file.
    """

    repo_name = os.path.basename(os.path.normpath(repo_path))
    output_folder = os.path.join(out_dir, repo_name)
    os.makedirs(output_folder, exist_ok=True)

    md_content = [f"# 🧠 Codebase Genius Report for `{repo_name}`\n"]

    # Section 1: File tree
    md_content.append("## 📂 Repository Structure\n")
    tree = build_file_tree(repo_path)
    from pprint import pformat
    md_content.append("```\n" + pformat(tree, indent=2) + "\n```\n")

        # Section 2: Code context graph
    md_content.append("## 🕸️ Code Context Graph\n")
    G = build_ccg(repo_path)
    graph_path = draw_ccg(G, output_folder, "ccg_diagram")
    md_content.append(f"![Code Context Graph]({graph_path})\n\n")

    # Section 3: Parsed classes & functions
    md_content.append("## 🧩 Classes and Functions\n")
    for root, _, files in os.walk(repo_path):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                info = parse_python_file(path)
                if info.get("error"):
                    continue
                relpath = os.path.relpath(path, repo_path)
                md_content.append(f"### `{relpath}`\n")
                if info.get("module_doc"):
                    md_content.append(f"> {info['module_doc']}\n\n")
                for c in info.get("classes", []):
                    md_content.append(f"- **Class** `{c['name']}`\n")
                    if c.get("doc"):
                        md_content.append(f"  - Doc: {c['doc']}\n")
                    for m in c.get("methods", []):
                        md_content.append(f"  - Method: `{m['name']}`\n")
                for f_ in info.get("functions", []):
                    md_content.append(f"- **Function** `{f_['name']}`\n")
                    if f_.get("doc"):
                        md_content.append(f"  - Doc: {f_['doc']}\n")

    # Combine all Markdown
    md_text = "\n".join(md_content)
    md_path = os.path.join(output_folder, "documentation.md")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)

    # Optionally convert to HTML (for previews)
    html_path = os.path.join(output_folder, "documentation.html")
    html_content = markdown2.markdown(md_text)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return md_path
