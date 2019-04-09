
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
