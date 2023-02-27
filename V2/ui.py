#UI [CHESS AI]

import pygame

class UserInterface():
  def __init__(self, grid):
    self.grid = grid
    self.boardCells = grid.grid

  def openPawnUpgradeTab(self):
    pass

  def drawTextGame(self, colorTurn):
    self.grid.printBoard()
    newPieceToMove = None
    whereToMoveTo = None
    possibleMoves = []

    print("White's turn!" if colorTurn == 0 else "Black's Turn!")
    while newPieceToMove == None or self.boardCells[int(newPieceToMove[0])][int(newPieceToMove[2])] == None:
      newPieceToMove = input("Which piece would you like to move? (y, x) ")
      if self.boardCells[int(newPieceToMove[0])][int(newPieceToMove[2])] == None:
        print("That's a blank space! Try again.")
      elif self.boardCells[int(newPieceToMove[0])][int(newPieceToMove[2])].color != colorTurn:
        print("It's not that player's turn! Try again.")
        newPieceToMove = None


    possibleMoves = self.grid.determineAvailableMoves(self.boardCells[int(newPieceToMove[0])][int(newPieceToMove[2])])
    while True:
      whereToMoveTo = input("Where would you like to move it? (y, x) ")
      if (int(whereToMoveTo[0]), int(whereToMoveTo[2])) in possibleMoves:
        break
      else:
        print("You can't move there! Try again.")

    self.grid.movePiece(int(newPieceToMove[0]), int(newPieceToMove[2]), int(whereToMoveTo[0]), int(whereToMoveTo[2]))

  def draw(self):
    pygame.draw.rect(win, (212, 173, 57), (0, 0, displaySize, displaySize))
    if isPieceHeld:
      for y in range(8):
        for x in range(8):
          if highlightedCells[y][x] == 1:
            pygame.draw.rect(win, (212, 255, 57), (x * 75 + 20, y * 75 + 20, 75, 75))
                
    for i in range(9):
      pygame.draw.line(win, (0, 0, 0), ((i*75) + 20, 20),
                        ((i*75) + 20, displaySize - 20), 2)
    for i in range(9):
      pygame.draw.line(win, (0, 0, 0), (20, (i*75) + 20),
                        (displaySize - 20, (i*75) + 20), 2)

    for row in cells:
      for cell in row:
        if cell != None:
          if cell != pieceHeld:
            win.blit(cell.img, cell.imgPos)
          else:
            win.blit(cell.img, (pygame.mouse.get_pos()[0] - 10,
                      pygame.mouse.get_pos()[1] - 10))

    pygame.display.update()
    
