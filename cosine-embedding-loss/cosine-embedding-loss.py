def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    ab = sum(a*b for a, b in zip(x1, x2)) 
    norm_a = math.sqrt(sum(a*a for a in x1))
    norm_b = math.sqrt(sum(b*b for b in x2))
    cos = ab/(norm_a*norm_b)
    if label == 1:
        return 1 - cos
    else:
        return max(0, cos -margin)