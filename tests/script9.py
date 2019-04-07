import qmspy as qp
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./Data.csv')
size = (10,8)

fig, ax = qp.scatter(data, size)
plt.show(fig)
