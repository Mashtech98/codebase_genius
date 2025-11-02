# 🧠 Codebase Genius Report for `repo`

## 🤖 AI Summary (Gemini)


This repository contains the **Requests library**, a popular and user-friendly HTTP client for Python. It provides a simple yet powerful API for making various types of HTTP requests (GET, POST, PUT, DELETE, etc.) to interact with web services and APIs. Developers use it extensively for tasks like fetching web content, sending data, and integrating with RESTful services.

Key components include transport adapters for managing connections, authentication handlers, cookie management, SSL certificate handling, and structured objects for requests and responses. The library simplifies common HTTP patterns, handles exceptions gracefully, and supports Python 3.9 and later, offering a robust solution for all HTTP communication needs.

---

## 📂 Repository Structure

```
{ 'children': [ { 'name': '.coveragerc',
                  'path': '/tmp/tmp57hgqreb/repo/.coveragerc',
                  'type': 'file'},
                { 'name': '.git',
                  'path': '/tmp/tmp57hgqreb/repo/.git',
                  'type': 'dir'},
                { 'name': '.git-blame-ignore-revs',
                  'path': '/tmp/tmp57hgqreb/repo/.git-blame-ignore-revs',
                  'type': 'file'},
                { 'children': [ { 'name': 'CODE_OF_CONDUCT.md',
                                  'path': '/tmp/tmp57hgqreb/repo/.github/CODE_OF_CONDUCT.md',
                                  'type': 'file'},
                                { 'name': 'CONTRIBUTING.md',
                                  'path': '/tmp/tmp57hgqreb/repo/.github/CONTRIBUTING.md',
                                  'type': 'file'},
                                { 'name': 'FUNDING.yml',
                                  'path': '/tmp/tmp57hgqreb/repo/.github/FUNDING.yml',
                                  'type': 'file'},
                                { 'children': [ { 'name': 'Bug_report.md',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/ISSUE_TEMPLATE/Bug_report.md',
                                                  'type': 'file'},
                                                { 'name': 'Custom.md',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/ISSUE_TEMPLATE/Custom.md',
                                                  'type': 'file'},
                                                { 'name': 'Feature_request.md',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/ISSUE_TEMPLATE/Feature_request.md',
                                                  'type': 'file'}],
                                  'name': 'ISSUE_TEMPLATE',
                                  'path': '/tmp/tmp57hgqreb/repo/.github/ISSUE_TEMPLATE',
                                  'type': 'dir'},
                                { 'name': 'ISSUE_TEMPLATE.md',
                                  'path': '/tmp/tmp57hgqreb/repo/.github/ISSUE_TEMPLATE.md',
                                  'type': 'file'},
                                { 'name': 'SECURITY.md',
                                  'path': '/tmp/tmp57hgqreb/repo/.github/SECURITY.md',
                                  'type': 'file'},
                                { 'name': 'dependabot.yml',
                                  'path': '/tmp/tmp57hgqreb/repo/.github/dependabot.yml',
                                  'type': 'file'},
                                { 'children': [ { 'name': 'close-issues.yml',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/workflows/close-issues.yml',
                                                  'type': 'file'},
                                                { 'name': 'codeql-analysis.yml',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/workflows/codeql-analysis.yml',
                                                  'type': 'file'},
                                                { 'name': 'lint.yml',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/workflows/lint.yml',
                                                  'type': 'file'},
                                                { 'name': 'lock-issues.yml',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/workflows/lock-issues.yml',
                                                  'type': 'file'},
                                                { 'name': 'publish.yml',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/workflows/publish.yml',
                                                  'type': 'file'},
                                                { 'name': 'run-tests.yml',
                                                  'path': '/tmp/tmp57hgqreb/repo/.github/workflows/run-tests.yml',
                                                  'type': 'file'}],
                                  'name': 'workflows',
                                  'path': '/tmp/tmp57hgqreb/repo/.github/workflows',
                                  'type': 'dir'}],
                  'name': '.github',
                  'path': '/tmp/tmp57hgqreb/repo/.github',
                  'type': 'dir'},
                { 'name': '.gitignore',
                  'path': '/tmp/tmp57hgqreb/repo/.gitignore',
                  'type': 'file'},
                { 'name': '.pre-commit-config.yaml',
                  'path': '/tmp/tmp57hgqreb/repo/.pre-commit-config.yaml',
                  'type': 'file'},
                { 'name': '.readthedocs.yaml',
                  'path': '/tmp/tmp57hgqreb/repo/.readthedocs.yaml',
                  'type': 'file'},
                { 'name': 'AUTHORS.rst',
                  'path': '/tmp/tmp57hgqreb/repo/AUTHORS.rst',
                  'type': 'file'},
                { 'name': 'HISTORY.md',
                  'path': '/tmp/tmp57hgqreb/repo/HISTORY.md',
                  'type': 'file'},
                { 'name': 'LICENSE',
                  'path': '/tmp/tmp57hgqreb/repo/LICENSE',
                  'type': 'file'},
                { 'name': 'MANIFEST.in',
                  'path': '/tmp/tmp57hgqreb/repo/MANIFEST.in',
                  'type': 'file'},
                { 'name': 'Makefile',
                  'path': '/tmp/tmp57hgqreb/repo/Makefile',
                  'type': 'file'},
                { 'name': 'NOTICE',
                  'path': '/tmp/tmp57hgqreb/repo/NOTICE',
                  'type': 'file'},
                { 'name': 'README.md',
                  'path': '/tmp/tmp57hgqreb/repo/README.md',
                  'type': 'file'},
                { 'children': [ { 'name': '.nojekyll',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/.nojekyll',
                                  'type': 'file'},
                                { 'name': 'Makefile',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/Makefile',
                                  'type': 'file'},
                                { 'children': [ { 'name': 'custom.css',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/_static/custom.css',
                                                  'type': 'file'},
                                                { 'name': 'requests-sidebar.png',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/_static/requests-sidebar.png',
                                                  'type': 'file'}],
                                  'name': '_static',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/_static',
                                  'type': 'dir'},
                                { 'children': [ { 'name': 'hacks.html',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/_templates/hacks.html',
                                                  'type': 'file'},
                                                { 'name': 'sidebarintro.html',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/_templates/sidebarintro.html',
                                                  'type': 'file'},
                                                { 'name': 'sidebarlogo.html',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/_templates/sidebarlogo.html',
                                                  'type': 'file'}],
                                  'name': '_templates',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/_templates',
                                  'type': 'dir'},
                                { 'children': [ { 'name': '.gitignore',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/_themes/.gitignore',
                                                  'type': 'file'},
                                                { 'name': 'LICENSE',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/_themes/LICENSE',
                                                  'type': 'file'},
                                                { 'name': 'flask_theme_support.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/_themes/flask_theme_support.py',
                                                  'type': 'file'}],
                                  'name': '_themes',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/_themes',
                                  'type': 'dir'},
                                { 'name': 'api.rst',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/api.rst',
                                  'type': 'file'},
                                { 'children': [ { 'name': 'faq.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/community/faq.rst',
                                                  'type': 'file'},
                                                { 'name': 'out-there.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/community/out-there.rst',
                                                  'type': 'file'},
                                                { 'name': 'recommended.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/community/recommended.rst',
                                                  'type': 'file'},
                                                { 'name': 'release-process.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/community/release-process.rst',
                                                  'type': 'file'},
                                                { 'name': 'support.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/community/support.rst',
                                                  'type': 'file'},
                                                { 'name': 'updates.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/community/updates.rst',
                                                  'type': 'file'},
                                                { 'name': 'vulnerabilities.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/community/vulnerabilities.rst',
                                                  'type': 'file'}],
                                  'name': 'community',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/community',
                                  'type': 'dir'},
                                { 'name': 'conf.py',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/conf.py',
                                  'type': 'file'},
                                { 'children': [ { 'name': 'authors.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/dev/authors.rst',
                                                  'type': 'file'},
                                                { 'name': 'contributing.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/dev/contributing.rst',
                                                  'type': 'file'}],
                                  'name': 'dev',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/dev',
                                  'type': 'dir'},
                                { 'name': 'index.rst',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/index.rst',
                                  'type': 'file'},
                                { 'name': 'make.bat',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/make.bat',
                                  'type': 'file'},
                                { 'name': 'requirements.txt',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/requirements.txt',
                                  'type': 'file'},
                                { 'children': [ { 'name': 'advanced.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/user/advanced.rst',
                                                  'type': 'file'},
                                                { 'name': 'authentication.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/user/authentication.rst',
                                                  'type': 'file'},
                                                { 'name': 'install.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/user/install.rst',
                                                  'type': 'file'},
                                                { 'name': 'quickstart.rst',
                                                  'path': '/tmp/tmp57hgqreb/repo/docs/user/quickstart.rst',
                                                  'type': 'file'}],
                                  'name': 'user',
                                  'path': '/tmp/tmp57hgqreb/repo/docs/user',
                                  'type': 'dir'}],
                  'name': 'docs',
                  'path': '/tmp/tmp57hgqreb/repo/docs',
                  'type': 'dir'},
                { 'children': [ { 'name': 'LICENSE',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/LICENSE',
                                  'type': 'file'},
                                { 'name': 'flower-of-life.jpg',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/flower-of-life.jpg',
                                  'type': 'file'},
                                { 'name': 'kr-compressed.png',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/kr-compressed.png',
                                  'type': 'file'},
                                { 'name': 'kr.png',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/kr.png',
                                  'type': 'file'},
                                { 'name': 'psf-compressed.png',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/psf-compressed.png',
                                  'type': 'file'},
                                { 'name': 'psf.png',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/psf.png',
                                  'type': 'file'},
                                { 'name': 'requests-logo-compressed.png',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/requests-logo-compressed.png',
                                  'type': 'file'},
                                { 'name': 'requests-logo.ai',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/requests-logo.ai',
                                  'type': 'file'},
                                { 'name': 'requests-logo.png',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/requests-logo.png',
                                  'type': 'file'},
                                { 'name': 'requests-logo.svg',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/requests-logo.svg',
                                  'type': 'file'},
                                { 'name': 'ss-compressed.png',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/ss-compressed.png',
                                  'type': 'file'},
                                { 'name': 'ss.png',
                                  'path': '/tmp/tmp57hgqreb/repo/ext/ss.png',
                                  'type': 'file'}],
                  'name': 'ext',
                  'path': '/tmp/tmp57hgqreb/repo/ext',
                  'type': 'dir'},
                { 'name': 'pyproject.toml',
                  'path': '/tmp/tmp57hgqreb/repo/pyproject.toml',
                  'type': 'file'},
                { 'name': 'requirements-dev.txt',
                  'path': '/tmp/tmp57hgqreb/repo/requirements-dev.txt',
                  'type': 'file'},
                { 'name': 'setup.cfg',
                  'path': '/tmp/tmp57hgqreb/repo/setup.cfg',
                  'type': 'file'},
                { 'name': 'setup.py',
                  'path': '/tmp/tmp57hgqreb/repo/setup.py',
                  'type': 'file'},
                { 'children': [ { 'children': [ { 'name': '__init__.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/__init__.py',
                                                  'type': 'file'},
                                                { 'name': '__version__.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/__version__.py',
                                                  'type': 'file'},
                                                { 'name': '_internal_utils.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/_internal_utils.py',
                                                  'type': 'file'},
                                                { 'name': 'adapters.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/adapters.py',
                                                  'type': 'file'},
                                                { 'name': 'api.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/api.py',
                                                  'type': 'file'},
                                                { 'name': 'auth.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/auth.py',
                                                  'type': 'file'},
                                                { 'name': 'certs.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/certs.py',
                                                  'type': 'file'},
                                                { 'name': 'compat.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/compat.py',
                                                  'type': 'file'},
                                                { 'name': 'cookies.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/cookies.py',
                                                  'type': 'file'},
                                                { 'name': 'exceptions.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/exceptions.py',
                                                  'type': 'file'},
                                                { 'name': 'help.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/help.py',
                                                  'type': 'file'},
                                                { 'name': 'hooks.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/hooks.py',
                                                  'type': 'file'},
                                                { 'name': 'models.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/models.py',
                                                  'type': 'file'},
                                                { 'name': 'packages.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/packages.py',
                                                  'type': 'file'},
                                                { 'name': 'sessions.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/sessions.py',
                                                  'type': 'file'},
                                                { 'name': 'status_codes.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/status_codes.py',
                                                  'type': 'file'},
                                                { 'name': 'structures.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/structures.py',
                                                  'type': 'file'},
                                                { 'name': 'utils.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/src/requests/utils.py',
                                                  'type': 'file'}],
                                  'name': 'requests',
                                  'path': '/tmp/tmp57hgqreb/repo/src/requests',
                                  'type': 'dir'}],
                  'name': 'src',
                  'path': '/tmp/tmp57hgqreb/repo/src',
                  'type': 'dir'},
                { 'children': [ { 'name': '__init__.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/__init__.py',
                                  'type': 'file'},
                                { 'children': [ { 'name': 'README.md',
                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/README.md',
                                                  'type': 'file'},
                                                { 'children': [ { 'name': 'Makefile',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/Makefile',
                                                                  'type': 'file'},
                                                                { 'name': 'README.md',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/README.md',
                                                                  'type': 'file'},
                                                                { 'children': [ { 'name': 'Makefile',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/ca/Makefile',
                                                                                  'type': 'file'},
                                                                                { 'name': 'ca-private.key',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/ca/ca-private.key',
                                                                                  'type': 'file'},
                                                                                { 'name': 'ca.cnf',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/ca/ca.cnf',
                                                                                  'type': 'file'},
                                                                                { 'name': 'ca.crt',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/ca/ca.crt',
                                                                                  'type': 'file'},
                                                                                { 'name': 'ca.srl',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/ca/ca.srl',
                                                                                  'type': 'file'}],
                                                                  'name': 'ca',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/ca',
                                                                  'type': 'dir'},
                                                                { 'children': [ { 'name': 'Makefile',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/server/Makefile',
                                                                                  'type': 'file'},
                                                                                { 'name': 'cert.cnf',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/server/cert.cnf',
                                                                                  'type': 'file'},
                                                                                { 'name': 'server.csr',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/server/server.csr',
                                                                                  'type': 'file'},
                                                                                { 'name': 'server.key',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/server/server.key',
                                                                                  'type': 'file'},
                                                                                { 'name': 'server.pem',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/server/server.pem',
                                                                                  'type': 'file'}],
                                                                  'name': 'server',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired/server',
                                                                  'type': 'dir'}],
                                                  'name': 'expired',
                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/expired',
                                                  'type': 'dir'},
                                                { 'children': [ { 'name': 'Makefile',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/Makefile',
                                                                  'type': 'file'},
                                                                { 'name': 'README.md',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/README.md',
                                                                  'type': 'file'},
                                                                { 'children': [ { 'name': 'Makefile',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/Makefile',
                                                                                  'type': 'file'},
                                                                                { 'children': [ { 'name': 'Makefile',
                                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/ca/Makefile',
                                                                                                  'type': 'file'},
                                                                                                { 'name': 'ca-private.key',
                                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/ca/ca-private.key',
                                                                                                  'type': 'file'},
                                                                                                { 'name': 'ca.cnf',
                                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/ca/ca.cnf',
                                                                                                  'type': 'file'},
                                                                                                { 'name': 'ca.crt',
                                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/ca/ca.crt',
                                                                                                  'type': 'file'},
                                                                                                { 'name': 'ca.srl',
                                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/ca/ca.srl',
                                                                                                  'type': 'file'}],
                                                                                  'name': 'ca',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/ca',
                                                                                  'type': 'dir'},
                                                                                { 'name': 'cert.cnf',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/cert.cnf',
                                                                                  'type': 'file'},
                                                                                { 'name': 'client.csr',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/client.csr',
                                                                                  'type': 'file'},
                                                                                { 'name': 'client.key',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/client.key',
                                                                                  'type': 'file'},
                                                                                { 'name': 'client.pem',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client/client.pem',
                                                                                  'type': 'file'}],
                                                                  'name': 'client',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls/client',
                                                                  'type': 'dir'}],
                                                  'name': 'mtls',
                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/mtls',
                                                  'type': 'dir'},
                                                { 'children': [ { 'children': [ { 'name': 'Makefile',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/ca/Makefile',
                                                                                  'type': 'file'},
                                                                                { 'name': 'ca-private.key',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/ca/ca-private.key',
                                                                                  'type': 'file'},
                                                                                { 'name': 'ca.cnf',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/ca/ca.cnf',
                                                                                  'type': 'file'},
                                                                                { 'name': 'ca.crt',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/ca/ca.crt',
                                                                                  'type': 'file'},
                                                                                { 'name': 'ca.srl',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/ca/ca.srl',
                                                                                  'type': 'file'}],
                                                                  'name': 'ca',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/ca',
                                                                  'type': 'dir'},
                                                                { 'children': [ { 'name': 'Makefile',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/server/Makefile',
                                                                                  'type': 'file'},
                                                                                { 'name': 'cert.cnf',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/server/cert.cnf',
                                                                                  'type': 'file'},
                                                                                { 'name': 'server.csr',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/server/server.csr',
                                                                                  'type': 'file'},
                                                                                { 'name': 'server.key',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/server/server.key',
                                                                                  'type': 'file'},
                                                                                { 'name': 'server.pem',
                                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/server/server.pem',
                                                                                  'type': 'file'}],
                                                                  'name': 'server',
                                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid/server',
                                                                  'type': 'dir'}],
                                                  'name': 'valid',
                                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs/valid',
                                                  'type': 'dir'}],
                                  'name': 'certs',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/certs',
                                  'type': 'dir'},
                                { 'name': 'compat.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/compat.py',
                                  'type': 'file'},
                                { 'name': 'conftest.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/conftest.py',
                                  'type': 'file'},
                                { 'name': 'test_adapters.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_adapters.py',
                                  'type': 'file'},
                                { 'name': 'test_help.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_help.py',
                                  'type': 'file'},
                                { 'name': 'test_hooks.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_hooks.py',
                                  'type': 'file'},
                                { 'name': 'test_lowlevel.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_lowlevel.py',
                                  'type': 'file'},
                                { 'name': 'test_packages.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_packages.py',
                                  'type': 'file'},
                                { 'name': 'test_requests.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_requests.py',
                                  'type': 'file'},
                                { 'name': 'test_structures.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_structures.py',
                                  'type': 'file'},
                                { 'name': 'test_testserver.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_testserver.py',
                                  'type': 'file'},
                                { 'name': 'test_utils.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/test_utils.py',
                                  'type': 'file'},
                                { 'children': [ { 'name': '__init__.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/tests/testserver/__init__.py',
                                                  'type': 'file'},
                                                { 'name': 'server.py',
                                                  'path': '/tmp/tmp57hgqreb/repo/tests/testserver/server.py',
                                                  'type': 'file'}],
                                  'name': 'testserver',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/testserver',
                                  'type': 'dir'},
                                { 'name': 'utils.py',
                                  'path': '/tmp/tmp57hgqreb/repo/tests/utils.py',
                                  'type': 'file'}],
                  'name': 'tests',
                  'path': '/tmp/tmp57hgqreb/repo/tests',
                  'type': 'dir'},
                { 'name': 'tox.ini',
                  'path': '/tmp/tmp57hgqreb/repo/tox.ini',
                  'type': 'file'}],
  'name': 'repo',
  'path': '/tmp/tmp57hgqreb/repo',
  'type': 'dir'}
```

