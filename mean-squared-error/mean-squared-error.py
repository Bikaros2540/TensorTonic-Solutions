import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    n= len(y_pred)
    y_pred, y_true = np.array(y_pred), np.array(y_true)
    MSE = sum((y_pred-y_true)**2)/n*1.0 
    return MSE
    pass
