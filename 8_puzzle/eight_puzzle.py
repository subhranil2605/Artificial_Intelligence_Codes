import numpy as np
from numpy import ndarray
from tabulate import tabulate


def shuffle_board(puzzle_board: ndarray) -> ndarray:
    """
    Shuffle the tiles
    
    """
    
    flatten_board: ndarray = puzzle_board.flatten() # 2D array to 1D array
    perm: ndarray = np.random.permutation(flatten_board.shape[0])   # randomize the values using permutation
    shuffled_board: ndarray = flatten_board[perm].reshape(puzzle_board.shape)   # convert 1D array back to 2D
    
    return shuffled_board



def misplaced_tiles(old_board: ndarray, new_board: ndarray) -> int:
    """
    Count the misplaced tiles
    
    """

    # count variable to store the number of misplaced tiles
    __count = 0
    
    for i in range(new_board.shape[0]):
        for j in range(new_board.shape[1]):
            # compairing two arrays and if the element at the same position don't match 
            # and exclude for the new blank position
            # then increment the count variable by 1
            if old_board[i][j] != new_board[i][j] and new_board[i][j] != 0:
                print(f"Expected: {old_board[i][j]} But: {new_board[i][j]}")
                __count += 1

    return __count



def manhattan_distance(old_board: ndarray, new_board: ndarray) -> int:
    """
    Calculate Manhattan Distance
    
    """

    # convert the arrays into dictionary data structure
    new_board_dict = dict()
    old_board_dict = dict()
    
    for i in range(new_board.shape[0]):
        for j in range(new_board.shape[1]):
            old_board_dict.setdefault(f"{old_board[i][j]}", [i, j])
            new_board_dict.setdefault(f"{new_board[i][j]}", [i, j])


    # manhattan distance
    manhttn_dist = 0
    
    for tile in range(1, 9):    # 0 means no tile
        row_distance = abs(new_board_dict[f'{tile}'][0] - old_board_dict[f'{tile}'][0])
        col_distance = abs(new_board_dict[f'{tile}'][1] - old_board_dict[f'{tile}'][1])
        print(f"{tile}'s distance =  {row_distance + col_distance}")
        
        manhttn_dist += row_distance + col_distance

    return manhttn_dist


def print_board(puzzle_board: ndarray) -> None:
    modified_board: list = [[f'{j}' if j != 0 else 'X' for j in i ] for i in puzzle_board]
    print(tabulate(modified_board, tablefmt='grid'))



if __name__ == "__main__":
    # 0 means blank tile
    eight_puzzle_board = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])

    """
    # test purpose
    new_board = np.array([
        [5, 0, 8],
        [4, 2, 1],
        [7, 3, 6]
    ])
    """

    new_board = shuffle_board(eight_puzzle_board)
    
    print(f"The shuffled board is ")
    print_board(new_board)
    print()

    misplaced_tiles: int = misplaced_tiles(eight_puzzle_board, new_board)
    print(f"\nThere are(/is) {misplaced_tiles} misplaced tile(s).\n")

    m_d = manhattan_distance(eight_puzzle_board, new_board)

    print(f"Manhattan Distance is {m_d}")
    
