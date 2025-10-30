# py_modules/repo_clone.py
import git
import os

def clone_repo(repo_url: str, dest_path: str):
    """
    Clone a GitHub repository to the given destination path.
    """
    if os.path.exists(dest_path):
        return f"Repository already exists at {dest_path}"

    try:
        git.Repo.clone_from(repo_url, dest_path)
        return f"✅ Repository cloned successfully to {dest_path}"
    except Exception as e:
        raise Exception(f"Error cloning repo: {e}")
