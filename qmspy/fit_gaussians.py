from .config      import *
from scipy.signal import find_peaks
from scipy.signal import gaussian

def fit_gaussians(data, peaks):
    """
    Fits gaussians to the data peaks.

    Parameters
    ----------


    Returns
    -------


    Example
    -------

    """
    df = check_data_type(data)

    #find peaks and preperties(widths) in data
    peaks, properties = find_peaks(df[sem], height=1e-16, width=5)

    #Add peaks column to DataFrame
    df[pks]            = 0
    df.loc[peaks][pks] = 1

    #Add gaussian fits column to dataframe
    i   = 0
    gao = np.zeros(len(df[sem]))
    for peak in peaks:
        left   = properties['left_ips'][i]
        right  = properties['right_ips'][i]
        length = int(right - left)
        width  = properties['widths'][i]
        gaus   = gaussian(length, width) * properties['peak_heights'][i]

        gao[left:right] = gaus
        i+=1

    df[gau] = gao

    return df
