def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    for raw in X:
        n = len(raw)
        for col1 in range(n):
            for col2 in range(col1+1,n):
                raw.append(raw[col1]*raw[col2])
    return X