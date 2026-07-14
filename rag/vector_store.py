from langchain_community.vectorstores import FAISS

from rag.embedder import get_embedding_model


def create_vector_store(chunks):

    embedding_model = get_embedding_model()

    vector_store = FAISS.from_documents(
        chunks,
        embedding_model
    )

    vector_store.save_local("vector_db")

    return vector_store