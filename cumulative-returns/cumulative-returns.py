def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    L=1
    out = []
    for i in returns:
        L *= (1+i)
        out.append(L-1)
    return out