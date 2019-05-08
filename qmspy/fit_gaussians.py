from .config      import *
from scipy.signal import find_peaks
from scipy.signal import gaussian

def fit_gaussians(data, height, width):
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
    peaks, properties = find_peaks(df[sem], height=height, width=width)

    #Add peaks column to DataFrame
    temp        = np.zeros(len(df[sem]))
    temp[peaks] = 1
    df[pks]     = temp

    #initialize some counter and gao==array for gaussian fit values
    i   = 0
    gao = np.zeros(len(df[sem]))

    #interate through peaks
    for peak in peaks:
        left   = int(round(properties['left_ips'][i] ) ) #left point of gaussian
        right  = int(round(properties['right_ips'][i]) ) #right point of gaussian
        length = right - left                       #length of gaussian
        width  = properties['widths'][i]            #gaussian width

        #generate gaussian curve fit to peak data
        gaus   = gaussian(length, width) * properties['peak_heights'][i]

        #plug generated gaussian into gao array then increment counter
        gao[left:right] = gaus
        i+=1

    #Add gaussian fits column to dataframe
    df[gau] = gao

    return df
