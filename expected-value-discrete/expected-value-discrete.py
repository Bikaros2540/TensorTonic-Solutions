import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if not np.allclose(1,np.sum(p),rtol=0, atol=1e-08):
        raise ValueError(" props don't add to one")
    if np.size(x) == np.size(p):
        return np.inner(x, p)
    pass
