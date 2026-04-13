import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a, b = np.array(a), np.array(b)
    nor_a, nor_b = np.linalg.norm(a), np.linalg.norm(b)
    if nor_a*nor_b == 0.0:
        return 0.0
    return np.dot(a,b)/nor_a/nor_b
    pass