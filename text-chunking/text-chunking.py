def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    i  = 0
    out = []
    n = len(tokens)
    if not n:
        return out
    while True:
        chunck = tokens[i:min(i+chunk_size,n)]
        out.append(chunck)
        i += chunk_size
        if i >= n:
            break
        i -= overlap
    return out 