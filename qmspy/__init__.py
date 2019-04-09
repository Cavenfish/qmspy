"""
This is the qmspy module, a python module designed to automate graphing data
collected from a QMS.

Contains the following functions:
                init_data
                get_errs
                add_style

Contains the following submodules:
                graph_data


Author: Brian C. Ferrari
"""
import numpy as np
import pandas as pd

#Data Frame Columns
amu       =  'mass amu'
sem       =  'SEM Amps'
ev        =  'electron-energy V'
cyc       =  'Cycle'
col       =  'Color'
mar       =  'Marker'
std       =  'Standard Deviation'
