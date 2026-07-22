from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    BSHTMLLoader,
     TextLoader
)


def load_documents():

    documents = []

    base_path = Path("knowledge_base")

    for file in base_path.rglob("*"):

        if file.suffix.lower() == ".pdf":

            loader = PyPDFLoader(str(file))
            documents.extend(loader.load())

        elif file.suffix.lower() == ".html":

            try:

                loader = BSHTMLLoader(
                    str(file),
                    open_encoding="utf-8"
                )

                documents.extend(loader.load())

            except Exception as e:

                print(f"Skipped {file.name}: {e}")
                
        elif file.suffix.lower() == ".txt":

            loader = TextLoader(
                str(file),
                encoding="utf-8"
            )

            documents.extend(loader.load())

    return documents