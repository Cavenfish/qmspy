
def scatter3d(data, size):
    """
    """
    fig = plt.figure(figsize=size)
    ax  = fig.add_subplot(111, projection='3d')
    ax.scatter(data[amu], data[ev], data[sem], c=data[col])
    ax.set_zscale('log')
    return fig, ax
