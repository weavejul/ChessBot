import grid, piece, movementFunctions, ui, game, os, miscFunctions, pygame, math


displaySize = 640

#Init Pygame
pygame.init()

win = pygame.display.set_mode((displaySize, displaySize))
pygame.display.set_caption("Chess")

#Game class

class Game:
    def __init__(self, grid, ui):
        self.grid = grid
        self.ui = ui
        self.gameState_Check = False
        self.gameState_Checkmate = False

    def textBasedGame(self):
        num = 0
        while True:
            self.ui.drawTextGame(num % 2)
            os.system("cls")
            num += 1

board = grid.Grid()
ui = ui.UserInterface(board)
game = Game(board, ui)

board.initializeStandardBoard()
# -----------------------------------------------------------
isPieceHeld = False
pieceHeld = None


#Draw
def draw():
    pygame.draw.rect(win, (212, 173, 57), (0, 0, displaySize, displaySize))


    if isPieceHeld:
        for y in range(8):
            for x in range(8):
                if (y, x) in board.grid[pieceHeld.coord[0]][pieceHeld.coord[1]].determineAvailableMoves(board.grid, False):
                    pygame.draw.rect(win, (212 - 30, 173 - 30, 57 - 30), (x * 75 + 20, y * 75 + 20, 75, 75))
                    pygame.draw.rect(win, (212, 255, 57), (x * 75 + 21, y * 75 + 21, 75, 75), 5)
                
    for i in range(9):
        pygame.draw.line(win, (0, 0, 0), ((i*75) + 20, 20),
                         ((i*75) + 20, displaySize - 20), 2)
    for i in range(9):
        pygame.draw.line(win, (0, 0, 0), (20, (i*75) + 20),
                         (displaySize - 20, (i*75) + 20), 2)

    for row in board.grid:
        for cell in row:
            if cell != None:
                if cell != pieceHeld:
                    win.blit(cell.img, (cell.coord[1] * 75 + 27.5, cell.coord[0] * 75 + 27.5))
                else:
                    win.blit(cell.img, (pygame.mouse.get_pos()[0] - 10,
                             pygame.mouse.get_pos()[1] - 10))

    pygame.display.update()

#PlacePiece
    """
def placePiece():
    global isPieceHeld, pieceHeld
    mouse_pos = pygame.mouse.get_pos()
    cell_over = [0, 0]
    if mouse_pos[0] <= displaySize - 20 and mouse_pos[0] >= 20:
        if mouse_pos[1] <= displaySize - 20 and mouse_pos[1] >= 20:
            cell_over[0] = math.floor((mouse_pos[0] - 20) / 75)
            cell_over[1] = math.floor((mouse_pos[1] - 20) / 75)
            if (cell_over[1], cell_over[0]) in board.grid[pieceHeld.coord[0]][pieceHeld.coord[1]].determineAvailableMoves(board.grid):
                print(cell_over)
                board.movePiece(pieceHeld.coord[0], pieceHeld.coord[1], cell_over[1], cell_over[0])
    isPieceHeld = False
    pieceHeld = None"""

#CheckForImageMove
def checkForImageMove():
    global pieceHeld, isPieceHeld
    mouse_pos = pygame.mouse.get_pos()
    cell_clicked = [0, 0]
    if mouse_pos[0] <= displaySize - 20 and mouse_pos[0] >= 20:
        if mouse_pos[1] <= displaySize - 20 and mouse_pos[1] >= 20:
            cell_clicked[0] = math.floor((mouse_pos[0] - 20) / 75)
            cell_clicked[1] = math.floor((mouse_pos[1] - 20) / 75)
            if board.grid[cell_clicked[1]][cell_clicked[0]] != None:
                pieceHeld = board.grid[cell_clicked[1]][cell_clicked[0]]
                isPieceHeld = True

# MAIN LOOP ##################################################################################################
run = True
while run:
    draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not isPieceHeld:
                checkForImageMove()
        elif event.type == pygame.MOUSEBUTTONUP:
            if isPieceHeld:
                isPieceHeld, pieceHeld = ui.placePiece(isPieceHeld, pieceHeld, displaySize)
                

pygame.quit()
