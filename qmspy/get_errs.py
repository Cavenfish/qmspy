import pandas as pd

def get_errs(high, low):
    """
    """
    #Data Frame Columns
    amu       =  'mass amu'
    sem       =  'SEM Amps'
    ev        =  'electron-energy V'
    cyc       =  'Cycle'

    hi = pd.read_csv(high, header=22)
    lo = pd.read_csv(low,  header=22)

    stdhi = hi.groupby([ev, amu]).std()
    stdlo = lo.groupby([ev, amu]).std()

    avgstd = (stdhi[sem] + stdlo[sem]) / 2

    return stdhi, stdlo
