def get_queen_positions(queens):
    positions = []
    for (i, j) in enumerate(queens):
        positions.append([j, i])
    return positions


queen_position_rows = [6, 4, 2, 0, 5, 7, 1, 2]

print(get_queen_positions(queen_position_rows))
