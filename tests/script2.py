import qmspy as qp

#Directory Strings
datadir0  =  '../CSV Files/2019-01-17/'
datadir1  =  '../CSV Files/2019-01-26/'
outdir0   =  './10e-6 Methane/'
outdir1   =  './1.50-1.51 e-7 Methane/'
outdir2   =  './1.43-1.45 e-8 Methane/'
outdir3   =  './1.10-1.45 e-9 Methane/'

#File Extensions
csv       =  '.csv'

#Data File Strings
empty0    = datadir0 + '10e-9 methane experiment background'    + csv
empty1    = datadir1 + '2.26e-10 esweep'                        + csv
filled0   = datadir0 + '10e-6 methane expriment run'            + csv
filled1   = datadir1 + 'filled chamber 1.50e-7--1.51e-7 esweep' + csv
filled2   = datadir1 + 'filled chamber 1.43e-8--1.45e-8 esweep' + csv
filled3   = datadir1 + 'filled chamber 1.10e-9--1.45e-9 esweep' + csv

#Get Standar deviation of high and low pressure runs
std0, std3 = qp.get_errs(filled0, filled3)

#Initialize data
data = qp.init_data(filled0, empty0, std0)

#Add Colors and Markers columns to DataFrame
df = qp.add_style(data)
