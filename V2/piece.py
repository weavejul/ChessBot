#Piece [CHESS AI]

import essentialFunctions

#The piece class represents all pieces on the board
class Piece():
  def __init__(self, typeOfPiece, color, coord, canCastle = False, hasTakenFirstMove = False, inCheck = False):
    #Types: 0-Pawn 1-Rook 2-Knight 3-Bishop 4-Queen 5-King
    self.typeOfPiece = typeOfPiece
    # 0-White 1-Black
    self.color = color
    #Starts from zero
    self.coord = coord
    #(y, x)
    self.canCastle = canCastle
    self.hasTakenFirstMove = hasTakenFirstMove

  #Changes the piece's coordinates.
  def changeCoordinates(self, y, x):
    self.coord = (y, x)

  def findAvailableMoves(self, grid):
    return essentialFunctions.determineAvailableMoves(grid, self)
