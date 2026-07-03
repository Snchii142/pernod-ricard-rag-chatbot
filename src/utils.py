"""
Utility functions for the RAG chatbot.
"""


def format_sources(chunks):
    """
    Format retrieved sources for display.
    """

    if not chunks:
        return "No sources available."

    lines = []

    lines.append("\nSources:\n")

    seen = set()

    for chunk in chunks:

        metadata = chunk["metadata"]

        key = (
            metadata["title"],
            metadata["url"]
        )

        if key in seen:
            continue

        seen.add(key)

        lines.append(
            f"• {metadata['brand']}"
        )

        lines.append(
            f"  {metadata['title']}"
        )

        lines.append(
            f"  {metadata['url']}\n"
        )

    return "\n".join(lines)