## 🕸️ Code Context Graph

![Code Context Graph](outputs/repo/ccg_diagram.png)


## 🧩 Classes and Functions

### `setup.py`

### `docs/conf.py`

### `docs/_themes/flask_theme_support.py`

- **Class** `FlaskyStyle`

### `src/requests/adapters.py`

> requests.adapters
~~~~~~~~~~~~~~~~~

This module contains the transport adapters that Requests uses to define
and maintain connections.


- **Class** `BaseAdapter`

  - Doc: The Base Transport Adapter

  - Method: `__init__`

  - Method: `send`

  - Method: `close`

- **Class** `HTTPAdapter`

  - Doc: The built-in HTTP Adapter for urllib3.

Provides a general-case interface for Requests sessions to contact HTTP and
HTTPS urls by implementing the Transport Adapter interface. This class will
usually be created by the :class:`Session <Session>` class under the
covers.

:param pool_connections: The number of urllib3 connection pools to cache.
:param pool_maxsize: The maximum number of connections to save in the pool.
:param max_retries: The maximum number of retries each connection
    should attempt. Note, this applies only to failed DNS lookups, socket
    connections and connection timeouts, never to requests where data has
    made it to the server. By default, Requests does not retry failed
    connections. If you need granular control over the conditions under
    which we retry a request, import urllib3's ``Retry`` class and pass
    that instead.
