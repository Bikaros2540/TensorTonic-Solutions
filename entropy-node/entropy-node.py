import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    H = 0.0
    _, counts= np.unique(y, return_counts=True)
    l = len(y)
    for p in counts:
        prob=1.0* p / l
        print(prob)
        H -= prob * np.log2(prob)
    return H
        
    pass