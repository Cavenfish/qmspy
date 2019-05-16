from .config      import *
from scipy.signal import find_peaks, peak_widths

def fit_gaussians(data, height, width,
                  savename='./Data-With-Gaussians.csv'):
    """
    Fits gaussians to the data peaks.

    Parameters
    ----------
    data: string or Pandas DataFrame
        This should be a string that points to the csv DataFrame file
        or a Pandas DataFrame. (FULL DIRECTORY STRING REQUIRED)
    height: float
        This should be the minimum value for data peak heights that will
        get a fitting.
    width: float
        This should be the minimum value for data peak widths that will
        get a fitting.
    savename: string [Optional, Default = './Data-With-Gaussians.csv']
        This should be a directory string that will be used to write
        the DataFrame csv to. (FULL DIRECTORY STRING REQUIRED)

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

    #initialize DataFrame for gaussian fits
    a   = []
    b   = []
    c   = []
    gao = pd.DataFrame(columns=[apk,gfx,gfy])

    #Arrays for interpolations
    fp = df[amu].unique().tolist()
    xp = range(len(fp))

    #iterate through peaks
    for i in range(len(peaks)):
        if (df.loc[peaks[i]][amu] < df.loc[peaks[i-1]][amu]) and (i is not 0):
            xp = range(max(xp)+1, max(xp)+1+len(xp))

        #The peak currently being worked on
        peak = peaks[i]

        #start point of gaussian df.loc[x_right][amu]
        x_left   = np.interp(full_widths[2][i]*0.95, xp, fp)

        #end point of gaussian df.loc[x_left][amu]
        x_right  = np.interp(full_widths[3][i]*1.1, xp, fp)

        #gaussian width
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

    #Make DataFrame
    gao[apk] = a
    gao[gfx] = b
    gao[gfy] = c

    #Merge DataFrames
    ret = pd.concat([df,gao], axis=1)

    #Write csv file of data
    ret.to_csv(savename)

    return ret
