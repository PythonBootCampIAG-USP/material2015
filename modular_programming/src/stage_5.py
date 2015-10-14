#!/usr/bin/python
#
# 6th stage: all operations become classes
#
# Advantage: all operations now have the same "interface", i.e.,
#   an operation is applied by calling: output = operation.apply(input)
#   regardless of the class of the operation.

import matplotlib.pyplot as plt
import numpy as np

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


class Cutter(object):
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
    def __init__(self, offset):
        self.offset = offset

    def apply(self, input):
        # Converts flux to magnitude
        output = Spectrum()
        output.lamb = np.copy(input.lamb) # lambda vector is copied
        output.flux = -2.5 * np.log10(input.flux) + self.offset
        return output


# --- Applies the sequence ---

# creates objects
operation_0 = Cutter(LAMBDA_CUT_LEFT, LAMBDA_CUT_RIGHT)
operation_1 = ToMagnitude(MAGNITUDE_OFFSET)
# acts
spectrum0 = load_spectrum(FILENAME)
spectrum1 = operation_0.apply(spectrum0)
spectrum2 = operation_1.apply(spectrum1)


# Visualizes the results
ax0 = plt.subplot(3, 1, 1)
plt.plot(spectrum0.lamb, spectrum0.flux)
ax = plt.gca()

plt.subplot(3, 1, 2, sharex=ax0)
plt.plot(spectrum1.lamb, spectrum1.flux)

plt.subplot(3, 1, 3, sharex=ax0)
plt.plot(spectrum2.lamb, spectrum2.flux)

plt.show()

