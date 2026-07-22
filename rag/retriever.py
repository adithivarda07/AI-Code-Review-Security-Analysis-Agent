from langchain_community.vectorstores import FAISS

from rag.embedder import get_embedding_model


def load_vector_store():

    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        "vector_db",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store


def retrieve_documents(query, k=3):

    vector_store = load_vector_store()

    documents = vector_store.similarity_search(
        query,
        k=k
    )

    return documents