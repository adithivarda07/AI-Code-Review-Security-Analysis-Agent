from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.vector_store import create_vector_store


def main():

    print("Loading documents...")

    documents = load_documents()

    print(f"Loaded {len(documents)} documents.")

    print("Chunking documents...")

    chunks = chunk_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating FAISS vector database...")

    create_vector_store(chunks)

    print("Vector database created successfully!")


if __name__ == "__main__":
    main()