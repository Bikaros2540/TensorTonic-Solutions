import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.array(x)
    sig = 1/(1+np.exp(-x))
    return x*sig
    pass