import numpy as np
from tabulate import tabulate


# Get 'X' and 'O' at random positions
def get_positions():   
    x_pos = np.random.randint(9)
    o_pos = np.random.randint(9)

    # check if two positions are same
    if x_pos == o_pos:
        if o_pos == 0:      # edge case number 1
            x_pos = np.random.randint(1, 9)
        elif o_pos == 8:    # edfe case number 2
            x_pos = np.random.randint(8)
        else:
            first = np.random.randint(o_pos)
            second = np.random.randint(o_pos + 1, 9)
            x_pos = [first, second][np.random.randint(2)]

    return x_pos, o_pos


def convert_row_col(positions, player):
    x_pos, o_pos = positions
    if player == 2: 
        row, col = x_pos // 3, x_pos % 3
    elif player == 1:
        row, col = o_pos // 3, o_pos % 3
    return row, col


# create a board
def board(positions):
    """
    2 means X
    1 means O
    """
    x_row, x_col = convert_row_col(positions, 2)
    o_row, o_col = convert_row_col(positions, 1)
    
    board = np.zeros((3, 3))
    board[x_row][x_col] = 2
    board[o_row][o_col] = 1

    board_ = []
    for i in board:
        row = []
        for j in i:
            if j == 2:
                row.append('X')
            elif j == 1:
                row.append('O')
            else:
                row.append('_')
        board_.append(row)

    print(tabulate(board_, tablefmt='grid'))


    

# Check if they are on the same row
def same_row(positions):    
    return 0 if convert_row_col(positions, 2)[0] == convert_row_col(positions, 1)[0] else 1


# Check if they are on the same column
def same_col(positions):    
    return 0 if convert_row_col(positions, 2)[1] == convert_row_col(positions, 1)[1] else 1


# Check if they are on the same diagonal
def same_diagonal(positions, player):
    x_row, x_col = convert_row_col(positions, 2)
    o_row, o_col = convert_row_col(positions, 1)

    if player == 'X':
        player_row, player_col = convert_row_col(positions, 2)
        other_player_row, other_player_col = convert_row_col(positions, 1)
    elif player == 'O':
        player_row, player_col = convert_row_col(positions, 1)
        other_player_row, other_player_col = convert_row_col(positions, 2)
        

    if player_row == player_col and player_row != 1:
        return 0 if other_player_row == other_player_col else 1
    
    elif player_row == player_col and player_row == 1:
        if other_player_row == other_player_col or abs(other_player_row - other_player_col) == 2:
            return 1
        else:
            return 2
            
    elif abs(player_row - player_col) == 2:
        return 0 if abs(other_player_row - other_player_col) == 2 or other_player_row == other_player_col  else 1
    else:
        return 0


def evaluate_winning(player):
    postns = get_positions()
    board(postns)
    row_wise_win = same_row(postns)
    col_wise_win = same_col(postns)
    
    x_diag_wise_win = same_diagonal(postns, 'X')
    o_diag_wise_win = same_diagonal(postns, 'O')
    
    x_total_winning = row_wise_win + col_wise_win + x_diag_wise_win
    o_total_winning = row_wise_win + col_wise_win + o_diag_wise_win

    if player == 'X':
        if x_total_winning > o_total_winning:
            return 'favourable'
        elif x_total_winning == o_total_winning:
            return 'chances are equal for both'
        else:
            return 'not favourable'
    elif player == 'O':
        if o_total_winning > x_total_winning:
            return 'favourable'
        elif o_total_winning == x_total_winning:
            return 'chances are equal for both'
        else:
            return 'not favourable'


if __name__ == "__main__":
    print(f"The position of player X indicates: {evaluate_winning('X')}")
