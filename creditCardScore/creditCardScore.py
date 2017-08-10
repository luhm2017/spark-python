from numpy.ma import exp


def sigmoid(inX):
    """

    :type inX: object
    """
    return 1.0/(1+exp(-inX))