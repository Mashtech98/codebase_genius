import streamlit as st
import tempfile
import os
from py_modules.repo_clone import clone_repo
from py_modules.docgen import generate_markdown_doc
from py_modules.ai_summary_gemini import summarize_codebase

st.set_page_config(page_title="Codebase Genius", page_icon="🚀", layout="wide")

# Sidebar
st.sidebar.title("🚀 Codebase Genius")
st.sidebar.markdown("### Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Generate Docs", "Analytics", "Settings"])

st.sidebar.divider()
st.sidebar.caption("© 2025 Codebase Genius")

# Home Page
if page == "Home":
    st.title("🎉 Welcome to Codebase Genius")
    st.markdown("AI-powered codebase documentation and summarization tool.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Projects Processed", "15", "+3 today")
    with col2:
        st.metric("Success Rate", "98%")
    with col3:
        st.metric("AI Model", "Gemini 2.5 Flash")

# Generate Docs Page
elif page == "Generate Docs":
    st.title("📚 Generate Documentation")

    repo_url = st.text_input("Enter a GitHub Repository URL", placeholder="https://github.com/username/repo.git")
    generate_button = st.button("🚀 Generate Documentation")

    if generate_button:
        if not repo_url.strip():
            st.error("Please enter a valid GitHub repository URL.")
        else:
            with st.spinner("Cloning and analyzing repository... ⏳"):
                try:
                    tmp_dir = tempfile.mkdtemp()
                    repo_path = os.path.join(tmp_dir, "repo")
                    clone_repo(repo_url, repo_path)
                    markdown_path = generate_markdown_doc(repo_path)
                    summary = summarize_codebase(f"This repository was analyzed from {repo_url}.")

                    st.success("✅ Documentation generated successfully!")
                    st.markdown(f"**Markdown Path:** `{markdown_path}`")
                    st.markdown("### 🤖 AI Summary")
                    st.info(summary)

                    with open(markdown_path, "r") as f:
                        st.download_button("⬇️ Download Markdown", f, file_name="documentation.md")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

# Analytics Page
elif page == "Analytics":
    st.title("📊 Analytics Dashboard (Coming Soon)")
    st.info("This section will display usage statistics and AI performance metrics.")

# Settings Page
elif page == "Settings":
    st.title("⚙️ Settings")
    st.markdown("Manage API keys, preferences, and customization here.")
    st.text_input("Google API Key", type="password")
