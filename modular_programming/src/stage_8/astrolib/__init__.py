"""
This packages contains tools to manipulate spectra.
"""

__all__ = ["Spectrum", "load_spectrum", "Cutter", "ToMagnitude"]

import numpy as np


class Spectrum(object):
    """Class to represent a spectrum."""
    def __init__(self):
        self.lamb = None
        self.flux = None


def load_spectrum(filename):
    # No need to document what is obvious; here I am not mentioning the
    # filename argument.
    """Loads spectrum file into two separate vectors."""
    X = np.loadtxt(filename)
    output = Spectrum()
    output.lamb = X[:, 0]
    output.flux = X[:, 1]
    return output


class Cutter(object):
    # Description of the arguments passed to __init__() go at the
    # class docstring
    """Cuts spectrum to region specified by a wavelength interval.

    Arguments:
      lambda_left -- initial wavelength
      lambda_right -- final wavelength
    """
    def __init__(self, lambda_left, lambda_right):
        self.lambda_left = lambda_left
        self.lambda_right = lambda_right

    def apply(self, input):
        # converts lambdas to vector indexes
        idx_cut_left = np.argmin(np.abs(input.lamb - self.lambda_left))
        idx_cut_right = np.argmin(np.abs(input.lamb - self.lambda_right))
        # cuts lambdas and fluxes
        output = Spectrum()
        output.lamb = input.lamb[idx_cut_left:idx_cut_right+1]
        output.flux = input.flux[idx_cut_left:idx_cut_right+1]
        return output


class ToMagnitude(object):
    """Converts flux to magnitude.

    Arguments:
      offset -- see formula

    Formula: magniture = -2.5 * log10(flux) + offset

    The formula is applied to all elements in flux vector.
    """
    def __init__(self, offset):
        self.offset = offset

    def apply(self, input):
        # Converts flux to magnitude
        output = Spectrum()
        output.lamb = np.copy(input.lamb) # lambda vector is copied
        output.flux = -2.5 * np.log10(input.flux) + self.offset
        return output

