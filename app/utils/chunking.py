def chunk_text(text: str, max_len: int = 600):
    words = text.split()
    chunks = []

    cur = []
    cur_len = 0

    for w in words:
        cur.append(w)
        cur_len += len(w)
        if cur_len > max_len:
            chunks.append(" ".join(cur))
            cur = []
            cur_len = 0

    if cur:
        chunks.append(" ".join(cur))

    return chunks
