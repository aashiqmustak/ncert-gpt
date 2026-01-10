import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from .formatting import format_docs_with_citations

load_dotenv()  # loads .env automatically

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in .env")

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a strict document-grounded assistant.

RULES:
- Use ONLY the provided context
- EVERY answer sentence MUST include citation
- Citation format:
(Source: <file>, Page <page>, Lines <start>-<end>)
- If not found, say: "Not found in the provided documents"

Context:
{context}

Question:
{question}

Answer:
""",
)

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-8b-8192",
    temperature=0,
)


def run_rag(query: str, vectordb: Chroma) -> str:
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    docs = retriever.get_relevant_documents(query)

    context = format_docs_with_citations(docs)

    response = llm.invoke(
        RAG_PROMPT.format(
            context=context,
            question=query,
        )
    )

    return response.content

