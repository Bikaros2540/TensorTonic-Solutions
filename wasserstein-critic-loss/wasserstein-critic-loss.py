import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    r ,f = np.array(real_scores, dtype=np.float64), np.array(fake_scores, \
                                                             dtype=np.float64) 
    return np.mean(f)-np.mean(r)
    pass