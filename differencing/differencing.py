def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    a = series
    for i in range(order):
        l = len(a)
        a1 = a + [0]
        a2 = [0] + a
        a3 = [x-y for x, y in zip(a1,a2)]
        a = a3[1:l]
    return a
        