import qmspy as qp

df = qp.fit_gaussians('./Data.csv', 1e-17, 0.2)

qp.graph_data.gaussians_overplotted(df, './figs/')
