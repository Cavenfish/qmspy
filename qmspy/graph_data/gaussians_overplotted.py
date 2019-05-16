from ..config import *

def gaussians_overplotted(data, savedir):
    """
    """
    df = check_data_type(data)

    #split DataFrame into actual data and gaussian data
    actual = df.loc[ev, amu, sem, std, pks]
    gaussi = df.loc[apk, gfx, gfy]

    i = 0
    for df, label in actual.groupby(ev):
        fig, ax = plt.subplots(figsize=size)

        df.plot(amu, sem, label=label, ax=ax)

        for j in #finish this later
