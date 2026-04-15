import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    x = np.array(X)
    n = np.shape(x)[0]
    if np.ndim(x) != 2 or n == 1:
        return None
    mu = np.mean(x, axis=0,keepdims=True)
    x = x-mu
    sig =(x.T@x)/(n-1)
    return sig
    pass