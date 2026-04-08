def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    in_ = 0
    top_k = recommended[:k]
    relevant = set(relevant)
    r = len(relevant)
    for e in top_k:
        if e in relevant:
            in_ +=1
    return [in_*1.0/k , in_*1.0/r]