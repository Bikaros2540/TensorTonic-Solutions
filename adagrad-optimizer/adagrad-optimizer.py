import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    w, g, G = np.array(w), np.array(g), np.array(G)
    G = G + g**2
    w = w - lr*g/np.sqrt(G+eps)
    return w, G
    pass