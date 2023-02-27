import movementFunctions

#The piece class represents all pieces on the board
class Piece():
    def __init__(self, typeOfPiece, color, coord, img, canCastle = False, movesTaken = 0):
        #Types: 0-Pawn 1-Rook 2-Knight 3-Bishop 4-Queen 5-King
        self.typeOfPiece = typeOfPiece
        # 0-White 1-Black
        self.color = color
        #Starts from zero
        self.coord = coord
        #(y, x)
        self.canCastle = canCastle
        self.movesTaken = movesTaken
        self.img = img

    #Changes the piece's coordinates.
    def changeCoordinates(self, y, x):
        self.coord = (y, x)

    def changeCastlePlusMoveState(self):
        self.canCastle = False
        self.movesTaken += 1

    def determineAvailableMoves(self, grid, checkOverride = False):
        return movementFunctions.determineMoves(grid, self, checkOverride)
