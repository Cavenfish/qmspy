from .config      import *
from scipy.signal import find_peaks, peak_widths

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
    half_widths       = peak_widths(df[sem], peaks, rel_height=0.5)[0]
    full_widths       = peak_widths(df[sem], peaks, rel_height=1)[0]

    #Add peaks column to DataFrame
    temp        = np.zeros(len(df[sem]))
    temp[peaks] = 1
    df[pks]     = temp

    #initialize a counter and DataFrame for gaussian fits
    i   = 0
    a   = []
    b   = []
    c   = []
    gao = pd.DataFrame(columns=[apk,gfx,gfy])

    #iterate through peaks
    for peak in peaks:
        #start point of gaussian
        x_left   = int( peak - full_widths[i]/2 )
        #end point of gaussian
        x_right  = int( peak + full_widths[i]/2 )
        #start of gaussian half width
        width_left = int( peak - half_widths[i]/2 )
        #right side of gaussian half width
        width_right = int( peak + half_widths[i]/2 )
        #gaussian width
        width  = (df.loc[width_right][amu] - df.loc[width_left][amu])
        #gaussian height
        height = df.loc[peak][sem]
        #gaussian x values
        x_values = np.linspace(df.loc[x_left][amu],
                               df.loc[x_right][amu],120)

        #generate gaussian curve fit to peak data
        gaus   = gaussian(x_values, df.loc[peak][amu], width, height)

        #plug generated gaussian into temp lists then increment counter
        a.extend(np.ones(len(x_values)) *df.loc[peak][amu])
        b.extend(x_values)
        c.extend(gaus)
        i+=1

    #Make DataFrame
    gao[apk] = a
    gao[gfx] = b
    gao[gfy] = c

    #Merge DataFrames
    ret = pd.concat([df,gao], axis=1)

    return ret
