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

    # === Gemini AI Summary Integration ===
    try:
        from py_modules.ai_summary_gemini import summarize_codebase
        print("🤖 Generating AI summary using Gemini...")

        # Collect a preview of the repo's Python files
        repo_preview = ""
        for root, _, files in os.walk(repo_path):
            for file in files:
                if file.endswith(".py") and len(repo_preview) < 8000:  # read up to ~8 KB
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            snippet = f.read(500)
                            repo_preview += f"\n\n### File: {file}\n{snippet}"
                    except Exception as e:
                        print(f"⚠️ Skipping {file_path}: {e}")
                        continue

        if not repo_preview.strip():
            repo_preview = "No Python source code detected in this repository."

        summary_text = summarize_codebase(
            "You are an AI code analyst. "
            "Here are excerpts from a Python repository:\n\n"
            f"{repo_preview}\n\n"
            "Write a concise summary (3–5 sentences) describing what this repository does, "
            "who would use it, and its main components."
        )

        md_content.append("## 🤖 AI Summary (Gemini)\n\n")
        md_content.append(summary_text + "\n\n---\n")

    except Exception as e:
        md_content.append(f"⚠️ AI summary could not be generated: {e}\n\n---\n")


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
