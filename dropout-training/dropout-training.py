import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    x = np.array(x)
    if rng is not None:
        mask = rng.random(np.shape(x)) < (1 - p)
    else:
        mask = np.random.random(np.shape(x)) < (1 - p)
    
    out = (x * mask) / (1 - p)
    return out, mask/(1-p)
    pass