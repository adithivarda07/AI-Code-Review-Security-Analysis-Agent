# AI Code Review & Security Analysis Agent

AI-powered static code review and security analysis tool for Python and Java, developed as part of the **Infosys Springboard Virtual Internship 7.0**.

---

## Project Overview

The AI Code Review & Security Analysis Agent is designed to assist developers in identifying code quality issues and common security vulnerabilities through automated static analysis.

The project currently supports Python and Java source code analysis and includes a structured secure coding knowledge base. Future enhancements will integrate Retrieval-Augmented Generation (RAG) to provide context-aware security recommendations using trusted secure coding resources.

---

## Features

- Upload Python (`.py`) and Java (`.java`) source files
- Paste source code directly into the application
- Automatic language detection
- Python syntax validation using Abstract Syntax Tree (AST)
- Static code quality analysis
- Basic security vulnerability detection
- Code quality scoring
- Review summary generation
- View submitted source code after analysis

---

## Supported Languages

- Python
- Java

---

## Security Checks

The current implementation detects:

- Hardcoded passwords
- Usage of `eval()`
- Usage of `exec()`
- SQL query identification
- Debug print statements
- TODO comments
- Large source files
- Presence of comments

---

## Knowledge Base

The secure coding knowledge base currently includes documentation from:

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

These resources form the foundation for the upcoming Retrieval-Augmented Generation (RAG) pipeline.

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
└── .gitignore
```

---

## Technology Stack

- Python
- Streamlit
- LangChain
- AST (Python Standard Library)
- PDF Document Loader
- HTML Document Loader

---

## Current Implementation

The current implementation includes:

- Streamlit-based user interface
- Modular code architecture
- Static code quality analysis
- Security vulnerability detection
- Python syntax validation
- Secure coding knowledge base
- PDF and HTML document loading for RAG preparation

Future development will focus on:

- Document chunking
- Embedding generation
- Vector database integration
- Retrieval-Augmented Generation (RAG)
- AI-powered security recommendations

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/adithivarda07/AI-Code-Review-Security-Analysis-Agent.git
```

### Navigate to the project

```bash
cd AI-Code-Review-Security-Analysis-Agent
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Developer

**Adithi Varda**




