def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    n = len(values)
    l = window_size
    mean = [0]*(n-l+1)
    for i in  range(n-l+1):
        sp = sorted(values[i:i+l])
        mean[i] = (sp[l//2]+sp[(l-1)//2])/2.0
    return mean
        
        