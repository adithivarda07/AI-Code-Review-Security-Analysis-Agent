# 🤖 AI Code Review & Security Analysis Agent

> AI-powered static code review and secure coding assistant for Python and Java.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Store-orange)
![Status](https://img.shields.io/badge/Status-Phase%201%20Completed-success)

---

## 📌 Project Overview

The **AI Code Review & Security Analysis Agent** is being developed as part of the **Infosys Springboard Virtual Internship 7.0**.

The objective of this project is to build an intelligent assistant capable of reviewing source code, detecting security vulnerabilities, recommending secure coding practices, and leveraging Retrieval-Augmented Generation (RAG) to provide context-aware guidance from trusted security documentation.

Currently, the application performs static analysis for Python and Java programs and lays the foundation for an AI-powered secure code review platform.

---

## 🎯 Objectives

- Perform automated static code analysis
- Detect common coding issues
- Identify basic security vulnerabilities
- Provide an overall code quality score
- Generate concise review summaries
- Build a secure coding knowledge base
- Integrate Retrieval-Augmented Generation (RAG) for intelligent recommendations

---

# ✨ Current Features (Phase 1)

### 📂 Code Input
- Upload Python (.py) and Java (.java) source files
- Paste source code directly into the application

### 🔍 Language Detection
- Automatic detection of:
  - Python
  - Java

### ✅ Syntax Validation
- Python syntax validation using Python AST
- Java file recognition

### 📊 Code Quality Analysis
- Detects debug print statements
- Detects TODO comments
- Detects oversized source files
- Detects presence of comments

### 🔒 Security Analysis
- Hardcoded password detection
- Detects usage of eval()
- Detects usage of exec()
- Detects SQL queries requiring parameterized execution

### 📈 Review Report
- Code Quality Score
- Security Findings
- Review Summary
- Submitted Code Viewer

---

# 🧠 Knowledge Base

The project includes a structured secure coding knowledge base containing industry-standard references.

### OWASP
- OWASP Top 10 (2021)
- OWASP Developer Guide
- OWASP Secure Coding Practices

### Python
- Python Security Considerations
- Python Secure Coding Guide

### Java
- Oracle Secure Coding Guidelines
- Java Code Conventions

---

# 📁 Project Structure

```
AI-Code-Review-Security-Analysis-Agent
│
├── knowledge_base/
│   ├── java/
│   ├── owasp/
│   └── python/
│
├── modules/
│   ├── analysis.py
│   ├── security.py
│   └── validator.py
│
├── rag/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   └── vector_store.py
│
├── reports/
├── screenshots/
├── app.py
└── test_loader.py
```

---

# 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS (Planned)
- Google Gemini API (Planned)

---

# 🚀 RAG Pipeline (In Progress)

The Retrieval-Augmented Generation pipeline is being implemented with the following workflow:

```
Knowledge Base
      │
      ▼
Document Loader
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Vector Database (FAISS)
      │
      ▼
Retriever
      │
      ▼
Gemini LLM
      │
      ▼
AI Security Recommendations
```

---

# 📌 Current Progress

| Module | Status |
|---------|--------|
| Streamlit Interface | ✅ Completed |
| File Upload | ✅ Completed |
| Language Detection | ✅ Completed |
| Python Syntax Validation | ✅ Completed |
| Static Code Analysis | ✅ Completed |
| Security Analysis | ✅ Completed |
| Modular Architecture | ✅ Completed |
| Knowledge Base | ✅ Completed |
| Document Loader | ✅ Completed |
| RAG Chunking | 🚧 In Progress |
| Embeddings | 🚧 In Progress |
| Vector Database | 🚧 In Progress |
| Gemini Integration | 🚧 Planned |

---

# ▶️ Running the Project

Clone the repository

```bash
git clone https://github.com/adithivarda07/AI-Code-Review-Security-Analysis-Agent.git
```

Navigate into the project

```bash
cd AI-Code-Review-Security-Analysis-Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📷 Screenshots

Project screenshots will be added during subsequent milestones.

---

# 👩‍💻 Developer

**Adithi Varda**

B.Tech – Information Technology

Infosys Springboard Virtual Internship 7.0

---

# 📄 License

This project is developed for educational purposes as part of the **Infosys Springboard Virtual Internship 7.0**.
