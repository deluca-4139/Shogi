from piece import Piece

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

def main():
    x = makeBoard(1)

main()
