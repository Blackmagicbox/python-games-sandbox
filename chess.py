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

    print_board(board)



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

    build_board()

main()