import numpy as np

def minmax_scale(x, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    M, m = np.max(x, axis=axis, keepdims=True), np.min(x, axis=axis, keepdims=True)
    den = M-m
    return (x-m)/np.maximum(den,eps)
    
    pass