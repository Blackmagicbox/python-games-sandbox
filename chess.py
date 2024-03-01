import copy

BOARD_COORDS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7

}


def print_board(board):
    for row in board:
        print("".join(row))


def build_board():
    board = []
    for row in range(8):
        board.append([])

    color = 0
    for row in board:
        for _ in range(8):
            if color == 0:
                square_color = "x"
            else:
                square_color = "_"
            color ^= 1
            row.append(f"{square_color}")

        color ^= 1

    return board


def update_board(board, move):
    piece, column, row = tuple(move)
    _board = copy.deepcopy(board)
    _board[int(row)][BOARD_COORDS[column]] = piece
    return _board


def main():
    board = [
        [],
        ["br", "bh", "bb", "bk", "bq", "bb", "bh", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["00", "01", "00", "01", "00", "01", "00", "01"],
        ["01", "00", "00", "01", "00", "01", "00", "01"],
        ["00", "01", "00", "01", "00", "01", "00", "01"],
        ["01", "00", "00", "01", "00", "01", "00", "01"],
        ["wr", "wh", "wb", "wk", "wq", "wb", "wh", "wr"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ]

    print_board(build_board())

    play = input("What is your play:\n")
    while play != "exit":
        print_board(update_board(build_board(), (play.split(','))))
        print("\n")
        play = input("What is your play:\n")


main()
