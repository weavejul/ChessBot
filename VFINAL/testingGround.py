#Test Recusion

def findCurrentValue(grid):
    valueCurrent = 0
    for row in grid:
        for cell in row:
            if cell != None:
                valueCurrent += pieceValues[cell.typeOfPiece] * ((cell.color * -2) + 1
