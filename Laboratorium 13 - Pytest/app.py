import numpy as np
from numpy.polynomial import polynomial as P
# zad1
def polly_A(x):
    """
    Funkcja wyznaczajaca współczynniki wielomianu przy znanym wektorze pierwiastków.
    """
    x = P.polyfromroots(x)
    return x
