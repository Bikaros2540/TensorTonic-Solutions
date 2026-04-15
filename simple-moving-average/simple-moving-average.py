def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    SMA =[sum(values[:window_size])]
    for i in range(window_size,len(values)):
        SMA.append(SMA[-1]-values[i-window_size]+values[i])
    out=[c*1.0/window_size for c in SMA]
    return out
        