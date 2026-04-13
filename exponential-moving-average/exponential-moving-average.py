def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    EMA = [values[0]]
    for v in values[1:]:
        EMA.append(alpha*v+ (1-alpha)*EMA[-1])
    return EMA