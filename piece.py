# Piece object.

pieceType = ""  # [k]ing, [r]ook, [b]ishop, [g]old general, [s]ilver general, [kn]ight, [l]ance, [p]awn
owner = -1      # 0 for sente, 1 for gote.
position = []   # [x, y]; note that the x direction is flipped, as
                #         board reads from right to left. 1-based.
promoted = False

class Piece:
    def __init__(self, type, own, pos):
        self.pieceType = type
        self.owner = own
        self.position = pos
        #self.promoted == False 

    def __str__(self):
        return self.pieceType

    # Checks whether or not the provided position array is a valid move
    # for the piece to take. Assumes the position is valid insofar as it
    # is on the board; should check for this in parent class prior to
    # passing it in. Must still check board-wise validity wrt pieces.
    def checkLegalMove(self, pos):
        #TODO: check for promotion

        # We don't want to allow not moving at all.
        if pos == self.position:
            return False

        switch = {
            "k": False if (abs(self.position[0] - pos[0]) > 1 or abs(self.position[1] - pos[1]) > 1) else True,
            "r": True if (self.position[0] != pos[0] and self.position[1] == pos[1]) or (self.position[1] != pos[1] and self.position[0] == pos[0]) else False,
            "b": True if (abs(self.position[0] - pos[0]) == abs(self.position[1] - pos[1])) else False,
            "g": True if ((self.owner == 0 and (((self.position[1] - pos[1] == 1) and (abs(self.position[0] - pos[0]) <= 1))     # move forwards as sente
                                             or ((self.position[1] == pos[1]) and (abs(self.position[0] - pos[0]) == 1))         # move sideways as sente
                                             or ((self.position[1] - pos[1] == -1) and (self.position[0] == pos[0]))))           # move backwards as sente
                       or (self.owner == 1 and (((pos[1] - self.position[1] == 1) and (abs(self.position[0] - pos[0]) <= 1))     # move forwards as gote
                                             or ((self.position[1] == pos[1]) and (abs(self.position[0] - pos[0]) == 1))         # move sideways as gote
                                             or ((pos[1] - self.position[1] == -1) and (self.position[0] == pos[0])))))          # move backwards as gote
                      else False,
            "s": True if ((self.owner == 0 and (((self.position[1] - pos[1] == 1) and (abs(self.position[0] - pos[0]) <= 1))     # move forwards as sente
                                             or ((self.position[1] - pos[1] == -1) and (abs(self.position[0] - pos[0]) == 1))))  # move backwards as sente
                       or (self.owner == 1 and (((pos[1] - self.position[1] == 1) and (abs(self.position[0] - pos[0]) <= 1))     # move forward as gote
                                             or ((pos[1] - self.position[1] == -1) and (abs(self.position[0] - pos[0]) == 1))))) # move backwards as gote
                      else False,
            "kn": True if (((self.owner == 0) and ((self.position[1] - pos[1] == 2) and (abs(self.position[0] - pos[0]) == 1)))  # sente move
                        or ((self.owner == 1) and ((pos[1] - self.position[1] == 2) and (abs(self.position[0] - pos[0]) == 1)))) # gote move
                       else False,
            "l": True if (((self.owner == 0) and ((self.position[1] - pos[1] >= 1) and (self.position[0] == pos[0])))            # sente move
                       or ((self.owner == 1) and ((pos[1] - self.position[1] >= 1) and (self.position[0] == pos[0]))))           # gote move
                      else False,
            "p": True if (((self.owner == 0) and ((self.position[1] - pos[1] == 1) and (self.position[0] == pos[0])))            # sente move
                       or ((self.owner == 1) and ((pos[1] - self.position[1] == 1) and (self.position[0] == pos[0]))))           # gote move
                      else False
            }
        return switch[self.pieceType]

    # Returns a list of possible board positions (not array positions)
    # that this piece can move to, depending on board type (see main.makeBoard()).
    # Used for checking status of check/mate.
    def findPossibleMoves(self, type):
        moves = []
        top = 10 if type == 0 else 6
        for x in range(1, top):
            for y in range(1, 6):
                if self.checkLegalMove([x, y]):
                    moves.append([x, y])
        return moves
