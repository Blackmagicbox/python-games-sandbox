import math

print("Hello, World!")
y = lambda x: math.sqrt(x)

print(y(4))

chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]
for row in chess_board:
    print(row)
