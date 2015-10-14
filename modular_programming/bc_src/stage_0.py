#!/usr/bin/python
#
# First stage: loads spectrum from file

import matplotlib.pyplot as plt
import numpy as np

FILENAME = 'exemplo_espectro.txt'

# Loads spectrum into two separate vectors
X = np.loadtxt(FILENAME)
lamb = X[:, 0]
flux = X[:, 1]

# Visualizes the results
plt.plot(lamb, flux)
plt.show()
