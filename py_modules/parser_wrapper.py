# py_modules/parser_wrapper.py
import ast

def parse_python_file(path: str) -> dict:
    """
    Parse a Python file using the built-in AST (Abstract Syntax Tree).
    Returns structured info about its functions and classes.
    """
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            src = f.read()
    except Exception as e:
        return {"error": str(e), "path": path}

    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return {"error": f"SyntaxError: {e}", "path": path}

    module_doc = ast.get_docstring(tree)
    functions = []
    classes = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            functions.append({
                "name": node.name,
                "lineno": node.lineno,
                "doc": ast.get_docstring(node),
                "args": [a.arg for a in node.args.args]
            })
        elif isinstance(node, ast.ClassDef):
            methods = []
            for cnode in node.body:
                if isinstance(cnode, ast.FunctionDef):
                    methods.append({
                        "name": cnode.name,
                        "lineno": cnode.lineno,
                        "doc": ast.get_docstring(cnode),
                        "args": [a.arg for a in cnode.args.args]
                    })
            classes.append({
                "name": node.name,
                "lineno": node.lineno,
                "doc": ast.get_docstring(node),
                "bases": [getattr(b, 'id', str(b)) for b in node.bases],
                "methods": methods
            })

    return {
        "path": path,
        "module_doc": module_doc,
        "functions": functions,
        "classes": classes
    }
