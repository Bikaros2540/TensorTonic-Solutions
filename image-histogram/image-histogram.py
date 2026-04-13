def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    L = [0] * 256
    # If image is a list of lists, this treats it as a single sequence
    for row in image:
        for pixel in row:
            L[pixel] += 1
    return L