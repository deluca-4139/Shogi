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
    array_pos = [(5-pos[0]), (pos[1]-1)] # Tuple of location in array of desired space to move to.
    # Check for piece type; rook, bishop, and lance are the only ones we care about.
    pieces = ["r", "b", "l"]
    if board[piece[0]][piece[1]].pieceType in pieces:
        if board[piece[0]][piece[1]].position[0] != pos[0] and board[piece[0]][piece[1]].position[1] != pos[1]:
            # Diagonal move chosen
            test_pos = [board[piece[0]][piece[1]].position[0], board[piece[0]][piece[1]].position[1]] # This was originally pass by reference and gave me a lot of trouble
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
            test_pos = [board[piece[0]][piece[1]].position[0], board[piece[0]][piece[1]].position[1]]
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
            test_pos = [board[piece[0]][piece[1]].position[0], board[piece[0]][piece[1]].position[1]]
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

# Completes a given move. Checks for legality and possibility before doing so.
# Args are same as checkIntermediatePieces.
# Returns a tuple:
# [0] is False if not a legal or possible move.
#     - if False, [1] is 0 if illegal, 1 if intervening pieces found.
# [0] is True if move has been made.
#     - if True, [1] is the resulting board state after making given move. [2] is a piece if captured, None if not.
def takeMove(board, piece, pos):
    # Check legality of move for specific piece.
    legal = board[piece[0]][piece[1]].checkLegalMove(pos)
    if not legal:
        return [False, 0]
    # Check possibility of move for piece on board.
    possible = checkIntermediatePieces(board, piece, pos)
    if not possible:
        return [False, 1]
    # Take move, update piece's interal position.
    origPiece = Piece(board[piece[0]][piece[1]].pieceType, board[piece[0]][piece[1]].owner, [pos[0], pos[1]])
    board[piece[0]][piece[1]] = None
    board[(pos[1]-1)][(5-pos[0])] = origPiece
    # Check if move would capture piece.
    if isinstance(possible, Piece):
        return [True, board, possible]
    else:
        return [True, board, None]

# Checks the status of the board to see if a player is in check.
# Player whose status is checked is opposite owner input
# (i.e. checkCheck(0, board) will return True if 1 is in check).
def checkCheck(owner, board):
    pieces = [] # Array of pieces owned by owner to check move possibilities for
    type = 0 if len(board) == 9 else 1
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] is not None and board[y][x].owner == owner:
                pieces.append([y, x])
    for piece in pieces:
        moves = board[piece[0]][piece[1]].findPossibleMoves(type)
        for move in moves:
            check = checkIntermediatePieces(board, piece, move)
            if isinstance(check, Piece):
                if check.pieceType == "k" and check.owner != owner:
                    return True
    return False

# Checks the status of the board to see if a player is in checkmate.
# Similar to checkCheck, player whose status is checked is opposite
# owner input (i.e. checkMate(0, board)) will return True if 1 is
# in checkmate.
def checkMate(owner, board):
    pieces = [] # Array of all pieces owned by !owner to check move possibilities for
    type = 0 if len(board) == 9 else 1
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] is not None and board[y][x].owner != owner:
                pieces.append([y, x])
    all_moves = [] # Array of pieces paired with all their possible moves
    for piece in pieces:
        moves = board[piece[0]][piece[1]].findPossibleMoves(type)
        all_moves.append([piece, moves])
    for p in all_moves:
        for move in p[1]:
            board_buf = copyBoard(board)
            board_buf = takeMove(board_buf, p[0], move)
            if board_buf[0] == True:
                if not checkCheck(owner, board_buf[1]):
                    return False
    return True

# Performs a drop of the given piece onto the given board.
# Performs standard drop checks depending on piece type,
# returns False if drop is not legal/possible. Returns a
# new board with successfully dropped piece if possible.
# Args same as checkIntermediatePieces/takeMove.
def drop(board, piece, pos):
    array_pos = [(5-pos[0]), (pos[1]-1)] # Tuple of location in array of desired space to move to.
    # We don't allow drops on non-empty spaces.
    if board[array_pos[1]][array_pos[0]] is not None:
        return False
    if piece.pieceType == "p":
        # Pawn not allowed to drop on final row (行き所のない駒)
        if (pos[1] == 1 and piece.owner == 1) or (pos[1] == len(board) and piece.owner == 0):
            return False
        # Pawn not allowed to drop in a file that already has a pawn (二歩)
        for p in range(len(board)):
            if board[p][array_pos[0]] is not None:
                if board[p][array_pos[0]].owner != piece.owner and board[p][array_pos[0]].pieceType == "p":
                    return False
        # Pawn not allowed to drop to give immediate checkmate (打ち歩詰め)
        testMate = copyBoard(board)
        testMate[array_pos[1]][array_pos[0]] = piece
        if checkCheck(((piece.owner + 1) % 2), testMate):
            if checkMate(((piece.owner + 1) % 2), testMate):
                return False
    if piece.pieceType == "l":
        # Lance not allowed to drop on final row (行き所のない駒)
        if (pos[1] == 1 and piece.owner == 1) or (pos[1] == len(board) and piece.owner == 0):
            return False
    if piece.pieceType == "kn":
        # Knight not allowed to drop on final or penultimate row (行き所のない駒)
        if (pos[1] <= 2 and piece.owner == 1) or (pos[1] >= (len(board)-1) and piece.owner == 0):
            return False
    # If we've gotten through all these checks, we must be allowed to drop.
    newBoard = copyBoard(board)
    newBoard[array_pos[1]][array_pos[0]] = Piece(piece.pieceType, ((piece.owner + 1) % 2), [pos[0], pos[1]])
    return newBoard

# Copies board state from b1 into a new returned board.
def copyBoard(b1):
    type = 0 if len(b1) == 9 else 1
    buf = makeBoard(type)
    for y in range(len(b1)):
        for x in range(len(b1)):
            if b1[y][x] is None:
                buf[y][x] = None
            else:
                buf[y][x] = Piece(b1[y][x].pieceType, b1[y][x].owner, b1[y][x].position)
    return buf

# Prints a text representation of the board to the console.
# Purely for diagnostic purposes.
def printBoard(board):
    for line in board:
        for piece in line:
            if piece is None:
                print("~", end=" ")
            else:
                print(piece, end=" ")
        print()

# Check equivalency of two boards.
# Purely for diagnostic purposes.
def checkBoards(b1, b2):
    for y in range(len(b1)):
        for x in range(len(b1)):
            if (b1[y][x] == None and b2[y][x] != None) or (b2[y][x] == None and b1[y][x] != None):
                return False
            elif b1[y][x] != None and b2[y][x] != None:
                if b1[y][x].pieceType != b2[y][x].pieceType:
                    print(y, x)
                    print(b1[y][x].pieceType, b2[y][x].pieceType)
                    return False
                if b1[y][x].owner != b2[y][x].owner:
                    print(y, x)
                    print(b1[y][x].owner, b2[y][x].owner)
                    return False
                if b1[y][x].position != b2[y][x].position:
                    print(y, x)
                    print(b1[y][x].position, b2[y][x].position)
                    return False
    return True

def main():
    x = makeBoard(1)

main()
