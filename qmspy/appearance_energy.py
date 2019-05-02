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
    df = check_data_type(data)

    for specie in df.groupby(amu):
        if specie[pks] is 0:
            continue

    #still am not quite sure how to do this lol sucks to suck
