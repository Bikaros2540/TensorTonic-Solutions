import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x, dtype=np.float64)
    mean, median, mode = np.mean(x), np.median(x), Counter(x).most_common(1)[0][0]
    return mean, median, mode
    pass