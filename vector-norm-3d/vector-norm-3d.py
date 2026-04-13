import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    v = np.array(v)
    return np.linalg.norm(v, axis=0 if np.size(v) ==3 else 1)        
    pass