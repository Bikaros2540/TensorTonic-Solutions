def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    n = len(values)
    M = max(values)
    m = min(values)
    w = (M - m)*1.0/ num_bins
    if  not w:
        return [0]*n
    for i in range(n):
        values[i]= min(int((values[i] - m) / w), num_bins - 1)
    return values