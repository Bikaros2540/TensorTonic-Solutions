import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    """
    Perform one Nesterov Momentum update step.
    """
    w, v, grad = np.array(w), np.array(v), np.array(grad)
    #w = w - momentum*v
    v = momentum*v +lr*grad
    w = w - v
    return w, v