:param pool_block: Whether the connection pool should block for connections.

Usage::

  >>> import requests
  >>> s = requests.Session()
  >>> a = requests.adapters.HTTPAdapter(max_retries=3)
  >>> s.mount('http://', a)

  - Method: `__init__`

  - Method: `__getstate__`

  - Method: `__setstate__`

  - Method: `init_poolmanager`

  - Method: `proxy_manager_for`

  - Method: `cert_verify`

  - Method: `build_response`

  - Method: `build_connection_pool_key_attributes`

  - Method: `get_connection_with_tls_context`

  - Method: `get_connection`

  - Method: `close`

  - Method: `request_url`

  - Method: `add_headers`

  - Method: `proxy_headers`

  - Method: `send`

- **Function** `_urllib3_request_context`

### `src/requests/certs.py`

> requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.


### `src/requests/models.py`

> requests.models
~~~~~~~~~~~~~~~

This module contains the primary objects that power Requests.


- **Class** `RequestEncodingMixin`

  - Method: `path_url`

  - Method: `_encode_params`

  - Method: `_encode_files`

- **Class** `RequestHooksMixin`

  - Method: `register_hook`

  - Method: `deregister_hook`

- **Class** `Request`

  - Doc: A user-created :class:`Request <Request>` object.

Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

:param method: HTTP method to use.
:param url: URL to send.
:param headers: dictionary of headers to send.
:param files: dictionary of {filename: fileobject} files to multipart upload.
:param data: the body to attach to the request. If a dictionary or
    list of tuples ``[(key, value)]`` is provided, form-encoding will
    take place.
:param json: json for the body to attach to the request (if files or data is not specified).
:param params: URL parameters to append to the URL. If a dictionary or
    list of tuples ``[(key, value)]`` is provided, form-encoding will
    take place.
:param auth: Auth handler or (user, pass) tuple.
:param cookies: dictionary or CookieJar of cookies to attach to this request.
:param hooks: dictionary of callback hooks, for internal usage.

Usage::

  >>> import requests
  >>> req = requests.Request('GET', 'https://httpbin.org/get')
  >>> req.prepare()
  <PreparedRequest [GET]>

  - Method: `__init__`

  - Method: `__repr__`

  - Method: `prepare`

- **Class** `PreparedRequest`

  - Doc: The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
containing the exact bytes that will be sent to the server.

Instances are generated from a :class:`Request <Request>` object, and
should not be instantiated manually; doing so may produce undesirable
effects.

Usage::

  >>> import requests
  >>> req = requests.Request('GET', 'https://httpbin.org/get')
  >>> r = req.prepare()
  >>> r
  <PreparedRequest [GET]>

  >>> s = requests.Session()
  >>> s.send(r)
  <Response [200]>

  - Method: `__init__`

  - Method: `prepare`

  - Method: `__repr__`

  - Method: `copy`

  - Method: `prepare_method`

  - Method: `_get_idna_encoded_host`

  - Method: `prepare_url`

  - Method: `prepare_headers`

  - Method: `prepare_body`

  - Method: `prepare_content_length`

  - Method: `prepare_auth`

  - Method: `prepare_cookies`

  - Method: `prepare_hooks`

- **Class** `Response`

  - Doc: The :class:`Response <Response>` object, which contains a
server's response to an HTTP request.

  - Method: `__init__`

  - Method: `__enter__`

  - Method: `__exit__`

  - Method: `__getstate__`

  - Method: `__setstate__`

  - Method: `__repr__`

  - Method: `__bool__`

  - Method: `__nonzero__`

  - Method: `__iter__`

  - Method: `ok`

  - Method: `is_redirect`

  - Method: `is_permanent_redirect`

  - Method: `next`

  - Method: `apparent_encoding`

  - Method: `iter_content`

  - Method: `iter_lines`

  - Method: `content`

  - Method: `text`

  - Method: `json`

  - Method: `links`

  - Method: `raise_for_status`

  - Method: `close`

### `src/requests/structures.py`

> requests.structures
~~~~~~~~~~~~~~~~~~~

Data structures that power Requests.


- **Class** `CaseInsensitiveDict`

  - Doc: A case-insensitive ``dict``-like object.

Implements all methods and operations of
``MutableMapping`` as well as dict's ``copy``. Also
provides ``lower_items``.

All keys are expected to be strings. The structure remembers the
case of the last key to be set, and ``iter(instance)``,
``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
will contain case-sensitive keys. However, querying and contains
testing is case insensitive::

    cid = CaseInsensitiveDict()
    cid['Accept'] = 'application/json'
    cid['aCCEPT'] == 'application/json'  # True
    list(cid) == ['Accept']  # True

For example, ``headers['content-encoding']`` will return the
value of a ``'Content-Encoding'`` response header, regardless
of how the header name was originally stored.

If the constructor, ``.update``, or equality comparison
operations are given keys that have equal ``.lower()``s, the
behavior is undefined.

  - Method: `__init__`

  - Method: `__setitem__`

  - Method: `__getitem__`

  - Method: `__delitem__`

  - Method: `__iter__`

  - Method: `__len__`

  - Method: `lower_items`

  - Method: `__eq__`

  - Method: `copy`

  - Method: `__repr__`

- **Class** `LookupDict`

  - Doc: Dictionary lookup object.

  - Method: `__init__`

  - Method: `__repr__`

  - Method: `__getitem__`

  - Method: `get`

### `src/requests/status_codes.py`

