# py_modules/api_server.py
from flask import Flask, request, jsonify, send_file
import os
import tempfile
from py_modules.repo_clone import clone_repo
from py_modules.docgen import generate_markdown_doc

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "🚀 Codebase Genius API is running!",
        "endpoints": {
            "/analyze": "POST - Analyze a GitHub repo. Requires 'repo_url' in JSON."
        }
    })

@app.route('/analyze', methods=['POST'])
def analyze_repo():
    """
    Endpoint: /analyze
    Input: JSON { "repo_url": "https://github.com/user/repo.git" }
    Output: JSON with path to generated documentation.
    """
    data = request.get_json()
    if not data or 'repo_url' not in data:
        return jsonify({"error": "Missing 'repo_url'"}), 400

    repo_url = data['repo_url']

    # Temporary directory to clone the repo
    tmp_dir = tempfile.mkdtemp()
    repo_path = os.path.join(tmp_dir, "repo")

    try:
        clone_repo(repo_url, repo_path)
        doc_path = generate_markdown_doc(repo_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "message": "✅ Documentation generated successfully!",
        "markdown_path": doc_path,
        "html_path": doc_path.replace(".md", ".html")
    })

@app.route('/download/<path:filename>')
def download_file(filename):
    """
    Endpoint to download generated documentation.
    Example: /download/outputs/myrepo/documentation.md
    """
    if not os.path.exists(filename):
        return jsonify({"error": "File not found"}), 404
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
