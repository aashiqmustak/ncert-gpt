from typing import List
    return loader.load()

        raise ValueError("Unsupported file type")
    else:
        loader = Docx2txtLoader(file_path)
    elif file_path.endswith(".docx"):
        loader = TextLoader(file_path, encoding="utf-8")
    elif file_path.endswith(".txt"):
        loader = PyPDFLoader(file_path)
    if file_path.endswith(".pdf"):
def load_documents(file_path: str) -> List[Document]:


)
    Docx2txtLoader,
    TextLoader,
    PyPDFLoader,
from langchain_community.document_loaders import (
from langchain.schema import Document

