import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    y, p = np.array(y_true), np.array(y_pred)
    p = np.clip(p, eps, 1 - eps)
    return list(-(y*np.log(p)+(1-y)*np.log(1-p)))
    pass