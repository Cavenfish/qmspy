from .config import *

def init_data(filled, background, error, savename='./Data.csv', sub=False):
    """
    This function reads in the QMS csv files and forms pandas DataFrames,
    it also preps the data.

    Parameters
    ----------
    filled: string
        This should be a string that points to the csv file of a
        gas-filled esweep. (FULL DIRECTORY STRING REQUIRED)
    background: string
        This should be a string that points to the csv file of a
        empty chamber esweep. (FULL DIRECTORY STRING REQUIRED)
    error: Pandas DataFrame
        This should be the output of the `get_errs()` function within
        `qmspy` module.
    savename: string [Optional, Default = './Data.csv']
        This should be a directory string that will be used to write
        the DataFrame csv to. (FULL DIRECTORY STRING REQUIRED)

    Returns
    -------
    data: Pandas DataFrame
        This is the DataFrame of the Initialized experimental data

    Example
    -------
    >>> import qmspy as qp
    >>>
    >>> filled     = './SomeFile1.csv'
    >>> background = './SomeFile2.csv'
    >>> error      = qp.get_errs(filled, None)
    >>>
    >>> data = qp.init_data(filled, background, error)
    >>>
    """
    #Read in CSV files with Pandas
    data = pd.read_csv(filled,     header=22)
    back = pd.read_csv(background, header=22)

    #Get Standard Deviation of data
    data = pd.read_csv(datafile, header=header)
    std = hi.groupby([ev, amu]).std()

    #Add in Standard Deviation Column
    error     = error.rename(index=str, columns={sem:std})
    error     = error.reset_index()
    data[std] = error[std]

    #Removes negative values from data and background
    data.update( data[sem].clip(0) )
    back.update( back[sem].clip(0) )

    #Drops data outside of first cycle
    data = data.loc[data[cyc] == 1]
    back = back.loc[back[cyc] == 1]

    #subtract background from data
    if sub is True:
        data[sem] -= back[sem]

    #Removes negative values from data and background again
    data.update( data[sem].clip(0) )
    back.update( back[sem].clip(0) )

    #Make all 0s np.nan (prevents them from being plotted)
    data = data.replace(0, np.nan)
    back = back.replace(0, np.nan)

    #Write csv file of data, so this function does not need to be called again
    data.to_csv(savename)

    return data
