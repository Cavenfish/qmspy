from .config      import *
from scipy.signal import find_peak

def fit_gaussians(data, peaks):
    """
    ??????.

    Parameters
    ----------


    Returns
    -------


    Example
    -------

    """
    df = check_data_type(data)

    #split data up by electron energy
    for spectrum in df.groupby(ev):

        #find the peaks and their properties(width, and other lame stuff)
        peaks, properties = find_peak(spectrum[sem], width=1)

        #integrate over the peaks
