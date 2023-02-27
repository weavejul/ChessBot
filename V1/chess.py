#Chess

#TODO:
"""
Implement pawn-queen
Check/checkmate checks
Highlighted cells
Restrict movement
Back a Move
"""

import os, pygame, math

displaySize = 640

#Init Pygame
pygame.init()

win = pygame.display.set_mode((displaySize, displaySize))
pygame.display.set_caption("Chess")


#Images
chessPieces = [pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_pdt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_plt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_rdt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_rlt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_kdt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_klt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_qdt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_qlt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_ndt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_nlt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_bdt60.png"),
               pygame.image.load(r"C:\Users\Julian\Desktop\Chess AI\ChessImages\Chess_blt60.png"),]
#Pawn, Rook, King, Queen, Knight, Bishop

class Piece:
    def __init__(self, x, y, img, pieceType, color):
        self.x = x
        self.y = y
        self.img = img
        self.pieceType = pieceType
        self.color = color
        self.imgPos = (x * 75 + 27.5, y * 75 + 27.5)
        
    def move(self, x, y):
        self.x = x
        self.y = y
        self.imgPos = (x * 75 + 27.5, y * 75 + 27.5)
    
    


def draw():
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


run = True
cells = [[None for i in range(8)] for j in range(8)]
highlightedCells = [[0 for i in range(8)] for j in range(8)]
isPieceHeld = False
pieceHeld = None

def resetBoardCells():
    for i in range(8):
        cells[1][i] = Piece(i, 1, chessPieces[0], "Pawn", 1)
        cells[6][i] = Piece(i, 6, chessPieces[1], "Pawn", 0)
    cells[0][0] = Piece(0, 0, chessPieces[2], "Rook", 1)
    cells[0][1] = Piece(1, 0, chessPieces[8], "Knight", 1)
    cells[0][2] = Piece(2, 0, chessPieces[10], "Bishop", 1)
    cells[0][3] = Piece(3, 0, chessPieces[6], "Queen", 1)
    cells[0][4] = Piece(4, 0, chessPieces[4], "King", 1)
    cells[0][5] = Piece(5, 0, chessPieces[10], "Bishop", 1)
    cells[0][6] = Piece(6, 0, chessPieces[8], "Knight", 1)
    cells[0][7] = Piece(7, 0, chessPieces[2], "Rook", 1)
    cells[7][0] = Piece(0, 7, chessPieces[3], "Rook", 0)
    cells[7][1] = Piece(1, 7, chessPieces[9], "Knight", 0)
    cells[7][2] = Piece(2, 7, chessPieces[11], "Bishop", 0)
    cells[7][3] = Piece(3, 7, chessPieces[7], "Queen", 0)
    cells[7][4] = Piece(4, 7, chessPieces[5], "King", 0)
    cells[7][5] = Piece(5, 7, chessPieces[11], "Bishop", 0)
    cells[7][6] = Piece(6, 7, chessPieces[9], "Knight", 0)
    cells[7][7] = Piece(7, 7, chessPieces[3], "Rook", 0)
    
def checkForImageMove():
    global pieceHeld, isPieceHeld
    mouse_pos = pygame.mouse.get_pos()
    cell_clicked = [0, 0]
    if mouse_pos[0] <= displaySize - 20 and mouse_pos[0] >= 20:
        if mouse_pos[1] <= displaySize - 20 and mouse_pos[1] >= 20:
            cell_clicked[0] = math.floor((mouse_pos[0] - 20) / 75)
            cell_clicked[1] = math.floor((mouse_pos[1] - 20) / 75)
            if cells[cell_clicked[1]][cell_clicked[0]] != None:
                pieceHeld = cells[cell_clicked[1]][cell_clicked[0]]
                isPieceHeld = True
                highlightCells(cells[cell_clicked[1]][cell_clicked[0]])

