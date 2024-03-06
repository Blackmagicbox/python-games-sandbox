# import math
#
# print("Hello, World!")
# y = lambda x: math.sqrt(x)
#
# print(y(4))
#
# chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]
# for row in chess_board:
#     print(row)

rows = list('ABCDEFGH')
cols = list(range(1,9))
board_positions = list(zip(rows, cols))
print(board_positions)
sorted_by_col = sorted(board_positions, key=lambda square: -1 * square[1])
print(sorted_by_col)
