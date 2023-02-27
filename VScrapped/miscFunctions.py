import grid as gd
import piece as pc
import copy

#Is (y, x) inside the board?
def outOfBoard(y, x):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return True
    return False

#if opposite color, you can capture it. King exception is left out for check testing. The king exception will be implemented in the 'move' function.
def canCapture(piece1, piece2):
    if piece1.color != piece2.color:
        return True
    return False

#Determine whether the King is in Check
def checkIfKingInCheck(grid, color, coords = ()):
    kingCoords = ()
    if coords == ():
        for row in grid:
            for cell in row:
                if cell != None and cell.typeOfPiece == "King" and cell.color == color:
                    kingCoords = (cell.coord[0], cell.coord[1])
    else:
        kingCoords = coords

    for row in grid:
        for cell in row:
            if cell != None and cell.color != color:
                movePossibilities = cell.determineAvailableMoves(grid, True)
                #if cell.typeOfPiece == "Queen":
                    #print(movePossibilities)

                for move in movePossibilities:
                    if move == (kingCoords[0], kingCoords[1]):
                        return True
    return False

def doesMoveSolveCheck(grid, piece, move):
    gridCopy = gd.Grid(grid.copy())

    cell1 = gridCopy.grid[move[0]][move[1]]
    cell2 = gridCopy.grid[piece.coord[0]][piece.coord[1]]
    gridCopy.deleteCellContents(move[0], move[1])
    gridCopy.grid[move[0]][move[1]] = gridCopy.grid[piece.coord[0]][piece.coord[1]]
    gridCopy.deleteCellContents(piece.coord[0], piece.coord[1])
    gridCopy.grid[move[0]][move[1]].changeCoordinates(move[0], move[1])
    
    if checkIfKingInCheck(gridCopy.grid, piece.color):
        gridCopy.grid[move[0]][move[1]].changeCoordinates(piece.coord[0], piece.coord[1])
        gridCopy.grid[move[0]][move[1]] = cell1
        gridCopy.grid[piece.coord[0]][piece.coord[1]] = cell2
        gridCopy = None
        return True
    gridCopy.grid[move[0]][move[1]].changeCoordinates(piece.coord[0], piece.coord[1])
    gridCopy.grid[move[0]][move[1]] = cell1
    gridCopy.grid[piece.coord[0]][piece.coord[1]] = cell2
    gridCopy = None
    return False
    

def returnLetterForPiece(x):
    if x == None:
        return " "
    elif x.typeOfPiece == "Knight":
        return "N"

    return x.typeOfPiece[0]
