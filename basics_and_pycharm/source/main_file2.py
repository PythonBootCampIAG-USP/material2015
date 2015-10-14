#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Classify a list of stars"""

from my_functions import calculate_color_index as calc_color

if __name__ == '__main__':

    list_of_stars = dict()
    list_of_stars['ID'] = [8, 120, 165, 226]
    list_of_stars['F606W'] = [28.1970, 20.8430, 27.0140, 30.1930]
    list_of_stars['F814W'] = [27.1270, 19.8150, 26.0680, 28.2700]

    colors_indexes = calc_color(list_of_stars['F606W'], list_of_stars['F814W'])

    print('#{:>4s}{:>11s}{:>11s}{:>11s}'.format('ID', 'F606W', 'F814W', 'CI'))

    for i in range(len(colors_indexes)):

        print('{:3d} {:10.4f} {:10.4f} {:10.4f}'.format(
            list_of_stars['ID'][i],
            list_of_stars['F606W'][i],
            list_of_stars['F814W'][i],
            colors_indexes[i]
        ))

    print('All done!')
