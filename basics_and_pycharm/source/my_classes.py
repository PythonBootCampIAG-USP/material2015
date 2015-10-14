#!#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    My Classes

    File that will hold the class used on 'main_file3.py'.

    @author Bruno Quint
    @date   2015.10.13
    @version 0.1a
"""


class Star:

    def __init__(self, mag_J, mag_H):
        """
        Object constructor that receives the magnitude on V band and on R band.
        """
        self.mag_J = mag_J
        self.mag_H = mag_H

        return

    def calculate_color_index(self):
        """
        Calculates the color index based on magnitude J and H.
        """
        return self.mag_J - self.mag_H