> The ``codes`` object defines a mapping from common names for HTTP statuses
to their numerical codes, accessible either as attributes or as dictionary
items.

Example::

    >>> import requests
    >>> requests.codes['temporary_redirect']
    307
    >>> requests.codes.teapot
    418
    >>> requests.codes['\o/']
    200

Some codes have multiple names, and both upper- and lower-case versions of
the names are allowed. For example, ``codes.ok``, ``codes.OK``, and
``codes.okay`` all correspond to the HTTP status code 200.


- **Function** `_init`

### `src/requests/help.py`

> Module containing bug report helper(s).


- **Function** `_implementation`

  - Doc: Return a dict with the Python implementation and version.

Provide both the name and the version of the Python implementation
currently running. For example, on CPython 3.10.3 it will return
{'name': 'CPython', 'version': '3.10.3'}.

This function works best on CPython and PyPy: in particular, it probably
doesn't work for Jython or IronPython. Future investigation should be done
to work out the correct shape of the code for those platforms.

- **Function** `info`

  - Doc: Generate information for a bug report.

- **Function** `main`

  - Doc: Pretty-print the bug information as JSON.

### `src/requests/hooks.py`

> requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.


- **Function** `default_hooks`

- **Function** `dispatch_hook`

  - Doc: Dispatches a hook dictionary on a given piece of data.

### `src/requests/compat.py`

> requests.compat
~~~~~~~~~~~~~~~

This module previously handled import compatibility issues
between Python 2 and Python 3. It remains for backwards
compatibility until the next major version.


- **Function** `_resolve_char_detection`

  - Doc: Find supported character detection libraries.

### `src/requests/api.py`

> requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.


- **Function** `request`

  - Doc: Constructs and sends a :class:`Request <Request>`.

:param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
:param url: URL for the new :class:`Request` object.
:param params: (optional) Dictionary, list of tuples or bytes to send
    in the query string for the :class:`Request`.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
:param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
:param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
    ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
    or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
    defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
    to add for the file.
:param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
:param timeout: (optional) How many seconds to wait for the server to send data
    before giving up, as a float, or a :ref:`(connect timeout, read
    timeout) <timeouts>` tuple.
:type timeout: float or tuple
:param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
:type allow_redirects: bool
:param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
:param verify: (optional) Either a boolean, in which case it controls whether we verify
        the server's TLS certificate, or a string, in which case it must be a path
        to a CA bundle to use. Defaults to ``True``.
:param stream: (optional) if ``False``, the response content will be immediately downloaded.
:param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
:return: :class:`Response <Response>` object
:rtype: requests.Response

Usage::

  >>> import requests
  >>> req = requests.request('GET', 'https://httpbin.org/get')
  >>> req
  <Response [200]>

- **Function** `get`

  - Doc: Sends a GET request.

:param url: URL for the new :class:`Request` object.
:param params: (optional) Dictionary, list of tuples or bytes to send
    in the query string for the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

- **Function** `options`

  - Doc: Sends an OPTIONS request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

- **Function** `head`

  - Doc: Sends a HEAD request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes. If
    `allow_redirects` is not provided, it will be set to `False` (as
    opposed to the default :meth:`request` behavior).
:return: :class:`Response <Response>` object
:rtype: requests.Response

- **Function** `post`

  - Doc: Sends a POST request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

- **Function** `put`

  - Doc: Sends a PUT request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

- **Function** `patch`

  - Doc: Sends a PATCH request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

- **Function** `delete`

  - Doc: Sends a DELETE request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

### `src/requests/exceptions.py`

> requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.


- **Class** `RequestException`

  - Doc: There was an ambiguous exception that occurred while handling your
request.

  - Method: `__init__`

- **Class** `InvalidJSONError`

  - Doc: A JSON error occurred.

- **Class** `JSONDecodeError`

  - Doc: Couldn't decode the text into json

  - Method: `__init__`

  - Method: `__reduce__`

- **Class** `HTTPError`

  - Doc: An HTTP error occurred.

- **Class** `ConnectionError`

  - Doc: A Connection error occurred.

- **Class** `ProxyError`

  - Doc: A proxy error occurred.

- **Class** `SSLError`

  - Doc: An SSL error occurred.

- **Class** `Timeout`

  - Doc: The request timed out.

Catching this error will catch both
:exc:`~requests.exceptions.ConnectTimeout` and
:exc:`~requests.exceptions.ReadTimeout` errors.

- **Class** `ConnectTimeout`

  - Doc: The request timed out while trying to connect to the remote server.

Requests that produced this error are safe to retry.

- **Class** `ReadTimeout`

  - Doc: The server did not send any data in the allotted amount of time.

- **Class** `URLRequired`

  - Doc: A valid URL is required to make a request.

- **Class** `TooManyRedirects`

  - Doc: Too many redirects.

- **Class** `MissingSchema`

  - Doc: The URL scheme (e.g. http or https) is missing.

- **Class** `InvalidSchema`

  - Doc: The URL scheme provided is either invalid or unsupported.

- **Class** `InvalidURL`

  - Doc: The URL provided was somehow invalid.

- **Class** `InvalidHeader`

  - Doc: The header value provided was somehow invalid.

- **Class** `InvalidProxyURL`

  - Doc: The proxy URL provided is invalid.

- **Class** `ChunkedEncodingError`

  - Doc: The server declared chunked encoding but sent an invalid chunk.

- **Class** `ContentDecodingError`

  - Doc: Failed to decode response content.

- **Class** `StreamConsumedError`

  - Doc: The content for this response was already consumed.

- **Class** `RetryError`

  - Doc: Custom retries logic failed

- **Class** `UnrewindableBodyError`

  - Doc: Requests encountered an error when trying to rewind a body.

- **Class** `RequestsWarning`

  - Doc: Base warning for Requests.

- **Class** `FileModeWarning`

  - Doc: A file was opened in text mode, but Requests determined its binary length.

- **Class** `RequestsDependencyWarning`

  - Doc: An imported dependency doesn't match the expected version range.

### `src/requests/auth.py`

> requests.auth
~~~~~~~~~~~~~

This module contains the authentication handlers for Requests.


- **Class** `AuthBase`

  - Doc: Base class that all auth implementations derive from

  - Method: `__call__`

- **Class** `HTTPBasicAuth`

  - Doc: Attaches HTTP Basic Authentication to the given Request object.

  - Method: `__init__`

  - Method: `__eq__`

  - Method: `__ne__`

  - Method: `__call__`

- **Class** `HTTPProxyAuth`

  - Doc: Attaches HTTP Proxy Authentication to a given Request object.

  - Method: `__call__`

- **Class** `HTTPDigestAuth`

  - Doc: Attaches HTTP Digest Authentication to the given Request object.

  - Method: `__init__`

  - Method: `init_per_thread_state`

  - Method: `build_digest_header`

  - Method: `handle_redirect`

  - Method: `handle_401`

  - Method: `__call__`

  - Method: `__eq__`

  - Method: `__ne__`

- **Function** `_basic_auth_str`

  - Doc: Returns a Basic Auth string.

### `src/requests/cookies.py`

> requests.cookies
~~~~~~~~~~~~~~~~

Compatibility code to be able to use `http.cookiejar.CookieJar` with requests.

requests.utils imports from here, so be careful with imports.


- **Class** `MockRequest`

  - Doc: Wraps a `requests.Request` to mimic a `urllib2.Request`.

The code in `http.cookiejar.CookieJar` expects this interface in order to correctly
manage cookie policies, i.e., determine whether a cookie can be set, given the
domains of the request and the cookie.

The original request object is read-only. The client is responsible for collecting
the new headers via `get_new_headers()` and interpreting them appropriately. You
probably want `get_cookie_header`, defined below.

  - Method: `__init__`

  - Method: `get_type`

  - Method: `get_host`

  - Method: `get_origin_req_host`

  - Method: `get_full_url`

  - Method: `is_unverifiable`

  - Method: `has_header`

  - Method: `get_header`

  - Method: `add_header`

  - Method: `add_unredirected_header`

  - Method: `get_new_headers`

  - Method: `unverifiable`

  - Method: `origin_req_host`

  - Method: `host`

- **Class** `MockResponse`

  - Doc: Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.

...what? Basically, expose the parsed HTTP headers from the server response
the way `http.cookiejar` expects to see them.

  - Method: `__init__`

  - Method: `info`

  - Method: `getheaders`

- **Class** `CookieConflictError`

  - Doc: There are two cookies that meet the criteria specified in the cookie jar.
Use .get and .set and include domain and path args in order to be more specific.

- **Class** `RequestsCookieJar`

  - Doc: Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict
interface.

This is the CookieJar we create by default for requests and sessions that
don't specify one, since some clients may expect response.cookies and
session.cookies to support dict operations.

Requests does not use the dict interface internally; it's just for
compatibility with external client code. All requests code should work
out of the box with externally provided instances of ``CookieJar``, e.g.
``LWPCookieJar`` and ``FileCookieJar``.

