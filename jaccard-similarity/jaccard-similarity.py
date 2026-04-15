def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    a, b  = set(set_a), set(set_b)
    if a == set() == b:
        return 0.0
    inter = a & b
    union = a | b
    return len(inter)/len(union)*1.0