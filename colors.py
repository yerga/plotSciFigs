# -*- coding: utf-8 -*-
"""
colors.py
=========

A set of colors and color maps as provided by python package `palettable` (https://jiffyclub.github.io/palettable).

"""


from palettable.colorbrewer.qualitative import Set1_9
from cycler import cycler

almost_black = '#262626'

brewer_set1 = Set1_9.mpl_colors
# Remove the sixth color (yellow) which is too bright
brewer_set1.pop(5)
# Swap the red and blue to let blue come first
brewer_set1[0], brewer_set1[1] = brewer_set1[1], brewer_set1[0]
# Add a decent black color to this list
brewer_set1.append(almost_black)


default_color_cycler = cycler('color', brewer_set1)