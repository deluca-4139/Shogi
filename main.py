from piece import Piece

# Create the starting board depending on type of game.
# Returns nested array of pieces.
def makeBoard(type):
    # Full shogi. TBI
    if(type == 0):
        return None
    # Mini shogi.
    if(type == 1):
        board = [[Piece("r", 1, [5, 1]), Piece("b", 1, [4, 1]), Piece("s", 1, [3, 1]), Piece("g", 1, [2, 1]), Piece("k", 1, [1, 1])],
                 [None,                  None,                  None,                  None,                  Piece("p", 1, [1, 2])],
                 [None,                  None,                  None,                  None,                  None                 ],
                 [Piece("p", 0, [5, 4]), None,                  None,                  None,                  None                 ],
                 [Piece("k", 0, [5, 5]), Piece("g", 0, [4, 5]), Piece("s", 0, [3, 5]), Piece("b", 0, [2, 5]), Piece("r", 0, [1, 5])]]
        return board

# Check if there are pieces in between a piece and its desired move. Assumes move is legal.
# Returns true if move possible, false if not; returns a Piece if capturable.
# Args:
# board ~ board to check
# piece ~ tuple giving array position (NOT location on board) of piece to move
# pos ~ tuple giving desired location on board (NOT array position) to move piece to
def checkIntermediatePieces(board, piece, pos):
    array_pos = [(5-pos[0]), (pos[1]-1)] # Tuple of location in array of desired space to move to. Array pos ends up being [y, x]. Confusing, I know...
    # Check for piece type; rook, bishop, and lance are the only ones we care about.
    pieces = ["r", "b", "l"]
    if board[piece[0]][piece[1]].pieceType in pieces:
        if board[piece[0]][piece[1]].position[0] != pos[0] and board[piece[0]][piece[1]].position[1] != pos[1]:
            # Diagonal move chosen
            test_pos = board[piece[0]][piece[1]].position
            test_pos[0] = 5 - test_pos[0]
            test_pos[1] -= 1
            while test_pos != array_pos:
                # Find difference in x and y values, move one tick in direction desired, and check for piece; if found, return false.
                test_pos[0] += round(((array_pos[0] - test_pos[0]) / abs(array_pos[0] - test_pos[0])))
                test_pos[1] += round(((array_pos[1] - test_pos[1]) / abs(array_pos[1] - test_pos[1])))
                if board[test_pos[1]][test_pos[0]] != None and test_pos != array_pos:
                    return False
            # If we've gotten through the while loop, we must have not found an intervening piece,
            # so check for one in the space we want to move to; if found, return it if capturable.
            if isinstance(board[array_pos[1]][array_pos[0]], Piece):
                if board[array_pos[1]][array_pos[0]].owner != board[piece[0]][piece[1]].owner:
                    return board[array_pos[1]][array_pos[0]]
                else:
                    return False
            # Otherwise, we must be able to make the move freely. Return true.
            else:
                return True
        elif board[piece[0]][piece[1]].position[0] != pos[0]:
            # Horizontal move chosen
            test_pos = board[piece[0]][piece[1]].position
            test_pos[0] = 5 - test_pos[0]
            test_pos[1] -= 1
            while test_pos != array_pos:
                # Find difference in x values, move one tick in direction desired, and check for piece; if found, return false.
                test_pos[0] += round(((array_pos[0] - test_pos[0]) / abs(array_pos[0] - test_pos[0])))
                if board[test_pos[1]][test_pos[0]] != None and test_pos != array_pos:
                    return False
            # If we've gotten through the while loop, we must have not found an intervening piece,
            # so check for one in the space we want to move to; if found, return it if capturable.
            if isinstance(board[array_pos[1]][array_pos[0]], Piece):
                if board[array_pos[1]][array_pos[0]].owner != board[piece[0]][piece[1]].owner:
                    return board[array_pos[1]][array_pos[0]]
                else:
                    return False
            # Otherwise, we must be able to make the move freely. Return true.
            else:
                return True
        elif board[piece[0]][piece[1]].position[1] != pos[1]:
            # Vertical move chosen
            test_pos = board[piece[0]][piece[1]].position
            test_pos[0] = 5 - test_pos[0]
            test_pos[1] -= 1
            while test_pos != array_pos:
                # Find difference in y values, move one tick in direction desired, and check for piece; if found, return false.
                test_pos[1] += round(((array_pos[1] - test_pos[1]) / abs(array_pos[1] - test_pos[1])))
                if board[test_pos[1]][test_pos[0]] != None and test_pos != array_pos:
                    return False
            # If we've gotten through the while loop, we must have not found an intervening piece,
            # so check for one in the space we want to move to; if found, return it if capturable.
            if isinstance(board[array_pos[1]][array_pos[0]], Piece):
                if board[array_pos[1]][array_pos[0]].owner != board[piece[0]][piece[1]].owner:
                    return board[array_pos[1]][array_pos[0]]
                else:
                    return False
            # Otherwise, we must be able to make the move freely. Return true.
            else:
                return True
    # The piece must not be able to move more than one square. Check to see
    # if there is a piece where it wants to move. If so, return it.
    else:
        if isinstance(board[array_pos[1]][array_pos[0]], Piece):
            if board[array_pos[1]][array_pos[0]].owner != board[piece[0]][piece[1]].owner:
                return board[array_pos[1]][array_pos[0]]
            else:
                return False
        else:
            return True

# Completes a given move...
def takeMove(board, piece, pos):
    return None

def main():
    x = makeBoard(1)

main()