def placePiece():
    global pieceHeld, isPieceHeld, highlightedCells
    mouse_pos = pygame.mouse.get_pos()
    cell_over = [0, 0]
    if mouse_pos[0] <= displaySize - 20 and mouse_pos[0] >= 20:
        if mouse_pos[1] <= displaySize - 20 and mouse_pos[1] >= 20:
            cell_over[0] = math.floor((mouse_pos[0] - 20) / 75)
            cell_over[1] = math.floor((mouse_pos[1] - 20) / 75)
            if highlightedCells[cell_over[1]][cell_over[0]] == 1:
                cells[cell_over[1]][cell_over[0]] = pieceHeld
                cells[pieceHeld.y][pieceHeld.x] = None
                pieceHeld.move(cell_over[0], cell_over[1])
    pieceHeld = None
    isPieceHeld = False
    highlightedCells = [[0 for i in range(8)] for j in range(8)]

def highlightCells(piece):
    #pawn
    if piece.pieceType == "Pawn":
        if not ((piece.color == 0 and piece.y == 0) or (piece.color == 1 and piece.y == 7)): #To be removed?
            #left
            if not piece.x - 1 < 0:
                if cells[piece.y - 1 + 2*piece.color][piece.x - 1] != None and cells[piece.y - 1 + 2*piece.color][piece.x - 1].color != piece.color:
                    highlightedCells[piece.y - 1 + 2*piece.color][piece.x - 1] = 1
            #middle
            if cells[piece.y - 1 + 2*piece.color][piece.x] == None:
                highlightedCells[piece.y - 1 + 2*piece.color][piece.x] = 1
                if ((piece.color == 0 and piece.y == 6) or (piece.color == 1 and piece.y == 1)) and cells[piece.y - 2 + 4*piece.color][piece.x] == None:
                    highlightedCells[piece.y - 2 + 4*piece.color][piece.x] = 1

            #right
            if not piece.x + 1 > 7:
                if cells[piece.y - 1 + 2*piece.color][piece.x + 1] != None and cells[piece.y - 1 + 2*piece.color][piece.x + 1].color != piece.color:
                    highlightedCells[piece.y - 1 + 2*piece.color][piece.x + 1] = 1

    #rook    -------------------------------------------  
    elif piece.pieceType == "Rook":
        for i in range(1, 8):
            if piece.y - i >= 0:
                if cells[piece.y - i][piece.x] == None:
                    highlightedCells[piece.y - i][piece.x] = 1
                elif cells[piece.y - i][piece.x].color != piece.color:
                    highlightedCells[piece.y - i][piece.x] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y + i <= 7:
                if cells[piece.y + i][piece.x] == None:
                    highlightedCells[piece.y + i][piece.x] = 1
                elif cells[piece.y + i][piece.x].color != piece.color:
                    highlightedCells[piece.y + i][piece.x] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.x - i >= 0:
                if cells[piece.y][piece.x - i] == None:
                    highlightedCells[piece.y][piece.x - i] = 1
                elif cells[piece.y][piece.x - i].color != piece.color:
                    highlightedCells[piece.y][piece.x - i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.x + i <= 7:
                if cells[piece.y][piece.x + i] == None:
                    highlightedCells[piece.y][piece.x + i] = 1
                elif cells[piece.y][piece.x + i].color != piece.color:
                    highlightedCells[piece.y][piece.x + i] = 1
                    break
                else:
                    break
            else:
                break
    #knight--------------------------------------------------------
    elif piece.pieceType == "Knight":
        if piece.y - 2 >= 0:
            if piece.x + 1 <= 7:
                if cells[piece.y - 2][piece.x + 1] == None:
                    highlightedCells[piece.y - 2][piece.x + 1] = 1
                elif cells[piece.y - 2][piece.x + 1].color != piece.color:
                    highlightedCells[piece.y - 2][piece.x + 1] = 1
            if piece.x - 1 >= 0:
                if cells[piece.y - 2][piece.x - 1] == None:
                    highlightedCells[piece.y - 2][piece.x - 1] = 1
                elif cells[piece.y - 2][piece.x - 1].color != piece.color:
                    highlightedCells[piece.y - 2][piece.x - 1] = 1
        if piece.y + 2 <= 7:
            if piece.x + 1 <= 7:
                if cells[piece.y + 2][piece.x + 1] == None:
                    highlightedCells[piece.y + 2][piece.x + 1] = 1
                elif cells[piece.y + 2][piece.x + 1].color != piece.color:
                    highlightedCells[piece.y + 2][piece.x + 1] = 1
            if piece.x - 1 >= 0:
                if cells[piece.y + 2][piece.x - 1] == None:
                    highlightedCells[piece.y + 2][piece.x - 1] = 1
                elif cells[piece.y + 2][piece.x - 1].color != piece.color:
                    highlightedCells[piece.y + 2][piece.x - 1] = 1
        if piece.x - 2 >= 0:
            if piece.y + 1 <= 7:
                if cells[piece.y + 1][piece.x - 2] == None:
                    highlightedCells[piece.y + 1][piece.x - 2] = 1
                elif cells[piece.y + 1][piece.x - 2].color != piece.color:
                    highlightedCells[piece.y + 1][piece.x - 2] = 1
            if piece.y - 1 >= 0:
                if cells[piece.y - 1][piece.x - 2] == None:
                    highlightedCells[piece.y - 1][piece.x - 2] = 1
                elif cells[piece.y - 1][piece.x -2].color != piece.color:
                    highlightedCells[piece.y - 1][piece.x - 2] = 1
        if piece.x + 2 <= 7:
            if piece.y + 1 <= 7:
                if cells[piece.y + 1][piece.x + 2] == None:
                    highlightedCells[piece.y + 1][piece.x + 2] = 1
                elif cells[piece.y + 1][piece.x + 2].color != piece.color:
                    highlightedCells[piece.y + 1][piece.x + 2] = 1
            if piece.y - 1 >= 0:
                if cells[piece.y - 1][piece.x + 2] == None:
                    highlightedCells[piece.y - 1][piece.x + 2] = 1
                elif cells[piece.y - 1][piece.x + 2].color != piece.color:
                    highlightedCells[piece.y - 1][piece.x + 2] = 1
    # bishop -----------------------------------------------------------
    elif piece.pieceType == "Bishop":
        for i in range(1, 8):
            if piece.y - i >= 0 and piece.x - i >= 0:
                if cells[piece.y - i][piece.x - i] == None:
                    highlightedCells[piece.y - i][piece.x - i] = 1
                elif cells[piece.y - i][piece.x - i].color != piece.color:
                    highlightedCells[piece.y - i][piece.x - i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y + i <= 7 and piece.x - i >= 0:
                if cells[piece.y + i][piece.x - i] == None:
                    highlightedCells[piece.y + i][piece.x - i] = 1
                elif cells[piece.y + i][piece.x - i].color != piece.color:
                    highlightedCells[piece.y + i][piece.x - i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y - i >= 0 and piece.x + i <= 7:
                if cells[piece.y - i][piece.x + i] == None:
                    highlightedCells[piece.y - i][piece.x + i] = 1
                elif cells[piece.y - i][piece.x + i].color != piece.color:
                    highlightedCells[piece.y - i][piece.x + i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y + i <= 7 and piece.x + i <= 7:
                if cells[piece.y + i][piece.x + i] == None:
                    highlightedCells[piece.y + i][piece.x + i] = 1
                elif cells[piece.y + i][piece.x + i].color != piece.color:
                    highlightedCells[piece.y + i][piece.x + i] = 1
                    break
                else:
                    break
            else:
                break
    #kween --------------------------------------------------------------------
    elif piece.pieceType == "Queen":
        for i in range(1, 8):
            if piece.y - i >= 0:
                if cells[piece.y - i][piece.x] == None:
                    highlightedCells[piece.y - i][piece.x] = 1
                elif cells[piece.y - i][piece.x].color != piece.color:
                    highlightedCells[piece.y - i][piece.x] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y + i <= 7:
                if cells[piece.y + i][piece.x] == None:
                    highlightedCells[piece.y + i][piece.x] = 1
                elif cells[piece.y + i][piece.x].color != piece.color:
                    highlightedCells[piece.y + i][piece.x] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.x - i >= 0:
                if cells[piece.y][piece.x - i] == None:
                    highlightedCells[piece.y][piece.x - i] = 1
                elif cells[piece.y][piece.x - i].color != piece.color:
                    highlightedCells[piece.y][piece.x - i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.x + i <= 7:
                if cells[piece.y][piece.x + i] == None:
                    highlightedCells[piece.y][piece.x + i] = 1
                elif cells[piece.y][piece.x + i].color != piece.color:
                    highlightedCells[piece.y][piece.x + i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y - i >= 0 and piece.x - i >= 0:
                if cells[piece.y - i][piece.x - i] == None:
                    highlightedCells[piece.y - i][piece.x - i] = 1
                elif cells[piece.y - i][piece.x - i].color != piece.color:
                    highlightedCells[piece.y - i][piece.x - i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y + i <= 7 and piece.x - i >= 0:
                if cells[piece.y + i][piece.x - i] == None:
                    highlightedCells[piece.y + i][piece.x - i] = 1
                elif cells[piece.y + i][piece.x - i].color != piece.color:
                    highlightedCells[piece.y + i][piece.x - i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y - i >= 0 and piece.x + i <= 7:
                if cells[piece.y - i][piece.x + i] == None:
                    highlightedCells[piece.y - i][piece.x + i] = 1
                elif cells[piece.y - i][piece.x + i].color != piece.color:
                    highlightedCells[piece.y - i][piece.x + i] = 1
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if piece.y + i <= 7 and piece.x + i <= 7:
                if cells[piece.y + i][piece.x + i] == None:
                    highlightedCells[piece.y + i][piece.x + i] = 1
                elif cells[piece.y + i][piece.x + i].color != piece.color:
                    highlightedCells[piece.y + i][piece.x + i] = 1
                    break
                else:
                    break
            else:
                break
    #king ---------------------------------------------------------
    elif piece.pieceType == "King":
        if piece.y - 1 >= 0:
            if cells[piece.y - 1][piece.x] == None or cells[piece.y - 1][piece.x].color != piece.color:
                highlightedCells[piece.y - 1][piece.x] = 1
            if piece.x - 1 >= 0:
                if cells[piece.y - 1][piece.x - 1] == None or cells[piece.y - 1][piece.x - 1].color != piece.color:
                    highlightedCells[piece.y - 1][piece.x - 1] = 1
            if piece.x + 1 <= 7:
                if cells[piece.y - 1][piece.x + 1] == None or cells[piece.y - 1][piece.x + 1].color != piece.color:
                    highlightedCells[piece.y - 1][piece.x + 1] = 1

        if piece.y + 1 <= 7:
            if cells[piece.y + 1][piece.x] == None or cells[piece.y + 1][piece.x].color != piece.color:
                highlightedCells[piece.y + 1][piece.x] = 1
            if piece.x - 1 >= 0:
                if cells[piece.y + 1][piece.x - 1] == None or cells[piece.y + 1][piece.x - 1].color != piece.color:
                    highlightedCells[piece.y + 1][piece.x - 1] = 1
            if piece.x + 1 <= 7:
                if cells[piece.y + 1][piece.x + 1] == None or cells[piece.y + 1][piece.x + 1].color != piece.color:
                    highlightedCells[piece.y + 1][piece.x + 1] = 1

        if piece.x - 1 >= 0:
            if cells[piece.y][piece.x - 1] == None or cells[piece.y][piece.x - 1].color != piece.color:
                highlightedCells[piece.y][piece.x - 1] = 1
        if piece.x + 1 <= 7:
            if cells[piece.y][piece.x + 1] == None or cells[piece.y][piece.x + 1].color != piece.color:
                highlightedCells[piece.y][piece.x + 1] = 1

    #remove kings from highlights
    for y in range(8):
        for x in range(8):
            if cells[y][x] != None and cells[y][x].pieceType == "King":
                if highlightedCells[y][x] == 1:
                    highlightedCells[y][x] = 0

def pawnBeBetter(cell):
    pass

resetBoardCells()
while run:
    draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not isPieceHeld:
                checkForImageMove()
        elif event.type == pygame.MOUSEBUTTONUP:
            if isPieceHeld:
                placePiece()
                

pygame.quit()
