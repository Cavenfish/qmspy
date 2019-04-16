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
from itertools import cycle
import numpy as np
import pandas as pd

from .add_style  import add_style
from .get_errs   import get_errs
from .init_data  import init_data
from .integrate  import integrate
from .graph_data import *


#Error Header and Tail
error_head = "\n*****uh oh spaghettios*****\n"
error_tail = "\n*****Ponder this, then return to me*****\n"

#Data Frame Columns
amu       =  'mass amu'
sem       =  'SEM Amps'
ev        =  'electron-energy V'
cyc       =  'Cycle'
col       =  'Color'
mar       =  'Marker'
std       =  'Standard Deviation'
