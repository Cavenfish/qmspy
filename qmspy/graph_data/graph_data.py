
def line(data, size, ls):
    """
    """
    fig, ax = plt.subplots(figsize=size)
    for label, df in data.groupby(amu):
        c    = df[col].iloc[1]
        m    = df[mar].iloc[1]
        yerr = df[std].iloc[1]
        df.plot(x=ev, y=sem, linestyle=ls, marker=m,
                c=c, yerr=std, ax=ax, label=label)

    return fig,ax

def bar(data, size):
    """
    """
    fig, ax = plt.subplots(figsize=size)
    data.plot.bar(y=sem, ax=ax, legend=None)
    return fig, ax

def scatter(data, size, hue=False):
    """
    """
    if hue is not False:
        hue = data[col]
    else:
        hue = None

    fig, ax = plt.subplots(figsize=size)
    sizes   = (20, 400)
    sb.scatterplot(data[ev], data[amu], size=data[sem],
                   hue=hue, sizes=sizes, legend=False, ax=ax)
    return fig, ax

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

def barx3d(data, size):
    """
    """
    i = len(data[ev])
    z = np.zeros(i)
    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.bar(data[amu], data[ev], zs=data[sem])
    return fig, ax

def line3d(data, size):
    """
    """
    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.plot(data[amu], data[ev], data[sem])
    return fig, ax

def scatter3d(data, size):
    """
    """
    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.scatter(data[amu], data[ev], data[sem], c=data[col])
    ax.set_zscale('log')
    return fig, ax
