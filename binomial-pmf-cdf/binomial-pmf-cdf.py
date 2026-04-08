import numpy as np
from scipy.special import comb

def PMF (n, p, k):
    return float(comb(n,k)*(p**k)*(1 - p)**(n-k))

    
def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    
    """
    CDF = 0.0
    for i in range(k+1):
        CDF += PMF(n,p,i)
    return  PMF(n,p,k), CDF
        
    pass