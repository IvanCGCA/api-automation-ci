# 🚀 API Automation & CI/CD Pipeline (GitHub Actions)

[![CI Status](https://img.shields.io/badge/build-passing-brightgreen?logo=github-actions)](https://github.com/tu_usuario/tu_repositorio/actions)

## 📝 Project Overview
This repository implements a professional **Continuous Integration (CI)** workflow. It goes beyond localized test execution by orchestrating automated API tests within ephemeral cloud environments (Linux containers). The primary goal is to ensure code quality, build stability, and validate every code change automatically before it is integrated into the main branch.

## 🛠️ Tech Stack & CI/CD Tooling
* **Language:** Python 3.12
* **Testing Framework:** Pytest
* **HTTP Client:** Requests
* **CI/CD Orchestration:** GitHub Actions (YAML Workflows)
* **Execution Environment:** Ubuntu Latest (GitHub Hosted Runner)

## 🏗️ CI/CD Pipeline Architecture
The workflow (`main.yml`) automatically triggers on every `push` and `pull_request`, executing the following stages:
1. **Checkout:** Fetches the repository source code into the virtual runner.
2. **Setup Environment:** Provisions the Python 3.12 runtime.
3. **Dependency Management:** Installs all required libraries defined in `requirements.txt`.
4. **Automated Execution:** Triggers the Pytest suite and outputs the build status.

## 🧪 Testing Scope
The automated suite focuses on critical backend validation:
* **Status Code Validation:** Ensures endpoints respond accurately (e.g., HTTP 200 OK, 404 Not Found).
* **JSON Integrity Verification:** Validates that the returned data structures comply with defined business rules.
* **Contract Testing:** Strictly validates data types, schema integrity, and object IDs in the API responses.

## 📂 Project Structure
```text
api-cicd-automation/
├── .github/
│   └── workflows/
│       └── main.yml       # GitHub Actions CI/CD configuration file
├── tests/
│   └── test_api.py        # Pytest scripts targeting the API
├── requirements.txt       # Python dependencies
└── README.md
```

🚀 Getting Started (Local Execution)
If you want to run the pipeline tests locally:

```Bash
# Clone the repository
git clone [https://github.com/tu_usuario/tu_repositorio.git](https://github.com/tu_usuario/tu_repositorio.git)
cd tu_repositorio

# Activate virtual environment and install dependencies
python -m venv venv
# Windows: .\venv\Scripts\activate | Mac/Linux: source venv/bin/activate
pip install -r requirements.txt

# Run tests locally
pytest -v
```

Linkedin: www.linkedin.com/in/ivan-vega-porras


CI/CD & QA Engineered by Iván Vega Porras
