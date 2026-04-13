import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    d = {v: 0 for v in vocab}
    for v in tokens:
        if v in d:
            d[v] += 1
    x = [x for x in d.values()]
    if not x:
        x = np.zeros(len(vocab))
    return np.array(x, dtype = np.int64)
    pass