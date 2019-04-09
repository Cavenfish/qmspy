
def line3d(data, size):
    """
    """
    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.plot(data[amu], data[ev], data[sem])
    return fig, ax
