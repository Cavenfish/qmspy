import qmspy as qp
import pandas as pd
import matplotlib.pyplot as plt

#Data Frame Columns
amu       =  'mass amu'
sem       =  'SEM Amps'
ev        =  'electron-energy V'
cyc       =  'Cycle'
col       =  'Color'
mar       =  'Marker'
std       =  'Standard Deviation'

data = pd.read_csv('./Data.csv')
size = (10,8)

data0 = data.loc[data[ev] == 15]
data2 = data.loc[data[ev] == 25]
data4 = data.loc[data[ev] == 35]

data0 = data0.loc[data0[amu] <= 16]
data2 = data2.loc[data2[amu] <= 16]
data4 = data4.loc[data4[amu] <= 16]

data0 = data0.loc[data0[sem] > 0]
data2 = data2.loc[data2[sem] > 0]
data4 = data4.loc[data4[sem] > 0]

data0 = data0.set_index(amu)
data2 = data2.set_index(amu)
data4 = data4.set_index(amu)

fig, ax = qp.bar(data4, size)
plt.show(fig)
