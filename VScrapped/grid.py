import piece, movementFunctions, miscFunctions, pygame

#The grid class represent the board itself, with pieces interacting on it
class Grid():
    def __init__(self, grid = None):
        self.previousMove = []
        if grid != None:
            self.grid = grid
        else:
            self.grid = [[None for i in range(8)] for j in range(8)]
        self.chessPieces = [pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_pdt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_plt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_rdt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_rlt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_kdt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_klt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_qdt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_qlt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_ndt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_nlt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_bdt60.png"),
               pygame.image.load(r"C:\Users\mrwum\OneDrive\Desktop\Chess AI\ChessImages\Chess_blt60.png"),]

    #Sets the board to the standard chess game beginning
    def initializeStandardBoard(self):
        self.gridArray = [[None for i in range(8)] for j in range(8)]
        for i in range(8):
            self.grid[1][i] = piece.Piece("Pawn", 1, (1, i), self.chessPieces[0])
            self.grid[6][i] = piece.Piece("Pawn", 0, (6, i), self.chessPieces[1])
        for i in range(2):
            self.grid[0][i * 7] = piece.Piece("Rook", 1, (0, i*7), self.chessPieces[2])
            self.grid[7][i * 7] = piece.Piece("Rook", 0, (7, i*7), self.chessPieces[3])
        for i in range(2):
            self.grid[0][(i*5)+1] = piece.Piece("Knight", 1, (0, (i*5)+1), self.chessPieces[8])
            self.grid[7][(i*5)+1] = piece.Piece("Knight", 0, (7, (i*5)+1), self.chessPieces[9])
        for i in range(2):
            self.grid[0][(i*3)+2] = piece.Piece("Bishop", 1, (0, (i*3)+2), self.chessPieces[10])
            self.grid[7][(i*3)+2] = piece.Piece("Bishop", 0, (7, (i*3)+2), self.chessPieces[11])

        self.grid[0][3] = piece.Piece("Queen", 1, (0, 3), self.chessPieces[6])
        self.grid[7][3] = piece.Piece("Queen", 0, (7, 3), self.chessPieces[7])
        self.grid[0][4] = piece.Piece("King", 1, (0, 4), self.chessPieces[4], True, 0)
        self.grid[7][4] = piece.Piece("King", 0, (7, 4), self.chessPieces[5], True, 0)
        ####
        #self.grid[2][2] = piece.Piece("King", 0, (2, 2))
        ####

    #Deletes the content of a cell
    def deleteCellContents(self, y, x):
        self.grid[y][x] = None

    #Moves a piece from one cell to another
    def movePiece(self, y1, x1, y2, x2):
        global previousMove
        
        self.deleteCellContents(y2, x2)
        self.grid[y2][x2] = self.grid[y1][x1]
        self.deleteCellContents(y1, x1)
        self.grid[y2][x2].changeCoordinates(y2, x2)
        
        self.grid[y2][x2].hasTakenFirstMove = True
        self.grid[y2][x2].canCastle = False

        if self.grid[y2][x2].typeOfPiece == "King":
            if abs(x2-x1) > 1:
                if x2 == 2:
                    self.movePiece(y1, 0, y1, 3)
                elif x2 == 6:
                    self.movePiece(y1, 7, y1, 5)

        elif self.grid[y2][x2].typeOfPiece == "Pawn":
            if abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
                self.deleteCellContents(y2 - (2 * self.grid[y2][x2].color - 1), x2)
            
        if y2 == self.grid[y2][x2].color * 7 and self.grid[y2][x2].typeOfPiece == "Pawn":
            promotion = input("Promote to:")
            if promotion.lower() == "q":
                self.grid[y2][x2] = piece.Piece("Queen", self.grid[y2][x2].color, (y2, x2), self.chessPieces[7 - self.grid[y2][x2].color])
            elif promotion.lower() == "k":
                self.grid[y2][x2] = piece.Piece("Knight", self.grid[y2][x2].color, (y2, x2), self.chessPieces[9 - self.grid[y2][x2].color])
            elif promotion.lower() == "b":
                self.grid[y2][x2] = piece.Piece("Bishop", self.grid[y2][x2].color, (y2, x2), self.chessPieces[11 - self.grid[y2][x2].color])
            elif promotion.lower() == "r":
                self.grid[y2][x2] = piece.Piece("Rook", self.grid[y2][x2].color, (y2, x2), self.chessPieces[3 - self.grid[y2][x2].color])


        self.grid[y2][x2].changeCastlePlusMoveState()
        previousMove = (y2, x2)

        

    #Prints the board state (for debugging)
    def printBoard(self):
        
        print("   0   1   2   3   4   5   6   7  X")
        for i in range(8):
            print(str(i) + " |", end = "")
            for j in range(8):
                if j == 7:
                    print(miscFunctions.returnLetterForPiece(self.grid[i][j]) + "|")
                else:
                    print((miscFunctions.returnLetterForPiece(self.grid[i][j])) + " | ", end = "")
            if i != 7:
                print("  |" + ("----" * 7) + "-|") 
