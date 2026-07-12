from rag.loader import load_documents
from rag.chunker import chunk_documents


documents = load_documents()

chunks = chunk_documents(documents)

print("Documents Loaded :", len(documents))
print("Chunks Created   :", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])