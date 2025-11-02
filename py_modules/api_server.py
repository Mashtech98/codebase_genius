# py_modules/api_server.py
from flask import render_template
from flask import Flask, request, jsonify, send_file
import os
import tempfile
from py_modules.repo_clone import clone_repo
from py_modules.docgen import generate_markdown_doc
from flask import render_template


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


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

        # Optional: load summary text directly from the doc file (first few lines)
    summary_text = ""
    try:
        with open(doc_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("## 🤖 AI Summary"):
                    summary_text = "".join(lines[lines.index(line)+1:lines.index(line)+5])
                    break
    except Exception:
        summary_text = "(Summary not found in file.)"

    return jsonify({
        "message": "✅ Documentation generated successfully!",
        "markdown_path": doc_path,
        "html_path": doc_path.replace(".md", ".html"),
        "ai_summary": summary_text
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

@app.route('/ui')
def ui_page():
    # Home Page (Dashboard Welcome)
    return render_template('index.html', active='home')


@app.route('/generate', methods=['GET', 'POST'])
def generate_docs_page():
    if request.method == 'POST':
        repo_url = request.form.get('repo_url')
        if not repo_url:
            return render_template('generate.html', error="Please enter a GitHub repository URL.", active='generate')
        
        try:
            import tempfile, os
            from py_modules.repo_clone import clone_repo
            from py_modules.docgen import generate_markdown_doc
            from py_modules.ai_summary_gemini import summarize_codebase

            tmp_dir = tempfile.mkdtemp()
            repo_path = os.path.join(tmp_dir, "repo")
            clone_repo(repo_url, repo_path)
            markdown_path = generate_markdown_doc(repo_path)

            summary = summarize_codebase(f"This repository was analyzed from {repo_url}.")
            
            return render_template('generate.html',
                                   success=True,
                                   repo_url=repo_url,
                                   markdown_path=markdown_path,
                                   summary=summary,
                                   active='generate')
        except Exception as e:
            return render_template('generate.html', error=str(e), active='generate')

    # If GET, show empty form
    return render_template('generate.html', active='generate')


@app.route('/analytics')
def analytics_page():
    return render_template('analytics.html', active='analytics')


@app.route('/settings')
def settings_page():
    return render_template('settings.html', active='settings')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
