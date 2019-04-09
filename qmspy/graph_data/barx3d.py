
def barx3d(data, size):
    """
    """
    i = len(data[ev])
    z = np.zeros(i)
    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.bar(data[amu], data[ev], zs=data[sem])
    return fig, ax
