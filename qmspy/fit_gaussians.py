from .config      import *
from scipy.signal import find_peaks, peak_widths
from scipy.optimize import curve_fit
import matplotlib.animation as ani

def fit_gaussians(data, height, width, savedir='./', overplot=False,
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

    #Initialize new columns
    df[pks] = np.nan
    df[gfs] = np.nan

    for label, subDF in df.groupby(ev):
        subDF = subDF.reset_index()

        #find peaks and preperties(widths) in data
        peaks, properties = find_peaks(subDF[sem], height=height, width=width,
                                       distance=10)
        half_widths       = peak_widths(subDF[sem], peaks, rel_height=0.5)
        full_widths       = peak_widths(subDF[sem], peaks, rel_height=1)

        #Add peaks column to DataFrame
        temp        = np.zeros(len(subDF[sem]))
        temp[peaks] = 1
        subDF[pks]  = temp

        #Iterate trough peak indexes
        for peak in peaks:
            #Get min and max index of subDataFrame
            imin, imax = subDF.index[0], subDF.index[-1]

            #Make sure a&b are within subDataFrame index
            a = peak-10
            b = peak+10
            if a < imin:
                a = imin
            if b > imax:
                b = imax

            #Slice x,y region for gaussian fitting
            x = subDF[amu].iloc[a:b].values
            y = subDF[sem].iloc[a:b].values

            #Fit Gaussian, then get sum
            mu0        = subDF[amu].iloc[peak]
            h0         = subDF[sem].iloc[peak]
            p0         = [mu0, 1, h0]
            popt, pcov = curve_fit(gaussian, x, y,p0=p0, maxfev=2000000000)
            gfitx      = np.arange(min(x), max(x), 0.001)
            gfity      = gaussian(gfitx, *popt)
            area       = popt[2]*popt[1]*np.sqrt(2.*np.pi)

            #Replace 1's in temp with sums
            temp[peak] = area

            #Make graph for this overplot
            if overplot is True:
                plt.plot(x,y, '.')
                plt.plot(gfitx,gfity,'--')
                plt.savefig(savedir+str(label)+'--'+str(mu0)+'.png')
                plt.close()

        #Add Gaussian integrations into Dataframe
        subDF[gfs] = temp

        #Update main DataFrame with sub-DataFrame
        df[pks].update(subDF[pks])
        df[gfs].update(subDF[gfs])

    #Write csv file of data
    df.to_csv(savename)

    return df
