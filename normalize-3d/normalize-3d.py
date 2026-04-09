import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.array(v, dtype=np.float64)
    m = np.linalg.norm(v, axis=-1, keepdims=True)
    v_nor = np.where(m < 10e-10, v, v/m)
    return v_nor
