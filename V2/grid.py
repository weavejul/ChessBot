#Grid [CHESS AI]

import piece, essentialFunctions

#The grid class represent the board itself, with pieces interacting on it
class Grid():
  def __init__(self):
    self.grid = [[None for i in range(8)] for j in range(8)]
  
  #Sets the board to the standard chess game beginning
  def initializeStandardBoard(self):
    self.gridArray = [[None for i in range(8)] for j in range(8)]
    for i in range(8):
      self.grid[1][i] = piece.Piece("Pawn", 1, (1, i), False, False)
      self.grid[6][i] = piece.Piece("Pawn", 0, (6, i), False, False)
    for i in range(2):
      self.grid[0][i * 7] = piece.Piece("Rook", 1, (0, i*7))
      self.grid[7][i * 7] = piece.Piece("Rook", 0, (7, i*7))
    for i in range(2):
      self.grid[0][(i*5)+1] = piece.Piece("Knight", 1, (0, (i*5)+1))
      self.grid[7][(i*5)+1] = piece.Piece("Knight", 0, (7, (i*5)+1))
    for i in range(2):
      self.grid[0][(i*3)+2] = piece.Piece("Bishop", 1, (0, (i*3)+2))
      self.grid[7][(i*3)+2] = piece.Piece("Bishop", 0, (7, (i*3)+2))
  
    self.grid[0][3] = piece.Piece("Queen", 1, (0, 3))
    self.grid[7][3] = piece.Piece("Queen", 0, (7, 3))
    self.grid[0][4] = piece.Piece("King", 1, (0, 4), True, False)
    self.grid[7][4] = piece.Piece("King", 0, (7, 4), True, False)
    ####
    #self.grid[2][2] = piece.Piece("King", 0, (2, 2))
    ####

  #Deletes the content of a cell
  def deleteCellContents(self, y, x):
    self.grid[y][x] = None

  #Moves a piece from one cell to another
  def movePiece(self, y1, x1, y2, x2):
    self.deleteCellContents(y2, x2)
    self.grid[y2][x2] = self.grid[y1][x1]
    self.deleteCellContents(y1, x1)
    self.grid[y2][x2].changeCoordinates(y2, x2)
    self.grid[y2][x2].hasTakenFirstMove = True
    self.grid[y2][x2].canCastle = False
    newPieceMoves = self.determineAvailableMoves(self.grid[y2][x2])

    for coords in newPieceMoves:
      if not self.grid[coords[0]][coords[1]] == None and self.grid[coords[0]][coords[1]].typeOfPiece == "King":
        print("CHECK")


  def determineAvailableMoves(self, piece):
    return essentialFunctions.determineAvailableMoves(self.grid, piece)

  #Prints the board state (for debugging)
  def printBoard(self):
    print("   0   1   2   3   4   5   6   7  X")
    for i in range(8):
      print(str(i) + " |", end = "")
      for j in range(8):
        if j == 7:
          print(essentialFunctions.returnLetterForPiece(self.grid[i][j]) + "|")
        else:
          print((essentialFunctions.returnLetterForPiece(self.grid[i][j])) + " | ", end = "")
      if i != 7:
        print("  |" + ("----" * 7) + "-|") 
