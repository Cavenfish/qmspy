import qmspy as qp
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./Data_with_Style.csv')
size = (10,8)

fig, ax = qp.barx3d(data, size)
plt.show(fig)