Unlike a regular CookieJar, this class is pickleable.

.. warning:: dictionary operations that are normally O(1) may be O(n).

  - Method: `get`

  - Method: `set`

  - Method: `iterkeys`

  - Method: `keys`

  - Method: `itervalues`

  - Method: `values`

  - Method: `iteritems`

  - Method: `items`

  - Method: `list_domains`

  - Method: `list_paths`

  - Method: `multiple_domains`

  - Method: `get_dict`

  - Method: `__contains__`

  - Method: `__getitem__`

  - Method: `__setitem__`

  - Method: `__delitem__`

  - Method: `set_cookie`

  - Method: `update`

  - Method: `_find`

  - Method: `_find_no_duplicates`

  - Method: `__getstate__`

  - Method: `__setstate__`

  - Method: `copy`

  - Method: `get_policy`

- **Function** `extract_cookies_to_jar`

  - Doc: Extract the cookies from the response into a CookieJar.

:param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)
:param request: our own requests.Request object
:param response: urllib3.HTTPResponse object

- **Function** `get_cookie_header`

  - Doc: Produce an appropriate Cookie header string to be sent with `request`, or None.

:rtype: str

- **Function** `remove_cookie_by_name`

  - Doc: Unsets a cookie by name, by default over all domains and paths.

Wraps CookieJar.clear(), is O(n).

- **Function** `_copy_cookie_jar`

- **Function** `create_cookie`

  - Doc: Make a cookie from underspecified parameters.

By default, the pair of `name` and `value` will be set for the domain ''
and sent on every request (this is sometimes called a "supercookie").

- **Function** `morsel_to_cookie`

  - Doc: Convert a Morsel object into a Cookie containing the one k/v pair.

- **Function** `cookiejar_from_dict`

  - Doc: Returns a CookieJar from a key/value dictionary.

:param cookie_dict: Dict of key/values to insert into CookieJar.
:param cookiejar: (optional) A cookiejar to add the cookies to.
:param overwrite: (optional) If False, will not replace cookies
    already in the jar with new ones.
:rtype: CookieJar

- **Function** `merge_cookies`

  - Doc: Add cookies to cookiejar and returns a merged CookieJar.

:param cookiejar: CookieJar object to add the cookies to.
:param cookies: Dictionary or CookieJar object to be added.
:rtype: CookieJar

### `src/requests/_internal_utils.py`

> requests._internal_utils
~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by Requests
which depend on extremely few external helpers (such as compat)


- **Function** `to_native_string`

  - Doc: Given a string object, regardless of type, returns a representation of
that string in the native string type, encoding and decoding where
necessary. This assumes ASCII unless told otherwise.

- **Function** `unicode_is_ascii`

  - Doc: Determine if unicode string only contains ASCII characters.

:param str u_string: unicode string to check. Must be unicode
    and not Python 2 `str`.
:rtype: bool

### `src/requests/packages.py`

### `src/requests/sessions.py`

> requests.sessions
~~~~~~~~~~~~~~~~~

This module provides a Session object to manage and persist settings across
requests (cookies, auth, proxies).


- **Class** `SessionRedirectMixin`

  - Method: `get_redirect_target`

  - Method: `should_strip_auth`

  - Method: `resolve_redirects`

  - Method: `rebuild_auth`

  - Method: `rebuild_proxies`

  - Method: `rebuild_method`

- **Class** `Session`

  - Doc: A Requests session.

Provides cookie persistence, connection-pooling, and configuration.

Basic Usage::

  >>> import requests
  >>> s = requests.Session()
  >>> s.get('https://httpbin.org/get')
  <Response [200]>

Or as a context manager::

  >>> with requests.Session() as s:
  ...     s.get('https://httpbin.org/get')
  <Response [200]>

  - Method: `__init__`

  - Method: `__enter__`

  - Method: `__exit__`

  - Method: `prepare_request`

  - Method: `request`

  - Method: `get`

  - Method: `options`

  - Method: `head`

  - Method: `post`

  - Method: `put`

  - Method: `patch`

  - Method: `delete`

  - Method: `send`

  - Method: `merge_environment_settings`

  - Method: `get_adapter`

  - Method: `close`

  - Method: `mount`

  - Method: `__getstate__`

  - Method: `__setstate__`

- **Function** `merge_setting`

  - Doc: Determines appropriate setting for a given request, taking into account
the explicit setting on that request, and the setting in the session. If a
setting is a dictionary, they will be merged together using `dict_class`

- **Function** `merge_hooks`

  - Doc: Properly merges both requests and session hooks.

This is necessary because when request_hooks == {'response': []}, the
merge breaks Session hooks entirely.

- **Function** `session`

  - Doc: Returns a :class:`Session` for context-management.

.. deprecated:: 1.0.0

    This method has been deprecated since version 1.0.0 and is only kept for
    backwards compatibility. New code should use :class:`~requests.sessions.Session`
    to create a session. This may be removed at a future date.

:rtype: Session

### `src/requests/__init__.py`

> Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.


- **Function** `check_compatibility`

- **Function** `_check_cryptography`

### `src/requests/__version__.py`

### `src/requests/utils.py`

> requests.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within Requests
that are also useful for external consumption.


- **Function** `dict_to_sequence`

  - Doc: Returns an internal sequence dictionary update.

- **Function** `super_len`

- **Function** `get_netrc_auth`

  - Doc: Returns the Requests tuple auth for a given url from netrc.

- **Function** `guess_filename`

  - Doc: Tries to guess the filename of the given object.

- **Function** `extract_zipped_paths`

  - Doc: Replace nonexistent paths that look like they refer to a member of a zip
archive with the location of an extracted copy of the target, or else
just return the provided path unchanged.

- **Function** `atomic_open`

  - Doc: Write a file to the disk in an atomic fashion

- **Function** `from_key_val_list`

  - Doc: Take an object and test to see if it can be represented as a
dictionary. Unless it can not be represented as such, return an
OrderedDict, e.g.,

::

    >>> from_key_val_list([('key', 'val')])
    OrderedDict([('key', 'val')])
    >>> from_key_val_list('string')
    Traceback (most recent call last):
    ...
    ValueError: cannot encode objects that are not 2-tuples
    >>> from_key_val_list({'key': 'val'})
    OrderedDict([('key', 'val')])

:rtype: OrderedDict

- **Function** `to_key_val_list`

  - Doc: Take an object and test to see if it can be represented as a
dictionary. If it can be, return a list of tuples, e.g.,

::

    >>> to_key_val_list([('key', 'val')])
    [('key', 'val')]
    >>> to_key_val_list({'key': 'val'})
    [('key', 'val')]
    >>> to_key_val_list('string')
    Traceback (most recent call last):
    ...
    ValueError: cannot encode objects that are not 2-tuples

:rtype: list

- **Function** `parse_list_header`

  - Doc: Parse lists as described by RFC 2068 Section 2.

In particular, parse comma-separated lists where the elements of
the list may include quoted-strings.  A quoted-string could
contain a comma.  A non-quoted string could have quotes in the
middle.  Quotes are removed automatically after parsing.

It basically works like :func:`parse_set_header` just that items
may appear multiple times and case sensitivity is preserved.

The return value is a standard :class:`list`:

>>> parse_list_header('token, "quoted value"')
['token', 'quoted value']

To create a header from the :class:`list` again, use the
:func:`dump_header` function.

:param value: a string with a list header.
:return: :class:`list`
:rtype: list

- **Function** `parse_dict_header`

  - Doc: Parse lists of key, value pairs as described by RFC 2068 Section 2 and
convert them into a python dict:

>>> d = parse_dict_header('foo="is a fish", bar="as well"')
>>> type(d) is dict
True
>>> sorted(d.items())
[('bar', 'as well'), ('foo', 'is a fish')]

If there is no value for a key it will be `None`:

>>> parse_dict_header('key_without_value')
{'key_without_value': None}

To create a header from the :class:`dict` again, use the
:func:`dump_header` function.

:param value: a string with a dict header.
:return: :class:`dict`
:rtype: dict

- **Function** `unquote_header_value`

  - Doc: Unquotes a header value.  (Reversal of :func:`quote_header_value`).
This does not use the real unquoting but what browsers are actually
using for quoting.

:param value: the header value to unquote.
:rtype: str

- **Function** `dict_from_cookiejar`

  - Doc: Returns a key/value dictionary from a CookieJar.

:param cj: CookieJar object to extract cookies from.
:rtype: dict

- **Function** `add_dict_to_cookiejar`

  - Doc: Returns a CookieJar from a key/value dictionary.

:param cj: CookieJar to insert cookies into.
:param cookie_dict: Dict of key/values to insert into CookieJar.
:rtype: CookieJar

