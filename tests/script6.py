import qmspy as qp
import matplotlib.pyplot as plt

#Directory Strings
emptydir =  '../CSV Files/2019-02-09/'
datadir  =  '../CSV Files/2019-02-10/'

#File Extensions
csv       =  '.csv'

#Data File Strings
empty      = emptydir + '1.11--1.38e-10 empty esweep'    + csv
filledlo   = datadir  + '1.15--1.20e-6 filled esweep'    + csv
filledhi   = emptydir + '1.15--1.20e-9 filled esweep'    + csv

#Get Standar deviation of high and low pressure runs
stdlo, stdhi = qp.get_errs(filledlo, filledhi)

#Initialize data
datalo = qp.init_data(filledlo, empty, stdlo)
datahi = qp.init_data(filledhi, empty, stdhi)

#Make heatmaps
size        = (10,8)
figlo, axlo = qp.contour(datalo, size)
fighi, axhi = qp.contour(datahi, size)

#Save figures
figlo.savefig('Low')
fighi.savefig('High')
