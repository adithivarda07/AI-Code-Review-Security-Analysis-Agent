from rag.embedder import get_embedding_model

embedding_model = get_embedding_model()

vector = embedding_model.embed_query("Hello World")

print("Embedding Dimension:", len(vector))

print("\nFirst 10 Values:")

print(vector[:10])