import matplotlib.pyplot as plt
import numpy as np
import pandas
from main import *
from matplotlib.table import Table


def main():
    queen_position_rows = [6, 4, 2, 0, 5, 7, 1, 2]

    chess_board = make_board()
    add_queens(chess_board, queen_position_rows)
    queen_positions = get_queen_positions(chess_board)
    attacking_pairs = attacking(is_attacking(queen_positions))

    
    data = pandas.DataFrame(chess_board, 
                columns=range(8))
    checkerboard_table(data)
    plt.show()

def checkerboard_table(data, bkg_colors=['black', 'white']):
    fig, ax = plt.subplots()
    ax.set_axis_off()

    tb = Table(ax, bbox=[0,0,1,1])

    nrows = ncols = 8

    width, height = 1.0 / ncols, 1.0 / nrows

    # Add cells
    for (i,j), val in np.ndenumerate(data):
        # Index either the first or second item of bkg_colors based on
        # a checker board pattern
        idx = [j % 2, (j + 1) % 2][i % 2]
        color = bkg_colors[idx]
        c = 'white' if bkg_colors[idx] == 'black' else 'black'

        tb.add_cell(i, j, width, height, text="♛" if val == 1 else '', 
                    loc='center', facecolor=color).set_text_props(c=c, fontsize='xx-large')

        
        

    # Row Labels...
    for i, label in enumerate(data.index):
        tb.add_cell(i, -1, width, height, text=label, loc='right', 
                    edgecolor='none', facecolor='none')
    # Column Labels...
    for j, label in enumerate(data.columns):
        tb.add_cell(-1, j, width, height/2, text=label, loc='center', 
                           edgecolor='none', facecolor='none')
    ax.add_table(tb)
    return fig

if __name__ == '__main__':
    main()
