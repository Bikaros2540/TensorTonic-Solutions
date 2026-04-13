import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x , y = np.array(x,dtype=np.float64), np.array(y,dtype=np.float64)
    return np.sum(np.abs(x-y))
    
    pass