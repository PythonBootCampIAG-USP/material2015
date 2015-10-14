#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Classify a list of stars"""

import numpy as np
from my_classes import Star

if __name__ == '__main__':

    filename = 'list_of_stars.dat'
    table = np.loadtxt(filename, usecols=[0, 3, 5])

    for line in table:

        id = line[0]
        mag_J = line[1]
        mag_H = line[2]

        one_star = Star(mag_J, mag_H)
        print(id, one_star.calculate_color_index())
