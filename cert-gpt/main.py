"""
RAG Pipeline with Page + Line Number Citations
----------------------------------------------
Documents: TXT / DOCX / PDF
Vector DB : Chroma
Embeddings: HuggingFace
LLM : Groq (dotenv-based)
Framework : LangChain
"""

# ...existing code...

from controllers.loader import load_documents
from controllers.chunker import chunk_with_line_numbers
from controllers.vectordb import build_vectorstore
from controllers.rag import run_rag

if __name__ == "__main__":
    FILE_PATH = "sample.pdf"  # pdf / txt / docx

    print("Loading documents...")
    docs = load_documents(FILE_PATH)

    print("Chunking with page & line numbers...")
    chunks = chunk_with_line_numbers(docs)

    print("Building vector store...")
    vectordb = build_vectorstore(chunks)

    while True:
        query = input("\nAsk a question (or 'exit'): ")
        if query.lower() == "exit":
            break

        answer = run_rag(query, vectordb)

        print("\n===== ANSWER =====\n")
        print(answer)

