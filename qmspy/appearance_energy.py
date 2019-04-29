from .config import *

def appearance_energy(data, threshold):
    """
    This function finds the appearance energy of all amu species present in
    the data.

    Parameters
    ----------
    data: string or Pandas DataFrame
        This should be a string that points to the csv DataFrame file
        or a Pandas DataFrame. (FULL DIRECTORY STRING REQUIRED)
    threshold: numpy float
        This should be the value used as the threshold for determining the
        appearance energies.

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
        temp = specie.where(sem > threshold)
        temp.min()
