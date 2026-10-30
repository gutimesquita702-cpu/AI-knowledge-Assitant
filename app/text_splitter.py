def split_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    overlap = 50

    if chunk_size <= overlap:
        raise ValueError(f"chunk_size must be greater than {overlap}")

    if not words:
        return chunks

    for i in range(0, len(words), chunk_size - overlap):
        chunks.append(" ".join(words[i:i + chunk_size]))

    return chunks