import matplotlib.pyplot as plt
import numpy as np
import pandas
from matplotlib.table import Table


def checkerboard_table(data, bkg_colors=None):
    data = pandas.DataFrame(data,
                            columns=range(8))
    if bkg_colors is None:
        bkg_colors = ['black', 'white']
    fig, ax = plt.subplots()
    ax.set_axis_off()

    tb = Table(ax, bbox=[0, 0, 1, 1])

    nrows = ncols = 8

    width, height = 1.0 / ncols, 1.0 / nrows

    # Add cells
    for (i, j), val in np.ndenumerate(data):
        # Index either the first or second item of bkg_colors based on
        # a checker board pattern
        idx = [j % 2, (j + 1) % 2][i % 2]
        color = bkg_colors[idx]
        c = 'white' if bkg_colors[idx] == 'black' else 'black'

        tb.add_cell(i, j, width, height, text="♛" if val == 1 else '',
                    loc='center', facecolor=color).set_text_props(c=c)

    # Row Labels...
    for i, label in enumerate(data.index):
        tb.add_cell(i, -1, width, height, text=label, loc='right',
                    edgecolor='none', facecolor='none')
    # Column Labels...
    for j, label in enumerate(data.columns):
        tb.add_cell(-1, j, width, height / 2, text=label, loc='center',
                    edgecolor='none', facecolor='none')
    ax.add_table(tb)
    plt.show()
    return fig
