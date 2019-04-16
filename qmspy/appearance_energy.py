
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
    #Check if data is in CSV format
    if '.csv' in data:
        df = pd.read_csv(data)

    #Terminates function with error message if data format not acceptable
    elif type(data) is not type(pd.DataFrame()):
        print(error_head)
        print("Your data is not in CSV or Pandas DataFrame Format")
        print(error_tail)
        return

    #If data already DataFrame format, changes its name to df
    else:
        df = data

    for specie in df.groupby(amu):
        temp = specie.where(sem > threshold)
        temp.min()
