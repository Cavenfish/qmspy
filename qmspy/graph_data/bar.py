
def bar(data, size):
    """
    """
    fig, ax = plt.subplots(figsize=size)
    data.plot.bar(y=sem, ax=ax, legend=None)
    return fig, ax