- **Function** `get_encodings_from_content`

  - Doc: Returns encodings from given content string.

:param content: bytestring to extract encodings from.

- **Function** `_parse_content_type_header`

  - Doc: Returns content type and parameters from given header

:param header: string
:return: tuple containing content type and dictionary of
     parameters

- **Function** `get_encoding_from_headers`

  - Doc: Returns encodings from given HTTP Header Dict.

:param headers: dictionary to extract encoding from.
:rtype: str

- **Function** `stream_decode_response_unicode`

  - Doc: Stream decodes an iterator.

- **Function** `iter_slices`

  - Doc: Iterate over slices of a string.

- **Function** `get_unicode_from_response`

  - Doc: Returns the requested content back in unicode.

:param r: Response object to get unicode content from.

Tried:

1. charset from content-type
2. fall back and replace all unicode characters

:rtype: str

- **Function** `unquote_unreserved`

  - Doc: Un-escape any percent-escape sequences in a URI that are unreserved
characters. This leaves all reserved, illegal and non-ASCII bytes encoded.

:rtype: str

- **Function** `requote_uri`

  - Doc: Re-quote the given URI.

This function passes the given URI through an unquote/quote cycle to
ensure that it is fully and consistently quoted.

:rtype: str

- **Function** `address_in_network`

  - Doc: This function allows you to check if an IP belongs to a network subnet

Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
         returns False if ip = 192.168.1.1 and net = 192.168.100.0/24

:rtype: bool

- **Function** `dotted_netmask`

  - Doc: Converts mask from /xx format to xxx.xxx.xxx.xxx

Example: if mask is 24 function returns 255.255.255.0

:rtype: str

- **Function** `is_ipv4_address`

  - Doc: :rtype: bool

- **Function** `is_valid_cidr`

  - Doc: Very simple check of the cidr format in no_proxy variable.

:rtype: bool

- **Function** `set_environ`

  - Doc: Set the environment variable 'env_name' to 'value'

Save previous value, yield, and then restore the previous value stored in
the environment variable 'env_name'.

If 'value' is None, do nothing

- **Function** `should_bypass_proxies`

  - Doc: Returns whether we should bypass proxies or not.

:rtype: bool

- **Function** `get_environ_proxies`

  - Doc: Return a dict of environment proxies.

:rtype: dict

- **Function** `select_proxy`

  - Doc: Select a proxy for the url, if applicable.

:param url: The url being for the request
:param proxies: A dictionary of schemes or schemes and hosts to proxy URLs

- **Function** `resolve_proxies`

  - Doc: This method takes proxy information from a request and configuration
input to resolve a mapping of target proxies. This will consider settings
such as NO_PROXY to strip proxy configurations.

:param request: Request or PreparedRequest
:param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
:param trust_env: Boolean declaring whether to trust environment configs

:rtype: dict

- **Function** `default_user_agent`

  - Doc: Return a string representing the default user agent.

:rtype: str

- **Function** `default_headers`

  - Doc: :rtype: requests.structures.CaseInsensitiveDict

- **Function** `parse_header_links`

  - Doc: Return a list of parsed link headers proxies.

i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"

:rtype: list

- **Function** `guess_json_utf`

  - Doc: :rtype: str

- **Function** `prepend_scheme_if_needed`

  - Doc: Given a URL that may or may not have a scheme, prepend the given scheme.
Does not replace a present scheme with the one provided as an argument.

:rtype: str

- **Function** `get_auth_from_url`

  - Doc: Given a url with authentication components, extract them into a tuple of
username,password.

:rtype: (str,str)

- **Function** `check_header_validity`

  - Doc: Verifies that header parts don't contain leading whitespace
reserved characters, or return characters.

:param header: tuple, in the format (name, value).

- **Function** `_validate_header_part`

- **Function** `urldefragauth`

  - Doc: Given a url remove the fragment and the authentication part.

:rtype: str

- **Function** `rewind_body`

  - Doc: Move file pointer back to its recorded starting position
so it can be read again on redirect.

### `tests/test_requests.py`

> Tests for Requests.


