__all__ = ["load_spectrum"]

from spectrum import *
import numpy as np

def load_spectrum(filename):
    # No need to document what is obvious; here I am not mentioning the
    # filename argument.
    """Loads spectrum file into two separate vectors."""
    X = np.loadtxt(filename)
    output = Spectrum()
    output.lamb = X[:, 0]
    output.flux = X[:, 1]
    return output

