# 🧠 Codebase Genius Report for `py_modules`

## 📂 Repository Structure

```
{ 'children': [ { 'name': '__pycache__',
                  'path': 'py_modules/__pycache__',
                  'type': 'dir'},
                { 'name': 'api_server.py',
                  'path': 'py_modules/api_server.py',
                  'type': 'file'},
                { 'name': 'ccg_builder.py',
                  'path': 'py_modules/ccg_builder.py',
                  'type': 'file'},
                { 'name': 'diagram.py',
                  'path': 'py_modules/diagram.py',
                  'type': 'file'},
                { 'name': 'docgen.py',
                  'path': 'py_modules/docgen.py',
                  'type': 'file'},
                { 'name': 'file_tree.py',
                  'path': 'py_modules/file_tree.py',
                  'type': 'file'},
                { 'name': 'parser_wrapper.py',
                  'path': 'py_modules/parser_wrapper.py',
                  'type': 'file'},
                { 'name': 'repo_clone.py',
                  'path': 'py_modules/repo_clone.py',
                  'type': 'file'}],
  'name': 'py_modules',
  'path': 'py_modules',
  'type': 'dir'}
```

## 🕸️ Code Context Graph

![Code Context Graph](outputs/py_modules/ccg_diagram.png)


## 🧩 Classes and Functions

### `parser_wrapper.py`

- **Function** `parse_python_file`

  - Doc: Parse a Python file using the built-in AST (Abstract Syntax Tree).
Returns structured info about its functions and classes.

### `diagram.py`

- **Function** `draw_ccg`

  - Doc: Draw a Code Context Graph (CCG) and save it as an image.
Requires Graphviz installed on the system.

### `ccg_builder.py`

- **Function** `build_ccg`

  - Doc: Build a Code Context Graph (CCG) of functions and classes across all Python files in a repo.
Nodes = functions/classes
Edges = inheritance or naive call relationships

### `api_server.py`

### `docgen.py`

- **Function** `generate_markdown_doc`

  - Doc: Generate a Markdown documentation file summarizing:
- Repository structure
- Classes and functions
- CCG diagram
Returns path to the Markdown file.

### `file_tree.py`

- **Function** `build_file_tree`

  - Doc: Walk through the directory and return a nested dictionary structure
representing the file tree.

- **Function** `find_readme_summary`

  - Doc: Find and read the README.md file in the repo (if available)
and return the first few lines as a summary.

### `repo_clone.py`
