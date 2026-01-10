from typing import List
from langchain.schema import Document


def chunk_with_line_numbers(
    docs: List[Document],
    chunk_size: int = 20,
    overlap: int = 3,
) -> List[Document]:
    chunks = []

    for doc in docs:
        lines = doc.page_content.splitlines()
        page = doc.metadata.get("page", 0)
        source = doc.metadata.get("source")

        start = 0
        while start < len(lines):
            end = min(start + chunk_size, len(lines))

            chunks.append(
                Document(
                    page_content="\n".join(lines[start:end]),
                    metadata={
                        "source": source,
                        "page": page,
                        "line_start": start + 1,
                        "line_end": end,
                    },
                )
            )

            start += chunk_size - overlap

    return chunks

