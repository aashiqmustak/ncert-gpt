from typing import List
from langchain.schema import Document


def format_docs_with_citations(docs: List[Document]) -> str:
    formatted = []

    for i, doc in enumerate(docs, start=1):
        m = doc.metadata
        formatted.append(
            f"""
[Source {i}]
File: {m.get('source')}
Page: {m.get('page')}
Lines: {m.get('line_start')}-{m.get('line_end')}
Content:
{doc.page_content}
"""
        )

    return "\n".join(formatted)