- **Class** `TestRequests`

  - Method: `test_entry_points`

  - Method: `test_invalid_url`

  - Method: `test_basic_building`

  - Method: `test_no_content_length`

  - Method: `test_no_body_content_length`

  - Method: `test_empty_content_length`

  - Method: `test_override_content_length`

  - Method: `test_path_is_not_double_encoded`

  - Method: `test_params_are_added_before_fragment`

  - Method: `test_params_original_order_is_preserved_by_default`

  - Method: `test_params_bytes_are_encoded`

  - Method: `test_binary_put`

  - Method: `test_whitespaces_are_removed_from_url`

  - Method: `test_mixed_case_scheme_acceptable`

  - Method: `test_HTTP_200_OK_GET_ALTERNATIVE`

  - Method: `test_HTTP_302_ALLOW_REDIRECT_GET`

  - Method: `test_HTTP_307_ALLOW_REDIRECT_POST`

  - Method: `test_HTTP_307_ALLOW_REDIRECT_POST_WITH_SEEKABLE`

  - Method: `test_HTTP_302_TOO_MANY_REDIRECTS`

  - Method: `test_HTTP_302_TOO_MANY_REDIRECTS_WITH_PARAMS`

  - Method: `test_http_301_changes_post_to_get`

  - Method: `test_http_301_doesnt_change_head_to_get`

  - Method: `test_http_302_changes_post_to_get`

  - Method: `test_http_302_doesnt_change_head_to_get`

  - Method: `test_http_303_changes_post_to_get`

  - Method: `test_http_303_doesnt_change_head_to_get`

  - Method: `test_header_and_body_removal_on_redirect`

  - Method: `test_transfer_enc_removal_on_redirect`

  - Method: `test_fragment_maintained_on_redirect`

  - Method: `test_HTTP_200_OK_GET_WITH_PARAMS`

  - Method: `test_HTTP_200_OK_GET_WITH_MIXED_PARAMS`

  - Method: `test_set_cookie_on_301`

  - Method: `test_cookie_sent_on_redirect`

  - Method: `test_cookie_removed_on_expire`

  - Method: `test_cookie_quote_wrapped`

  - Method: `test_cookie_persists_via_api`

  - Method: `test_request_cookie_overrides_session_cookie`

  - Method: `test_request_cookies_not_persisted`

  - Method: `test_generic_cookiejar_works`

  - Method: `test_param_cookiejar_works`

  - Method: `test_cookielib_cookiejar_on_redirect`

  - Method: `test_requests_in_history_are_not_overridden`

  - Method: `test_history_is_always_a_list`

  - Method: `test_headers_on_session_with_None_are_not_sent`

  - Method: `test_headers_preserve_order`

  - Method: `test_user_agent_transfers`

  - Method: `test_HTTP_200_OK_HEAD`

  - Method: `test_HTTP_200_OK_PUT`

  - Method: `test_BASICAUTH_TUPLE_HTTP_200_OK_GET`

  - Method: `test_set_basicauth`

  - Method: `test_basicauth_encodes_byte_strings`

  - Method: `test_errors`

  - Method: `test_proxy_error`

  - Method: `test_proxy_error_on_bad_url`

  - Method: `test_respect_proxy_env_on_send_self_prepared_request`

  - Method: `test_respect_proxy_env_on_send_session_prepared_request`

  - Method: `test_respect_proxy_env_on_send_with_redirects`

  - Method: `test_respect_proxy_env_on_get`

  - Method: `test_respect_proxy_env_on_request`

  - Method: `test_proxy_authorization_preserved_on_request`

  - Method: `test_proxy_authorization_not_appended_to_https_request`

  - Method: `test_basicauth_with_netrc`

  - Method: `test_basicauth_with_netrc_leak`

  - Method: `test_DIGEST_HTTP_200_OK_GET`

  - Method: `test_DIGEST_AUTH_RETURNS_COOKIE`

  - Method: `test_DIGEST_AUTH_SETS_SESSION_COOKIES`

  - Method: `test_DIGEST_STREAM`

  - Method: `test_DIGESTAUTH_WRONG_HTTP_401_GET`

  - Method: `test_DIGESTAUTH_QUOTES_QOP_VALUE`

  - Method: `test_POSTBIN_GET_POST_FILES`

  - Method: `test_invalid_files_input`

  - Method: `test_POSTBIN_SEEKED_OBJECT_WITH_NO_ITER`

  - Method: `test_POSTBIN_GET_POST_FILES_WITH_DATA`

  - Method: `test_post_with_custom_mapping`

  - Method: `test_conflicting_post_params`

  - Method: `test_request_ok_set`

  - Method: `test_status_raising`

  - Method: `test_decompress_gzip`

  - Method: `test_unicode_get`

  - Method: `test_unicode_header_name`

  - Method: `test_pyopenssl_redirect`

  - Method: `test_invalid_ca_certificate_path`

  - Method: `test_invalid_ssl_certificate_files`

  - Method: `test_env_cert_bundles`

  - Method: `test_http_with_certificate`

  - Method: `test_https_warnings`

  - Method: `test_certificate_failure`

  - Method: `test_urlencoded_get_query_multivalued_param`

  - Method: `test_form_encoded_post_query_multivalued_element`

  - Method: `test_different_encodings_dont_break_post`

  - Method: `test_unicode_multipart_post`

  - Method: `test_unicode_multipart_post_fieldnames`

  - Method: `test_unicode_method_name`

  - Method: `test_unicode_method_name_with_request_object`

  - Method: `test_non_prepared_request_error`

  - Method: `test_custom_content_type`

  - Method: `test_hook_receives_request_arguments`

  - Method: `test_session_hooks_are_used_with_no_request_hooks`

  - Method: `test_session_hooks_are_overridden_by_request_hooks`

  - Method: `test_prepared_request_hook`

  - Method: `test_prepared_from_session`

  - Method: `test_prepare_request_with_bytestring_url`

  - Method: `test_request_with_bytestring_host`

  - Method: `test_links`

  - Method: `test_cookie_parameters`

  - Method: `test_cookie_as_dict_keeps_len`

  - Method: `test_cookie_as_dict_keeps_items`

  - Method: `test_cookie_as_dict_keys`

  - Method: `test_cookie_as_dict_values`

  - Method: `test_cookie_as_dict_items`

  - Method: `test_cookie_duplicate_names_different_domains`

  - Method: `test_cookie_duplicate_names_raises_cookie_conflict_error`

  - Method: `test_cookie_policy_copy`

  - Method: `test_time_elapsed_blank`

  - Method: `test_empty_response_has_content_none`

  - Method: `test_response_is_iterable`

  - Method: `test_response_decode_unicode`

  - Method: `test_response_reason_unicode`

  - Method: `test_response_reason_unicode_fallback`

  - Method: `test_response_chunk_size_type`

  - Method: `test_iter_content_wraps_exceptions`

  - Method: `test_request_and_response_are_pickleable`

  - Method: `test_prepared_request_is_pickleable`

  - Method: `test_prepared_request_with_file_is_pickleable`

  - Method: `test_prepared_request_with_hook_is_pickleable`

  - Method: `test_cannot_send_unprepared_requests`

  - Method: `test_http_error`

  - Method: `test_session_pickling`

  - Method: `test_fixes_1329`

  - Method: `test_uppercase_scheme_redirect`

  - Method: `test_transport_adapter_ordering`

  - Method: `test_session_get_adapter_prefix_matching`

  - Method: `test_session_get_adapter_prefix_matching_mixed_case`

  - Method: `test_session_get_adapter_prefix_matching_is_case_insensitive`

  - Method: `test_session_get_adapter_prefix_with_trailing_slash`

  - Method: `test_session_get_adapter_prefix_without_trailing_slash`

  - Method: `test_header_remove_is_case_insensitive`

  - Method: `test_params_are_merged_case_sensitive`

  - Method: `test_long_authinfo_in_url`

  - Method: `test_header_keys_are_native`

  - Method: `test_header_validation`

  - Method: `test_header_value_not_str`

  - Method: `test_header_no_return_chars`

  - Method: `test_header_no_leading_space`

  - Method: `test_header_with_subclass_types`

  - Method: `test_can_send_objects_with_files`

  - Method: `test_can_send_file_object_with_non_string_filename`

  - Method: `test_autoset_header_values_are_native`

  - Method: `test_nonhttp_schemes_dont_check_URLs`

  - Method: `test_auth_is_stripped_on_http_downgrade`

  - Method: `test_auth_is_retained_for_redirect_on_host`

  - Method: `test_should_strip_auth_host_change`

  - Method: `test_should_strip_auth_http_downgrade`

  - Method: `test_should_strip_auth_https_upgrade`

  - Method: `test_should_strip_auth_port_change`

  - Method: `test_should_strip_auth_default_port`

  - Method: `test_manual_redirect_with_partial_body_read`

  - Method: `test_prepare_body_position_non_stream`

  - Method: `test_rewind_body`

  - Method: `test_rewind_partially_read_body`

  - Method: `test_rewind_body_no_seek`

  - Method: `test_rewind_body_failed_seek`

  - Method: `test_rewind_body_failed_tell`

  - Method: `_patch_adapter_gzipped_redirect`

  - Method: `test_redirect_with_wrong_gzipped_header`

  - Method: `test_basic_auth_str_is_always_native`

  - Method: `test_requests_history_is_saved`

  - Method: `test_json_param_post_content_type_works`

  - Method: `test_json_param_post_should_not_override_data_param`

  - Method: `test_response_iter_lines`

  - Method: `test_response_context_manager`

  - Method: `test_unconsumed_session_response_closes_connection`

  - Method: `test_response_iter_lines_reentrant`

  - Method: `test_session_close_proxy_clear`

  - Method: `test_proxy_auth`

  - Method: `test_proxy_auth_empty_pass`

  - Method: `test_response_json_when_content_is_None`

  - Method: `test_response_without_release_conn`

  - Method: `test_empty_stream_with_auth_does_not_set_content_length_header`

  - Method: `test_stream_with_auth_does_not_set_transfer_encoding_header`

  - Method: `test_chunked_upload_does_not_set_content_length_header`

  - Method: `test_custom_redirect_mixin`

- **Class** `TestCaseInsensitiveDict`

  - Method: `test_init`

  - Method: `test_docstring_example`

  - Method: `test_len`

  - Method: `test_getitem`

  - Method: `test_fixes_649`

  - Method: `test_delitem`

  - Method: `test_contains`

  - Method: `test_get`

  - Method: `test_update`

  - Method: `test_update_retains_unchanged`

  - Method: `test_iter`

  - Method: `test_equality`

  - Method: `test_setdefault`

  - Method: `test_lower_items`

  - Method: `test_preserve_key_case`

  - Method: `test_preserve_last_key_case`

  - Method: `test_copy`

- **Class** `TestMorselToCookieExpires`

  - Doc: Tests for morsel_to_cookie when morsel contains expires.

  - Method: `test_expires_valid_str`

  - Method: `test_expires_invalid_int`

  - Method: `test_expires_none`

- **Class** `TestMorselToCookieMaxAge`

  - Doc: Tests for morsel_to_cookie when morsel contains max-age.

  - Method: `test_max_age_valid_int`

  - Method: `test_max_age_invalid_str`

- **Class** `TestTimeout`

  - Method: `test_stream_timeout`

  - Method: `test_invalid_timeout`

  - Method: `test_none_timeout`

  - Method: `test_read_timeout`

  - Method: `test_connect_timeout`

  - Method: `test_total_timeout_connect`

  - Method: `test_encoded_methods`

- **Class** `RedirectSession`

  - Method: `__init__`

  - Method: `send`

  - Method: `build_response`

  - Method: `_build_raw`

- **Class** `TestPreparingURLs`

  - Method: `test_preparing_url`

  - Method: `test_preparing_bad_url`

  - Method: `test_redirecting_to_bad_url`

  - Method: `test_url_mutation`

  - Method: `test_parameters_for_nonstandard_schemes`

  - Method: `test_post_json_nan`

  - Method: `test_json_decode_compatibility`

  - Method: `test_json_decode_persists_doc_attr`

  - Method: `test_status_code_425`

  - Method: `test_different_connection_pool_for_tls_settings_verify_True`

  - Method: `test_different_connection_pool_for_tls_settings_verify_bundle_expired_cert`

  - Method: `test_different_connection_pool_for_tls_settings_verify_bundle_unexpired_cert`

  - Method: `test_different_connection_pool_for_mtls_settings`

- **Function** `test_json_encodes_as_bytes`

- **Function** `test_requests_are_updated_each_time`

- **Function** `test_proxy_env_vars_override_default`

- **Function** `test_data_argument_accepts_tuples`

  - Doc: Ensure that the data argument will accept tuples of strings
and properly encode them.

- **Function** `test_prepared_copy`

- **Function** `test_urllib3_retries`

- **Function** `test_urllib3_pool_connection_closed`

- **Function** `test_content_length_for_bytes_data`

- **Function** `test_content_length_for_string_data_counts_bytes`

- **Function** `test_json_decode_errors_are_serializable_deserializable`

### `tests/test_packages.py`

- **Function** `test_can_access_urllib3_attribute`

- **Function** `test_can_access_idna_attribute`

- **Function** `test_can_access_chardet_attribute`

### `tests/test_lowlevel.py`

- **Function** `echo_response_handler`

  - Doc: Simple handler that will take request and echo it back to requester.

- **Function** `test_chunked_upload`

  - Doc: can safely send generators

- **Function** `test_chunked_encoding_error`

  - Doc: get a ChunkedEncodingError if the server returns a bad response

