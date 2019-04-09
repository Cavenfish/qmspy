"""
This is the data graphing submodule of the QMS package, it houses all the
data plotting functions.

Contains the following functions:
                line
                line3d
                bar
                barx3d
                scatter
                scatter3d
                contour



Author: Brian C. Ferrari
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

#Data Frame Columns
amu       =  'mass amu'
sem       =  'SEM Amps'
ev        =  'electron-energy V'
cyc       =  'Cycle'
col       =  'Color'
mar       =  'Marker'
std       =  'Standard Deviation'
