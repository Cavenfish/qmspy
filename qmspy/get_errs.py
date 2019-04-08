import pandas as pd

def get_errs(datafile, header):
    """
    This fucntion gets the stadarad deviation of the QMS data given to it.

    Parameters
    ----------


    Returns
    -------


    Example
    -------

    """

    data = pd.read_csv(datafile, header=header)

    std = hi.groupby([ev, amu]).std()

    return std
