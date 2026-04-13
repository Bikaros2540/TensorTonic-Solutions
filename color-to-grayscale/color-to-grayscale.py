def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    grey1 = [] 
    for row in image:
        grey2 = []
        for col in row:
            grey2.append(0.299*col[0]+0.587*col[1]+0.114*col[2])

        grey1.append(grey2)
    return grey1
        