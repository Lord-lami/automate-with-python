import copy

def find_pieces_capturable_position_in_line(piece_position: str, line: list[str], board: dict[str, str]) -> str:
    for point in line:
        position = point + piece_position[1]
        if point.isdigit():
            position = piece_position[0] + point
        if position in board.keys():
            if board[position][0] == "b":
                return position
            else:
                break

def white_rook_can_capture(rook_position: str, board: dict[str, str]) -> list[str]:
    capturable_positions = []
    ROWS = "87654321"
    COLS = "abcdefgh"
    left = list(COLS[:COLS.index(rook_position[0])])
    left.reverse()
    right = list(COLS[COLS.index(rook_position[0])+1:])
    up = list(ROWS[:ROWS.index(rook_position[1])])
    up.reverse()
    down = list(ROWS[ROWS.index(rook_position[1])+1:])

    lines = [left, right, up, down]
    for line in lines:
        capturable_position = find_pieces_capturable_position_in_line(rook_position, line, board)
        if capturable_position:
            capturable_positions.append(capturable_position)
    return capturable_positions

print(white_rook_can_capture('d3', {'d7': 'bQ', 'd2': 'wB', 'f1': 'bP', 'a3': 'bN'}))    
    