#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Classify a list of stars"""

import my_functions

if __name__ == '__main__':

    list_of_stars = dict()
    ID = [8, 120, 165, 226]
    F606W = [28.1970, 20.8430, 27.0140, 30.1930]
    F814W = [27.1270, 19.8150, 26.0680, 28.2700]

    colors_indexes = my_functions.calculate_color_index(F606W, F814W)

    print('#{:>4s}{:>11s}{:>11s}{:>11s}'.format('ID', 'F606W', 'F814W', 'CI'))

    for i in range(len(colors_indexes)):

        print('{:5d} {:10.4f} {:10.4f} {:10.4f}'.format(
            ID[i],
            F606W[i],
            F814W[i],
            colors_indexes[i]
        ))

    print('All done!')
