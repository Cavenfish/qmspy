
def contour(data, size):
    """
    """
    fig, ax = plt.subplots(figsize=size)
    data = data.pivot(index=ev, columns=amu, values=sem)
    data.fillna(1e-20, inplace=True)
    log_norm = LogNorm(vmin=data.min().min(), vmax=data.max().max())
    ticks = {"ticks":[0,1e-19,1e-18,1e-17,1e-16,1e-15,1e-14,1e-13,1e-12]}
    sb.heatmap(data, norm=log_norm, cbar_kws=ticks, ax=ax)
    return fig, ax
