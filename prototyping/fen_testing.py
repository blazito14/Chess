startingFEN = r"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


# piecePlacement_sideToMove_castlingAbility_enPassantTargetSquare_halfMoveClock_fullMoveCounter
# piecePlacement
#   numbers are filling in empty squares, otherwise pieces are there.
#   starts at 8th rank and goes down. Starts at A file and moves right
#
# sideToMove
#   w or b depending on side
#
# castling
#   kq black king/queen side available KQ same for white. - means none
#
# enPassant
#   the space in algebraic notation behind a pawn that has just moved two squares, - means none
#
# halfMoveClock
#   how many moves both players have made since the last pawn advance or piece capture. When this is 100 game ends
#
# fullMove
#   how many moves both players have completed, increments by 1 every time black moves
#


class Piece:
    def __init__(self, pieceNum):
        pieceNums = {0: 'None',
                     1: 'King',
                     2: 'Pawn',
                     3: 'Knight',
                     4: 'Bishop',
                     5: 'Rook',
                     6: 'Queen',
                     }
        pieceColors = {8: 'White',
                       16: 'Black'}
        self.name = pieceNums[pieceNum % 8]
        self.color = pieceColors[pieceNum - (pieceNum % 8)]
        self.num = pieceNum


print(f"{'binary':<10}{'name':<10}{'color':<10}")
for i in range(0b110):
    whitePiece = Piece(i + 0b01000)
    blackPiece = Piece(i + 0b10000)
    print(f"{whitePiece.num:<10}{whitePiece.name:<10}{whitePiece.color}")
    print(f"{blackPiece.num:<10}{blackPiece.name:<10}{blackPiece.color}")
