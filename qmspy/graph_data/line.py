
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
