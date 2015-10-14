#!/usr/bin/python
#
# 3rd stage: converts flux to magnitude

import matplotlib.pyplot as plt
import numpy as np

FILENAME = 'exemplo_espectro.txt'
LAMBDA_CUT_LEFT = 5000
LAMBDA_CUT_RIGHT = 9000
MAGNITUDE_OFFSET = -48.60

# Loads spectrum into two separate vectors
X = np.loadtxt(FILENAME)
lamb = X[:, 0]
flux = X[:, 1]


# --- Step 0 --- Cuts spectrum to region of interest
# converts lambdas to vector indexes
idx_cut_left = np.argmin(np.abs(lamb-LAMBDA_CUT_LEFT))
idx_cut_right = np.argmin(np.abs(lamb-LAMBDA_CUT_RIGHT))
# cuts lambdas and fluxes
lamb_1 = lamb[idx_cut_left:idx_cut_right+1]
flux_1 = flux[idx_cut_left:idx_cut_right+1]


# --- Step 1 --- Converts flux to magnitude
lamb_2 = np.copy(lamb_1) # lambda vector is copied
flux_2 = -2.5 * np.log10(flux_1) + MAGNITUDE_OFFSET


# Visualizes the results
ax0 = plt.subplot(3, 1, 1)
plt.plot(lamb, flux)
ax = plt.gca()

plt.subplot(3, 1, 2, sharex=ax0)
plt.plot(lamb_1, flux_1)

plt.subplot(3, 1, 3, sharex=ax0)
plt.plot(lamb_2, flux_2)

plt.show()

