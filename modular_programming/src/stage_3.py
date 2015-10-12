#!/usr/bin/python
#
# 4th stage: def's
#
# Advantage: a library is born!

import matplotlib.pyplot as plt
import numpy as np

FILENAME = 'exemplo_espectro.txt'
LAMBDA_CUT_LEFT = 5000
LAMBDA_CUT_RIGHT = 9000
MAGNITUDE_OFFSET = -48.60


def load_spectrum(filename):
    # Loads spectrum into two separate vectors
    X = np.loadtxt(filename)
    lamb = X[:, 0]
    flux = X[:, 1]
    return lamb, flux


def cut(lamb, flux, lambda_left, lambda_right):
    # Cuts spectrum to region of interest

    # converts lambdas to vector indexes
    idx_cut_left = np.argmin(np.abs(lamb-lambda_left))
    idx_cut_right = np.argmin(np.abs(lamb-lambda_right))
    # cuts lambdas and fluxes
    lamb_1 = lamb[idx_cut_left:idx_cut_right+1]
    flux_1 = flux[idx_cut_left:idx_cut_right+1]
    return lamb_1, flux_1


def to_magnitude(lamb, flux, offset):
    # Converts flux to magnitude
    lamb_2 = np.copy(lamb) # lambda vector is copied
    flux_2 = -2.5 * np.log10(flux) + offset
    return lamb_2, flux_2


# Applies the sequence
lamb, flux = load_spectrum(FILENAME)
lamb_1, flux_1 = cut(lamb, flux, LAMBDA_CUT_LEFT, LAMBDA_CUT_RIGHT)
lamb_2, flux_2 = to_magnitude(lamb_1, flux_1, MAGNITUDE_OFFSET)


# Visualizes the results
ax0 = plt.subplot(3, 1, 1)
plt.plot(lamb, flux)
ax = plt.gca()

plt.subplot(3, 1, 2, sharex=ax0)
plt.plot(lamb_1, flux_1)

plt.subplot(3, 1, 3, sharex=ax0)
plt.plot(lamb_2, flux_2)

plt.show()

