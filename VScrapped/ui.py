import pygame, math

class UserInterface():
    def __init__(self, grid):
        self.gridTotal = grid
        self.grid = grid.grid

    def openPawnUpgradeTab(self):
        pass

    def drawTextGame(self, colorTurn):
        self.gridTotal.printBoard()
        newPieceToMove = None
        whereToMoveTo = None
        possibleMoves = []

        print("White's turn!" if colorTurn == 0 else "Black's Turn!")
        while newPieceToMove == None or self.grid[int(newPieceToMove[0])][int(newPieceToMove[2])] == None:
            newPieceToMove = input("Which piece would you like to move? (y, x) ")
            if self.grid[int(newPieceToMove[0])][int(newPieceToMove[2])] == None:
                print("That's a blank space! Try again.")
            elif self.grid[int(newPieceToMove[0])][int(newPieceToMove[2])].color != colorTurn:
                print("It's not that player's turn! Try again.")
                newPieceToMove = None


        possibleMoves = self.grid[int(newPieceToMove[0])][int(newPieceToMove[2])].determineAvailableMoves(self.grid)
        while True:
            whereToMoveTo = input("Where would you like to move it? (y, x)")
            if (int(whereToMoveTo[0]), int(whereToMoveTo[2])) in possibleMoves:
                break
            else:
                print("You can't move there! Try again.")

        self.gridTotal.movePiece(int(newPieceToMove[0]), int(newPieceToMove[2]), int(whereToMoveTo[0]), int(whereToMoveTo[2]))

    def placePiece(self, isPieceHeld, pieceHeld, displaySize):
        mouse_pos = pygame.mouse.get_pos()
        cell_over = [0, 0]
        if mouse_pos[0] <= displaySize - 20 and mouse_pos[0] >= 20:
            if mouse_pos[1] <= displaySize - 20 and mouse_pos[1] >= 20:
                cell_over[0] = math.floor((mouse_pos[0] - 20) / 75)
                cell_over[1] = math.floor((mouse_pos[1] - 20) / 75)
                if (cell_over[1], cell_over[0]) in self.grid[pieceHeld.coord[0]][pieceHeld.coord[1]].determineAvailableMoves(self.grid, False):
                    #print((cell_over[1], cell_over[0]))
                    #print(self.grid[pieceHeld.coord[0]][pieceHeld.coord[1]].determineAvailableMoves(self.grid, False))
                    self.gridTotal.movePiece(pieceHeld.coord[0], pieceHeld.coord[1], cell_over[1], cell_over[0])
        return (False, None)
        #isPieceHeld = False
        #pieceHeld = None