- **Function** `test_chunked_upload_uses_only_specified_host_header`

  - Doc: Ensure we use only the specified Host header for chunked requests.

- **Function** `test_chunked_upload_doesnt_skip_host_header`

  - Doc: Ensure we don't omit all Host headers with chunked requests.

- **Function** `test_conflicting_content_lengths`

  - Doc: Ensure we correctly throw an InvalidHeader error if multiple
conflicting Content-Length headers are returned.

- **Function** `test_digestauth_401_count_reset_on_redirect`

  - Doc: Ensure we correctly reset num_401_calls after a successful digest auth,
followed by a 302 redirect to another digest auth prompt.

See https://github.com/psf/requests/issues/1979.

- **Function** `test_digestauth_401_only_sent_once`

  - Doc: Ensure we correctly respond to a 401 challenge once, and then
stop responding if challenged again.

- **Function** `test_digestauth_only_on_4xx`

  - Doc: Ensure we only send digestauth on 4xx challenges.

See https://github.com/psf/requests/issues/3772.

- **Function** `test_use_proxy_from_environment`

- **Function** `test_redirect_rfc1808_to_non_ascii_location`

- **Function** `test_fragment_not_sent_with_request`

  - Doc: Verify that the fragment portion of a URI isn't sent to the server.

- **Function** `test_fragment_update_on_redirect`

  - Doc: Verify we only append previous fragment if one doesn't exist on new
location. If a new fragment is encountered in a Location header, it should
be added to all subsequent requests.

- **Function** `test_json_decode_compatibility_for_alt_utf_encodings`

### `tests/test_structures.py`

- **Class** `TestCaseInsensitiveDict`

  - Method: `setup`

  - Method: `test_list`

  - Method: `test_getitem`

  - Method: `test_delitem`

  - Method: `test_lower_items`

  - Method: `test_repr`

  - Method: `test_copy`

  - Method: `test_instance_equality`

- **Class** `TestLookupDict`

  - Method: `setup`

  - Method: `test_repr`

  - Method: `test_getitem`

  - Method: `test_get`

### `tests/compat.py`

- **Function** `u`

### `tests/test_adapters.py`

- **Function** `test_request_url_trims_leading_path_separators`

  - Doc: See also https://github.com/psf/requests/issues/6643.

### `tests/test_utils.py`

- **Class** `TestSuperLen`

  - Method: `test_io_streams`

  - Method: `test_super_len_correctly_calculates_len_of_partially_read_file`

  - Method: `test_super_len_handles_files_raising_weird_errors_in_tell`

  - Method: `test_super_len_tell_ioerror`

  - Method: `test_string`

  - Method: `test_file`

  - Method: `test_tarfile_member`

  - Method: `test_super_len_with__len__`

  - Method: `test_super_len_with_no__len__`

  - Method: `test_super_len_with_tell`

  - Method: `test_super_len_with_fileno`

  - Method: `test_super_len_with_no_matches`

- **Class** `TestGetNetrcAuth`

  - Method: `test_works`

  - Method: `test_not_vulnerable_to_bad_url_parsing`

- **Class** `TestToKeyValList`

  - Method: `test_valid`

  - Method: `test_invalid`

- **Class** `TestUnquoteHeaderValue`

  - Method: `test_valid`

  - Method: `test_is_filename`

- **Class** `TestGetEnvironProxies`

  - Doc: Ensures that IP addresses are correctly matches with ranges
in no_proxy variable.

  - Method: `no_proxy`

  - Method: `test_bypass`

  - Method: `test_not_bypass`

  - Method: `test_bypass_no_proxy_keyword`

  - Method: `test_not_bypass_no_proxy_keyword`

- **Class** `TestIsIPv4Address`

  - Method: `test_valid`

  - Method: `test_invalid`

- **Class** `TestIsValidCIDR`

  - Method: `test_valid`

  - Method: `test_invalid`

- **Class** `TestAddressInNetwork`

  - Method: `test_valid`

  - Method: `test_invalid`

- **Class** `TestGuessFilename`

  - Method: `test_guess_filename_invalid`

  - Method: `test_guess_filename_valid`

- **Class** `TestExtractZippedPaths`

  - Method: `test_unzipped_paths_unchanged`

  - Method: `test_zipped_paths_extracted`

  - Method: `test_invalid_unc_path`

- **Class** `TestContentEncodingDetection`

  - Method: `test_none`

  - Method: `test_pragmas`

  - Method: `test_precedence`

- **Class** `TestGuessJSONUTF`

  - Method: `test_encoded`

  - Method: `test_bad_utf_like_encoding`

  - Method: `test_guess_by_bom`

- **Function** `test_get_auth_from_url`

- **Function** `test_requote_uri_with_unquoted_percents`

  - Doc: See: https://github.com/psf/requests/issues/2356

- **Function** `test_unquote_unreserved`

- **Function** `test_dotted_netmask`

- **Function** `test_select_proxies`

  - Doc: Make sure we can select per-host proxies correctly.

- **Function** `test_parse_dict_header`

- **Function** `test__parse_content_type_header`

- **Function** `test_get_encoding_from_headers`

- **Function** `test_iter_slices`

- **Function** `test_parse_header_links`

- **Function** `test_prepend_scheme_if_needed`

- **Function** `test_to_native_string`

- **Function** `test_urldefragauth`

- **Function** `test_should_bypass_proxies`

  - Doc: Tests for function should_bypass_proxies to check if proxy
can be bypassed or not

- **Function** `test_should_bypass_proxies_pass_only_hostname`

  - Doc: The proxy_bypass function should be called with a hostname or IP without
a port number or auth credentials.

- **Function** `test_add_dict_to_cookiejar`

  - Doc: Ensure add_dict_to_cookiejar works for
non-RequestsCookieJar CookieJars

- **Function** `test_unicode_is_ascii`

- **Function** `test_should_bypass_proxies_no_proxy`

  - Doc: Tests for function should_bypass_proxies to check if proxy
can be bypassed or not using the 'no_proxy' argument

- **Function** `test_should_bypass_proxies_win_registry`

  - Doc: Tests for function should_bypass_proxies to check if proxy
can be bypassed or not with Windows registry settings

- **Function** `test_should_bypass_proxies_win_registry_bad_values`

  - Doc: Tests for function should_bypass_proxies to check if proxy
can be bypassed or not with Windows invalid registry settings.

- **Function** `test_set_environ`

  - Doc: Tests set_environ will set environ values and will restore the environ.

- **Function** `test_set_environ_raises_exception`

  - Doc: Tests set_environ will raise exceptions in context when the
value parameter is None.

- **Function** `test_should_bypass_proxies_win_registry_ProxyOverride_value`

  - Doc: Tests for function should_bypass_proxies to check if proxy
can be bypassed or not with Windows ProxyOverride registry value ending with a semicolon.

### `tests/conftest.py`

- **Function** `prepare_url`

- **Function** `httpbin`

- **Function** `httpbin_secure`

- **Function** `nosan_server`

### `tests/test_testserver.py`

- **Class** `TestTestServer`

  - Method: `test_basic`

  - Method: `test_server_closes`

  - Method: `test_text_response`

  - Method: `test_basic_response`

  - Method: `test_basic_waiting_server`

  - Method: `test_multiple_requests`

  - Method: `test_request_recovery`

  - Method: `test_requests_after_timeout_are_not_received`

  - Method: `test_request_recovery_with_bigger_timeout`

  - Method: `test_server_finishes_on_error`

  - Method: `test_server_finishes_when_no_connections`

### `tests/test_hooks.py`

- **Function** `hook`

- **Function** `test_hooks`

- **Function** `test_default_hooks`

### `tests/test_help.py`

- **Class** `VersionedPackage`

  - Method: `__init__`

- **Function** `test_system_ssl`

  - Doc: Verify we're actually setting system_ssl when it should be available.

- **Function** `test_idna_without_version_attribute`

  - Doc: Older versions of IDNA don't provide a __version__ attribute, verify
that if we have such a package, we don't blow up.

- **Function** `test_idna_with_version_attribute`

  - Doc: Verify we're actually setting idna version when it should be available.

### `tests/__init__.py`

> Requests test package initialisation.


### `tests/utils.py`

- **Function** `override_environ`

### `tests/testserver/__init__.py`

### `tests/testserver/server.py`

- **Class** `Server`

  - Doc: Dummy server using for unit testing

  - Method: `__init__`

  - Method: `text_response_server`

  - Method: `basic_response_server`

  - Method: `run`

  - Method: `_create_socket_and_bind`

  - Method: `_close_server_sock_ignore_errors`

  - Method: `_handle_requests`

  - Method: `_accept_connection`

  - Method: `__enter__`

  - Method: `__exit__`

- **Class** `TLSServer`

  - Method: `__init__`

  - Method: `_create_socket_and_bind`

- **Function** `consume_socket_content`
