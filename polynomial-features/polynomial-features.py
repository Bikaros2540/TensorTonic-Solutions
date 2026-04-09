def pol(x,t):
    l = 1
    a =[1]
    
    for i in range(t):
        l *= x
        a.append(l)
    return a
def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    a = []
    for i in values:
        a.append(pol(i,degree))
    return a
