import copy, sys, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)

starting_pieces = {}
ROWS = "87654321"
COLS = "abcdefgh"

# Fill the starting_pieces dictionary with 
# the - starting_pieces[position] = piece - format
# of a starting chessboard
for letter in COLS:
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

logging.debug(starting_pieces)
"""STARTING_PIECES is the board at the start of a chess game.
It looks like this when printed

    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||bR|| bN ||bB|| bQ ||bK|| bB ||bN|| bR |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | bP ||bP|| bP ||bP|| bP ||bP|| bP ||bP||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||||||    ||||||    ||||||    ||||||    |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 |    ||||||    ||||||    ||||||    ||||||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||||||    ||||||    ||||||    ||||||    |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 |    ||||||    ||||||    ||||||    ||||||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||wP|| wP ||wP|| wP ||wP|| wP ||wP|| wP |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | wR ||wN|| wB ||wQ|| wK ||wB|| wN ||wR||
  |____||||||____||||||____||||||____||||||


"""
STARTING_PIECES = copy.copy(starting_pieces)
del starting_pieces

# The {}s are to be replaced with pieces, pipes(||) or spaces(  )
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

# is_valid_chess_board takes a board (a dict[position] = pieces) and 
# returns True if it is a valid chess board and False if it isn't
# An invalid board has:
# 1. Pieces that are outside of the valid pieces: {'wP', 'wN', 'bK', 'bP', 'wR', 'bR', 'wK', 'wQ', 'bN', 'bB', 'bQ', 'wB'}
# 2. More than 16 White pieces or Black pieces
# 3. More than 8 White Pawns
# 4. More than 1 White King or Black King
def is_valid_chess_board(board: dict[str, str]) -> bool:
    valid_pieces = set(STARTING_PIECES.values())
    white_piece_count = {"P": 0, "R": 0, "N": 0, "B": 0, "Q": 0, "K": 0}
    black_piece_count = {"P": 0, "R": 0, "N": 0, "B": 0, "Q": 0, "K": 0}
    total_white_piece_count = 0
    total_black_piece_count = 0
    for _, piece in board.items():
        if piece not in valid_pieces:
            logging.debug("Invalid Chess Board: Invalid Piece - "+ piece)
            return False
        
        if piece[0] == "w":
            white_piece_count[piece[1]] += 1
            total_white_piece_count += 1
        else:
            black_piece_count[piece[1]] += 1
            total_black_piece_count += 1
        
    if white_piece_count["P"] > 8:
        logging.info("Invalid Chess Board: Too many White Pawns - " + white_piece_count["P"])
        return False
    if black_piece_count["P"] > 8:
        logging.info("Invalid Chess Board: Too many Black Pawns - " + black_piece_count["P"])
        return False
    if white_piece_count["K"] > 1:
        logging.info("Invalid Chess Board: More than 1 White King - " + white_piece_count["K"])
        return False
    if black_piece_count["K"] > 1:
        logging.info("Invalid Chess Board: More than 1 Black King - " + black_piece_count["K"])
        return False
    if total_white_piece_count > 16:
        logging.info("Invalid Chess Board: Too Many White Pieces - " + total_white_piece_count)
        return False
    if total_black_piece_count > 16:
        logging.info("Invalid Chess Board: Too Many Black Pieces - " + total_black_piece_count)
        return False

    logging.debug("The Chess Board is Valid")
    return True

WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

# print_chess_board takes a board and prints the chess board to a terminal
def print_chess_board(board: dict[str, str]) -> None:
    is_valid_chess_board(board)
    b_temp = copy.copy(BOARD_TEMPLATE)

    row = 0
    col = 0
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


def is_valid_position(position: str) -> bool:
    if len(position) != 2:
        return False
    if position[0] not in COLS:
        return False
    if position[1] not in ROWS:
        return False
    
    return True

instructions = '''
Pieces:
  w - White, b - Black
  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King
  Example:
    wB - White Bishop
Commands:
  move e2 e4 [message] - Moves the piece at e2 to e4.
  remove e2 - Removes the piece at e2.
  set e2 wP - Sets square e2 to a white pawn.
  reset - Resets pieces back to their starting squares.
  clear - Clears the entire board.
  fill wP - Fills entire board with white pawns.
  quit - Quits the program.
'''

print('Interactive Chessboard')
print('by Olamide Ifarajimi')

main_board = copy.copy(STARTING_PIECES)
message = ""
while True:
    print(instructions)
    print_chess_board(main_board)
    if message:
        print("Message:", message)

    prompt = input("> ").split()
    match prompt[0]:
        case "move":
            # Raise Exception if there are less than 2 positions written after move
            if len(prompt) < 3:
                raise Exception("Invalid number of arguments to the move command")

            # Anything written after the positions is a message
            if len(prompt) > 3:
                logging.info("Received message: " + message)
                message = " ".join(prompt[3:])
            
            # Check that the postions are valid
            if not is_valid_position(prompt[1]):
                logging.warning("Invalid Position: " + prompt[1])
                continue
            if not is_valid_position(prompt[2]):
                logging.warning("Invalid Position: " + prompt[2])
                continue
            logging.info("Positions are Valid")

            # Check that the postions have pieces on them
            if prompt[1] not in main_board.keys():
                logging.warning(f"Invalid Move: Position {prompt[1]} is empty")
                continue
            logging.info("The First Position has a piece on it")

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
            for row in ROWS:
                for col in COLS:
                    main_board[col+row] = prompt[1]
        case "quit":
            sys.exit()
        case _:
            print("Invalid command: " + prompt[0])
