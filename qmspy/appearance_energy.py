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

    #Grabs only rows with 1 in peaks column
    temp = df.loc[df[pks] == 1]

    #Makes a list of uniques species of interest (species with data peaks)
    species_of_interest  = temp[amu].unique()

    energies={}
    for specie in species_of_interest:
        temp = df.loc[df[amu] == specie]

        z = np.polyfit(temp[sem], temp[ev], 3)
        f = np.poly1d(z)

        energies[specie] = f(0)


    return energies
