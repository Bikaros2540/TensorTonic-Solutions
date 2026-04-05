import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    X, y = np.array(X), np.array(y)
    N,D = np.shape(X)
    XT = X.T
    w = np.zeros(D,)
    b = 0.0
    for i in range(steps):
        p_y = _sigmoid(X@w+b)-y
        w = w - lr*XT@p_y/N
        b= b - lr*np.mean(p_y)
    return (w,b)
    
    
    # Write code here
    pass