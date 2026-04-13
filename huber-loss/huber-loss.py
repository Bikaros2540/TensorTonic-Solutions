import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y, y_pred = np.array(y_true), np.array(y_pred)
    e = y-y_pred
    nor =np.abs(e)
    loss = np.where(nor <= delta, 0.5 * e**2, delta * (nor - 0.5 * delta))
    return np.mean(loss)