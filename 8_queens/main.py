def make_board(queen_rows: list) -> tuple[list, list]:
    """
    Creating chess board with the queen positions given as a list,
    returns the chess board and the queen positions
    """
    
    # chess board
    # initially all are 0s
    chess_board: list = [[0 for _ in range(8)] for _ in range(8)]

    # queen positions
    queen_positions: list = []


    # adding queens
    for col, row in enumerate(queen_rows):
        # change the queen positions to 1
        chess_board[row][col] = 1

        # adding the queen postions in the list
        queen_positions.append([row, col])

    return chess_board, queen_positions



def attacking(queen_positions):
    """
    Calculating the pair of attacking queens
    """
    
    # to track if the attacking pair occurs multiple times
    attacking_set: list = []

    # store the pairs
    attacking_pairs: list = []
    
    for pos_1 in queen_positions:
        for pos_2 in queen_positions:   # comparing each of the queen with each queens in the board
            if pos_1 != pos_2:          # except one compairing oneself

                # if the reverse of the pair not in the list
                # then add the pair the attacking set else don't
                if [pos_2, pos_1] not in attacking_set:

                    # two queens attack each other
                    # if two queens are on same row or they are on the diagonal
                    is_same_row: bool = pos_1[0] == pos_2[0]                        
                    is_diagonal: bool = pos_1[0] - pos_2[0] == pos_1[1] - pos_2[1]  

                    # add to the attacking pair if they are attacking
                    if is_same_row or is_diagonal:
                        attacking_pairs.append([pos_1, pos_2])

                    attacking_set.append([pos_1, pos_2])

    return attacking_pairs



def print_board(chs_board: list) -> None:
    """
    Print the chess board
    """
    for row in chs_board:
        for col in row:
            print(col, end=' ')
        print()



if __name__ == '__main__':
    # columns are fixed
    # so we've only to define the rows
    # in this case the position of the element is the column position
    queen_position_rows = [6, 4, 2, 0, 5, 7, 1, 2]

    chess_board, queen_positions = make_board(queen_position_rows)
    attacking_pairs = attacking(queen_positions)

    print("The chess board:")
    print_board(chess_board)

    print(f"\nThere is(/are) {len(attacking_pairs)} pair(s) of queens attacking each other")
    
    print("\nThe pairs are: ")
    for pair in attacking_pairs:
        print(f"{pair[0]} x {pair[1]}")
