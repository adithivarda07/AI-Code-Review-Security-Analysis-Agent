from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.vector_store import create_vector_store

documents = load_documents()

chunks = chunk_documents(documents)

vector_store = create_vector_store(chunks)

print("Documents Loaded :", len(documents))
print("Chunks Created   :", len(chunks))

print("\nVector Store Created Successfully!")