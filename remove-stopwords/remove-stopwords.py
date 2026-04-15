def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    L = set(tokens)
    for c in stopwords:
        L.discard(c)
    out =[c for c in tokens if c in L]
    return out 
    pass