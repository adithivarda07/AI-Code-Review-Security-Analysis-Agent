from rag.loader import load_documents

docs = load_documents()

print(f"Documents Loaded: {len(docs)}")

if docs:
    print("\nFirst Document Preview:\n")
    print(docs[0].page_content[:500])