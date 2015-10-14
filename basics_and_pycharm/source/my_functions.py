#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    My Functions

    File that will hold the functions that the 'main_file.py' and the
    'main_file2.py' are going to use.

    @author Bruno Quint
    @date   2015.10.13
    @version 0.1a
"""


def calculate_color_index(mag1, mag2):
    """
    Calculates the color index based on magnitude J and H.
    :param mag1: a list containing the magnitudes in one band.
    :type mag1: list
    :param mag2: a list containing the magnitudes in another band.
    :type mag2: list
    :return:
    """
    assert type(mag2) == list
    assert type(mag1) == list
    assert len(mag2) == len(mag1)

    temp_list = range(len(mag1))
    for i in range(len(mag1)):
        temp_list[i] = mag1[i] - mag2[i]

    return temp_list
