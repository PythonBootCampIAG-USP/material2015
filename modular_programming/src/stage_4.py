#!/usr/bin/python
#
# 5th stage: spectrum becomes an object
#
# Advantage: now the spectrum can be represented by a single variable.
#
# Q: Couldn't you just use a dictionary, i.e. spectrum["lamb"],
#    spectrum["flux"]??
# A: Sure! But here we are creating our own, expansible data type.
#    BTW dictionary is also a class.


import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

FILENAME = 'exemplo_espectro.txt'
LAMBDA_CUT_LEFT = 5000
LAMBDA_CUT_RIGHT = 9000
MAGNITUDE_OFFSET = -48.60


class Spectrum(object):
    def __init__(self):
        self.lamb = None
        self.flux = None


def load_spectrum(filename):
    # Loads spectrum into two separate vectors
    X = np.loadtxt(filename)
    output = Spectrum()
    output.lamb = X[:, 0]
    output.flux = X[:, 1]
    return output


def cut(input, lambda_left, lambda_right):
    # Cuts spectrum to region of interest

    # converts lambdas to vector indexes
    idx_cut_left = np.argmin(np.abs(input.lamb-lambda_left))
    idx_cut_right = np.argmin(np.abs(input.lamb-lambda_right))
    # cuts lambdas and fluxes
    output = Spectrum()
    output.lamb = input.lamb[idx_cut_left:idx_cut_right+1]
    output.flux = input.flux[idx_cut_left:idx_cut_right+1]
    return output


def to_magnitude(input, offset):
    # Converts flux to magnitude
    output = Spectrum()
    output.lamb = np.copy(input.lamb) # lambda vector is copied
    output.flux = -2.5 * np.log10(input.flux) + offset
    return output


# Applies the sequence
spectrum0 = load_spectrum(FILENAME)
spectrum1 = cut(spectrum0, LAMBDA_CUT_LEFT, LAMBDA_CUT_RIGHT)
spectrum2 = to_magnitude(spectrum1, MAGNITUDE_OFFSET)


# Visualizes the results
ax0 = plt.subplot(3, 1, 1)
plt.plot(spectrum0.lamb, spectrum0.flux)
ax = plt.gca()

plt.subplot(3, 1, 2, sharex=ax0)
plt.plot(spectrum1.lamb, spectrum1.flux)

plt.subplot(3, 1, 3, sharex=ax0)
plt.plot(spectrum2.lamb, spectrum2.flux)

plt.show()

