import os

from dotenv import load_dotenv
from groq import Groq

from rag.retriever import retrieve_documents
from modules.prompt_builder import build_prompt

# Load environment variables
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_assistant(question):

    # Retrieve relevant documents
    documents = retrieve_documents(question)

    # Build prompt
    prompt = build_prompt(question, documents)

    # Generate response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content