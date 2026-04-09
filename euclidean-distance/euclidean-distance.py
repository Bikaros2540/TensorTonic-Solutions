import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x, y = np.array(x), np.array(y)
    return np.sqrt(sum((x-y)**2))
    pass