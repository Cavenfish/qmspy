from .config import *
from scipy.optimize import curve_fit

def appearance_energy(data):
    """
    This function finds the appearance energy of all amu species present in
    the data by means of linear fit.

    Parameters
    ----------
    data: string or Pandas DataFrame
        This should be a string that points to the csv DataFrame file
        or a Pandas DataFrame. (FULL DIRECTORY STRING REQUIRED)

    Returns
    -------
    energies: list
        This will be a list where each element is string with the amu
        energy in the following format 'amu: energy'


    Example
    -------

    """
    df   = check_data_type(data)

    #Grab species of interest
    soi = species_of_interest(df)

    #initialize a dictionary for appearance energies
    energies={}

    #iterate through each species of interest
    for specie in soi:

        #slice the DataFrame so that it only has rows with amu value
        #equal to the specie of interest
        temp = df.loc[df[amu] == specie]

        #Perform a polynomial fitting to the entire data-set
        z = np.polyfit(temp[ev], temp[sem], 6)
        f = np.poly1d(z) #this is the fitting function

        #x-range to later interpolate the x-intercept
        x = np.arange(8,20)

        #interpolate the x-intercept and add it to the dictionary
        energies[specie] = np.interp(0, f(x), x)

    return energies
