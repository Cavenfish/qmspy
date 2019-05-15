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
    half_widths       = peak_widths(df[sem], peaks, rel_height=0.5)
    full_widths       = peak_widths(df[sem], peaks, rel_height=1)

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


#The problem right now is how im storing the Gaussian Fits data
#Since it is longer than original data, groupby ev does not work
#can groupby differently but would be best to fix this

    xp = range(len(df))
    fp = df[amu].tolist()

    #iterate through peaks
    for peak in peaks:
        #start point of gaussian df.loc[x_right][amu]
        x_left   = np.interp(full_widths[2][i]*0.95, xp, fp)
        #end point of gaussian df.loc[x_left][amu]
        x_right  = np.interp(full_widths[3][i]*1.1, xp, fp)
        #right side of gaussian half width
        #width_right = int(half_widths[3][i])
        #gaussian width df.loc[width_right][amu]
        width  = (np.interp(half_widths[3][i], xp, fp)
                  - df.loc[peak][amu])
        #gaussian height
        height = df.loc[peak][sem]
        #shouldnt need it but i do
        if x_left < 0:
            x_left = 0
        #gaussian x values
        x_values = np.linspace(x_left, x_right, 120)

        #generate gaussian curve fit to peak data
        gaus   = gaussian(x_values, df.loc[peak][amu], width, height)

        #plug generated gaussian into temp lists then increment counter
        a.extend(np.ones(120) *df.loc[peak][amu])
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
