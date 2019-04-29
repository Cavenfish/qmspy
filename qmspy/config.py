from itertools import cycle
import numpy as np
import pandas as pd
import sys

#Error Header and Tail
error_head = "\n*****uh oh spaghettios*****\n"
error_tail = "\n*****Ponder this, then return to me*****\n"

#Data Frame Columns
amu       =  'mass amu'
sem       =  'SEM Amps'
ev        =  'electron-energy V'
cyc       =  'Cycle'
col       =  'Color'
mar       =  'Marker'
std       =  'Standard Deviation'


def check_data_type(data):
    #Check if data is in CSV format
    if '.csv' in data:
        df = pd.read_csv(data)

    #Terminates function with error message if data format not acceptable
    elif type(data) is not type(pd.DataFrame()):
        print(error_head)
        print("Your data is not in CSV or Pandas DataFrame Format")
        print(error_tail)
        sys.exit()

    #If data already DataFrame format, changes its name to df
    else:
        df = data

    return df

def gaussian(x, a, x0, sigma):
    return a * np.exp( -(x - x0)**2 / (2 * sigma**2)  )
