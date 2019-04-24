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
from .config            import *

from .add_style         import add_style
from .get_errs          import get_errs
from .init_data         import init_data
from .integrate         import integrate
from .appearance_energy import appearance_energy

from .graph_data        import *
