# AI Code Review & Security Analysis Agent

An AI-powered static code review and security analysis tool developed as part of the **Infosys Springboard Virtual Internship 7.0**.

The application analyzes Python and Java source code for syntax errors, code quality issues, and common security vulnerabilities. It also includes a Retrieval-Augmented Generation (RAG) knowledge pipeline built from secure coding standards and best practice documents.

---

## Project Overview

The objective of this project is to assist developers by performing automated code reviews and security analysis while leveraging trusted secure coding documentation for future AI-assisted recommendations.

The project combines static code analysis with a RAG pipeline that prepares OWASP, Oracle Java, and Python security documentation for semantic retrieval.

---

## Features

- Upload Python (`.py`) and Java (`.java`) source files
- Paste source code directly into the application
- Automatic language detection
- Python syntax validation using AST
- Static code quality analysis
- Basic security vulnerability detection
- Code quality scoring
- Code review summary generation
- Secure coding knowledge base
- RAG document indexing pipeline

---

## Supported Languages

- Python
- Java

---

## Security Checks

Current implementation detects:

- Hardcoded passwords
- Usage of `eval()`
- Usage of `exec()`
- SQL query identification
- Debug print statements
- TODO comments
- Large source files
- Missing or limited comments

---

## Secure Coding Knowledge Base

The knowledge base includes trusted secure coding resources from:

### OWASP

- OWASP Top 10 (2021)
- OWASP Secure Coding Practices
- OWASP Developer Guide

### Python

- Python Security Considerations
- Python Secure Coding Guide

### Java

- Oracle Java Secure Coding Guidelines
- Java Code Conventions

These documents are processed through the RAG pipeline for semantic search.

---

## System Architecture

```text
                         +----------------------+
                         |     Streamlit UI     |
                         +----------+-----------+
                                    |
                     Upload File / Paste Source Code
                                    |
                                    ▼
                     +---------------------------+
                     |     Code Processing       |
                     +------------+--------------+
                                  |
        +-------------------------+-------------------------+
        |                         |                         |
        ▼                         ▼                         ▼
+----------------+      +----------------+      +----------------+
|   Validator    |      | Code Analysis  |      | Security Check |
+----------------+      +----------------+      +----------------+
        |                         |                         |
        +-------------------------+-------------------------+
                                  |
                                  ▼
                      Code Review & Security Report

────────────────────────────────────────────────────────────

                 Secure Coding Knowledge Base

      PDF / HTML Documents
               │
               ▼
        Document Loader
               │
               ▼
      Document Chunking
               │
               ▼
   Embedding Generation
               │
               ▼
      FAISS Vector Store
```

---

## Project Structure

```text
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
├── test_loader.py
├── test_chunker.py
├── test_embedder.py
├── test_vector_store.py
└── requirements.txt
```

---

## Technology Stack

- Python
- Streamlit
- LangChain
- Hugging Face Embeddings
- Sentence Transformers
- FAISS
- AST (Python Standard Library)

---

## RAG Pipeline

The secure coding knowledge base is processed using the following pipeline:

```text
Knowledge Base
      │
      ▼
Document Loader
      │
      ▼
Document Chunker
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Store
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/adithivarda07/AI-Code-Review-Security-Analysis-Agent.git
```

Move into the project directory:

```bash
cd AI-Code-Review-Security-Analysis-Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Developer

**Adithi Varda**

