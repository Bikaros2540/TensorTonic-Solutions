import numpy as np
def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    if not n_items:
        return 0.0
    a = []
    for r in recommendations:
        a = a + r
    a = set(a)
    l = len(a)
    return l*1.0/n_items
    