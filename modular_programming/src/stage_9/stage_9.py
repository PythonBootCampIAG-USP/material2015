#!/usr/bin/python
#
# 10th stage: no change in main file from 9th stage

import matplotlib.pyplot as plt
import numpy as np
from astrolib import *

FILENAME = '../exemplo_espectro.txt'
LAMBDA_CUT_LEFT = 5000
LAMBDA_CUT_RIGHT = 9000
MAGNITUDE_OFFSET = -48.60

# creates sequence
sequence = [Cutter(LAMBDA_CUT_LEFT, LAMBDA_CUT_RIGHT),
            ToMagnitude(MAGNITUDE_OFFSET)
            ]

# loads spectrum
input = load_spectrum(FILENAME)

# applies operations
spectra = [input]
for operation in sequence:
    output = operation.apply(input)
    spectra.append(output)
    input = output

# visualizes the results
num_plots = len(spectra)

for i in range(num_plots):
    if i == 0:
        ax = plt.subplot(num_plots, 1, i+1)
        reference_axis = ax # if first plot, saves reference axis
                            # to link to it later (below)
    else:
        ax = plt.subplot(num_plots, 1, i+1, sharex=ax)

    spectrum = spectra[i]
    plt.plot(spectrum.lamb, spectrum.flux)
plt.show()

