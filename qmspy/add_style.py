
def add_style(data, savename='./Data_with_Style.csv', clist=None, mlist=None):
    """
    This function adds a color and marker column to a Pandas DataFrame,
    then saves it as csv file.

    Parameters
    ----------
    data: string or Pandas DataFrame
        This should be a string that points to the csv DataFrame file
        or a Pandas DataFrame. (FULL DIRECTORY STRING REQUIRED)
    savename: string [Optional, Default = './Data_with_Style.csv']
        This should be a directory string that will be used to write
        the DataFrame csv to. (FULL DIRECTORY STRING REQUIRED)
    clist: list [Optional, Default = `Don't worry about it`]
        This should be a list where each element is a matplotlib
        color variable (ie: `red`)
    mlist: list [Optional, Default = `Don't worry about it`]
        This should be a list where each element is a matplotlib
        marker variable (ie: `+`)

    Returns
    -------
    df: Pandas DataFrame
        This is the DataFrame of the data with markers and colors columns.

    Example
    -------
    >>> import qmspy as qp
    >>>
    >>> data = './SomeFile.csv'
    >>>
    >>> df = qp.add_style(data)
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

    #If no color list given generate a default one
    if clist is None:
        listc = cycle(['k', 'g', 'y', 'c', 'm', 'r',
                       'lime', 'gold', 'coral', 'tan', 'purple', 'pink',
                       'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'])
    else:
        listc = cycle(clist)

    #If no marker list given generate a default one
    if mlist is None:
        listm = cycle(['o', 'o', 'o',
                       'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
                       '.', '^', '<', '>', '*', 'p', 'x', '+', '1'])
    else:
        listm = cycle(mlist)

    #Add Colors column to Data Frame
    cs      = [next(listc) for color in range(len(df))]
    ms      = [next(listm) for markr in range(len(df))]
    df[col] = cs
    df[mar] = ms


    #Write csv file of data, so this function does not need to be called again
    df.to_csv(savename)

    return df
