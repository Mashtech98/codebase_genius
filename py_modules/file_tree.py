# py_modules/file_tree.py
import os

IGNORE_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}

def build_file_tree(root_path: str, max_depth: int = 6) -> dict:
    """
    Walk through the directory and return a nested dictionary structure
    representing the file tree.
    """
    def walk(path, depth):
        name = os.path.basename(path)
        node = {
            "name": name,
            "path": path,
            "type": "dir" if os.path.isdir(path) else "file"
        }

        # Recursively walk into subfolders
        if os.path.isdir(path) and depth < max_depth and name not in IGNORE_DIRS:
            node["children"] = []
            try:
                for entry in sorted(os.listdir(path)):
                    node["children"].append(walk(os.path.join(path, entry), depth + 1))
            except PermissionError:
                node["error"] = "Permission denied"
        return node

    return walk(root_path, 0)

def find_readme_summary(root_path: str, n_lines=20) -> str:
    """
    Find and read the README.md file in the repo (if available)
    and return the first few lines as a summary.
    """
    for fname in ["README.md", "readme.md", "ReadMe.md"]:
        readme_path = os.path.join(root_path, fname)
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.read().splitlines()
            non_empty = [line for line in lines if line.strip()]
            return "\n".join(non_empty[:n_lines])
    return "No README.md file found in this repository."
