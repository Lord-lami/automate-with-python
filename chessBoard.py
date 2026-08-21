import copy, sys

starting_pieces = {}

for letter in "abcdefgh":
    starting_pieces[letter+"2"] = "wP"
    starting_pieces[letter+"7"] = "bP"
    match letter:
        case "a" | "h":
            starting_pieces[letter+"1"] = "wR"
            starting_pieces[letter+"8"] = "bR"
        case "b" | "g":
            starting_pieces[letter+"1"] = "wN"
            starting_pieces[letter+"8"] = "bN"
        case "c" | "f":
            starting_pieces[letter+"1"] = "wB"
            starting_pieces[letter+"8"] = "bB"
        case "d":
            starting_pieces[letter+"1"] = "wQ"
            starting_pieces[letter+"8"] = "bQ"
        case "e":
            starting_pieces[letter+"1"] = "wK"
            starting_pieces[letter+"8"] = "bK"

# print(starting_pieces)
STARTING_PIECES = copy.copy(starting_pieces)
del starting_pieces

even_row = """  ||||||    ||||||    ||||||    ||||||    |
N ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
"""

odd_row = """  |    ||||||    ||||||    ||||||    ||||||
N | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

def is_valid_chess_board(board: dict[str, str]) -> bool:
    valid_positions = set(STARTING_PIECES.keys())
    valid_pieces = set(STARTING_PIECES.values())
    white_piece_count = {"P": 0, "R": 0, "N": 0, "B": 0, "Q": 0, "K": 0}
    black_piece_count = {"P": 0, "R": 0, "N": 0, "B": 0, "Q": 0, "K": 0}
    total_white_piece_count = 0
    total_black_piece_count = 0
    for position, piece in board.items():
        if position not in valid_positions or piece not in valid_pieces:
            return False
        
        if piece[0] == "w":
            white_piece_count[piece[1]] += 1
            total_white_piece_count += 1
        else:
            black_piece_count[piece[1]] += 1
            total_black_piece_count += 1
        
    if white_piece_count["P"] > 8 or black_piece_count["P"] > 8:
        return False
    if white_piece_count["K"] > 1 or black_piece_count["K"] > 1:
        return False
    if total_white_piece_count > 16 or total_black_piece_count > 16:
        return False

    return True

# print(is_valid_chess_board(STARTING_PIECES))
    

def print_chess_board(board: dict[str, str]) -> None:
    b_temp = copy.copy(BOARD_TEMPLATE)

    row = 0
    col = 0
    ROWS = "87654321"
    COLS = "abcdefgh"
    current_ind = b_temp.find("{}", 0)
    is_white_tile = True
    while current_ind != -1:
        position = COLS[col] + ROWS[row]
        if position in board.keys():
            b_temp = b_temp[:current_ind] + board[position] + b_temp[current_ind+2:]
        else:
            if is_white_tile:
                b_temp = b_temp[:current_ind] + WHITE_SQUARE + b_temp[current_ind+2:]
            else:
                b_temp = b_temp[:current_ind] + BLACK_SQUARE + b_temp[current_ind+2:]

        if col < 7:
            col += 1
        else:
            col = 0
            row += 1
            is_white_tile = not is_white_tile
        is_white_tile = not is_white_tile
        current_ind = b_temp.find("{}", current_ind)
    print(b_temp)

print('Interactive Chessboard')
print('by Olamide Ifarajimi')
print()
print('Pieces:')
print('  w - White, b - Black')
print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
print('Commands:')
print('  move e2 e4 - Moves the piece at e2 to e4')
print('  remove e2 - Removes the piece at e2')
print('  set e2 wP - Sets square e2 to a white pawn')
print('  reset - Resets pieces back to their starting squares')
print('  clear - Clears the entire board')
print('  fill wP - Fills entire board with white pawns.')
print('  quit - Quits the program')

main_board = copy.copy(STARTING_PIECES)
while True:
    print_chess_board(main_board)
    prompt = input("> ").split()
    match prompt[0]:
        case "move":
            if len(prompt) != 3:
                raise Exception("Invalid number of arguments to the move command")
            main_board[prompt[2]] = main_board[prompt[1]]
            del main_board[prompt[1]]
        case "remove":
            if len(prompt) != 2:
                raise Exception("Invalid number of arguments to the remove command")
            del main_board[prompt[1]]
        case "set":
            if len(prompt) != 3:
                raise Exception("Invalid number of arguments to the set command")
            main_board[prompt[1]] = prompt[2]
        case "reset":
            if len(prompt) != 1:
                raise Exception("Invalid number of arguments to the reset command")
            main_board = copy.copy(STARTING_PIECES)
        case "clear":
            if len(prompt) != 1:
                raise Exception("Invalid number of arguments to the clear command")
            main_board = {}
        case "fill":
            if len(prompt) != 2:
                raise Exception("Invalid number of arguments to the fill command")
            ROWS = "87654321"
            COLS = "abcdefgh"
            for row in ROWS:
                for col in COLS:
                    main_board[col+row] = prompt[1]
        case "quit":
            sys.exit()
        case _:
            print("Invalid command: " + prompt[0])

