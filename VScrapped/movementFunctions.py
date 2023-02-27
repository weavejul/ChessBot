import miscFunctions, piece


#PIECE VARIABLES: MOVES TAKEN, CAN CASTLE?, COORDS, TYPE OF PIECE, COLOR (0 or 1)


#Find the moves possible for any given piece.

def determineMoves(grid, piece, checkOverride = False):

    #list of all moves found for the piece (including king captures)
    possibleMovesFound = []

    #Shadow moves are possible moves stored if a piece moves foward, like a king into a pawn's diagonals
    shadowMovesFound = []

    #Self-explanatory.
    if piece.typeOfPiece == "Rook":

        #CHANGING Y VALUES
        #Get -1 and 1
        for i in range(-1, 2, 2):
            #get numbers from 1 to 8
            for j in range(1, 9):
                #If its not out of the board,
                if not miscFunctions.outOfBoard(piece.coord[0] + i*j, piece.coord[1]):
                    #If its a blank space,
                    if grid[piece.coord[0] + i*j][piece.coord[1]] == None:
                        #append the move to the list
                        possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1]))
                    #Otheriwse,
                    else:
                        # If the space has a piece and its not the same color as the piece being moved,
                        if miscFunctions.canCapture(grid[piece.coord[0] + i*j][piece.coord[1]], grid[piece.coord[0]][piece.coord[1]]):
                            #Append that move
                            possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1]))
                            break
                        else:
                            break
        for i in range(-1, 2, 2):
            for j in range(1, 9):
                if not miscFunctions.outOfBoard(piece.coord[0], piece.coord[1] + i*j):
                    if grid[piece.coord[0]][piece.coord[1] + i*j] == None:
                        possibleMovesFound.append((piece.coord[0], piece.coord[1] + i*j))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0]][piece.coord[1] + i*j], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0], piece.coord[1] + i*j))
                            break
                        else:
                            break
    
    #Bishop Moves ----------------------------------------

    elif piece.typeOfPiece == "Bishop":

        for i in range(-1, 2, 2):
            for j in range(1, 9):
                if not miscFunctions.outOfBoard(piece.coord[0] + i*j, piece.coord[1] + j):
                    if grid[piece.coord[0] + i*j][piece.coord[1] + j] == None:
                        possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1] + j))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0] + i*j][piece.coord[1] + j], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1] + j))
                            break
                        else:
                            break
        for i in range(-1, 2, 2):
            for j in range(1, 9):
                if not miscFunctions.outOfBoard(piece.coord[0] + i*j, piece.coord[1] - j):
                    if grid[piece.coord[0] + i*j][piece.coord[1] - j] == None:
                        possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1] - j))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0] + i*j][piece.coord[1] - j], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1] - j))
                            break
                        else:
                            break

    #Knight moves --------------------------------------------------------

    elif piece.typeOfPiece == "Knight":

        for j in range (-1, 2, 2):
            for i in range(-1, 2, 2):
                if not miscFunctions.outOfBoard(piece.coord[0] + j*2, piece.coord[1] - i):
                    if grid[piece.coord[0] + j*2][piece.coord[1] - i] == None:
                        possibleMovesFound.append((piece.coord[0] + j*2, piece.coord[1] - i))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0] + j*2][piece.coord[1] - i], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0] + j*2, piece.coord[1] - i))
        for j in range (-1, 2, 2):
            for i in range(-1, 2, 2):
                if not miscFunctions.outOfBoard(piece.coord[0] + i, piece.coord[1] + j*2):
                    if grid[piece.coord[0] + i][piece.coord[1] + j*2] == None:
                        possibleMovesFound.append((piece.coord[0] + i, piece.coord[1] + j*2))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0] + i][piece.coord[1] + j*2], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0] + i, piece.coord[1] + j*2))


    #Queen moves -----------------------------------------
    elif piece.typeOfPiece == "Queen":
        
        for i in range(-1, 2, 2):
            for j in range(1, 9):
                if not miscFunctions.outOfBoard(piece.coord[0] + i*j, piece.coord[1] + j):
                    if grid[piece.coord[0] + i*j][piece.coord[1] + j] == None:
                        possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1] + j))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0] + i*j][piece.coord[1] + j], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1] + j))
                            break
                        else:
                            break
        for i in range(-1, 2, 2):
            for j in range(1, 9):
                if not miscFunctions.outOfBoard(piece.coord[0] + i*j, piece.coord[1] - j):
                    if grid[piece.coord[0] + i*j][piece.coord[1] - j] == None:
                        possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1] - j))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0] + i*j][piece.coord[1] - j], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1] - j))
                            break
                        else:
                            break
    
        #Rook Part
        for i in range(-1, 2, 2):
            for j in range(1, 9):
                if not miscFunctions.outOfBoard(piece.coord[0] + i*j, piece.coord[1]):
                    if grid[piece.coord[0] + i*j][piece.coord[1]] == None:
                        possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1]))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0] + i*j][piece.coord[1]], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0] + i*j, piece.coord[1]))
                            break
                        else:
                            break
        for i in range(-1, 2, 2):
            for j in range(1, 9):
                if not miscFunctions.outOfBoard(piece.coord[0], piece.coord[1] + i*j):
                    if grid[piece.coord[0]][piece.coord[1] + i*j] == None:
                        possibleMovesFound.append((piece.coord[0], piece.coord[1] + i*j))
                    else:
                        if miscFunctions.canCapture(grid[piece.coord[0]][piece.coord[1] + i*j], grid[piece.coord[0]][piece.coord[1]]):
                            possibleMovesFound.append((piece.coord[0], piece.coord[1] + i*j))
                            break
                        else:
                            break

    # Pawn moves --------------------------------------

    elif piece.typeOfPiece == "Pawn":

        if piece.movesTaken == 0:
            if not miscFunctions.outOfBoard(piece.coord[0] + (((piece.color * 2) - 1) * 2), piece.coord[1]):
                if grid[piece.coord[0] + (((piece.color * 2) - 1) * 2)][piece.coord[1]] == None and grid[piece.coord[0] + ((piece.color * 2) - 1)][piece.coord[1]] == None:
                    possibleMovesFound.append((piece.coord[0] + (((piece.color * 2) - 1) * 2), piece.coord[1]))

        if not miscFunctions.outOfBoard(piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1]):
                if grid[piece.coord[0] + ((piece.color * 2) - 1)][piece.coord[1]] == None:
                    possibleMovesFound.append((piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1]))

        for i in range(-1, 2, 2):
            if not miscFunctions.outOfBoard(piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1] + i):
                if grid[piece.coord[0] + ((piece.color * 2) - 1)][piece.coord[1] + i] != None and miscFunctions.canCapture(grid[piece.coord[0] + ((piece.color * 2) - 1)][piece.coord[1] + i], grid[piece.coord[0]][piece.coord[1]]):
                    possibleMovesFound.append((piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1] + i))
        
        if piece.color + 3 == piece.coord[0]:
            for i in range(-1, 2, 2):
                if not miscFunctions.outOfBoard(piece.coord[0], piece.coord[1] + i):
                    if not grid[piece.coord[0]][piece.coord[1] + i] == None and grid[piece.coord[0]][piece.coord[1] + i].color != piece.color and grid[piece.coord[0]][piece.coord[1] + i].movesTaken == 1:
                        if grid[piece.coord[0] + ((piece.color * 2) - 1)][piece.coord[1] + i] == None:
                            possibleMovesFound.append((piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1] + i))

    #King moves -------------------------------------------------

    elif piece.typeOfPiece == "King":
  
        if piece.canCastle:
            if grid[piece.coord[0]][7].movesTaken != None:
                if grid[piece.coord[0]][7].movesTaken == 0 and grid[piece.coord[0]][6] == grid[piece.coord[0]][5] == None:
                    possibleMovesFound.append((piece.coord[0], 6))
                if grid[piece.coord[0]][0].movesTaken == 0 and grid[piece.coord[0]][1] == grid[piece.coord[0]][2] == grid[piece.coord[0]][3] == None:
                    possibleMovesFound.append((piece.coord[0], 2))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                if not miscFunctions.outOfBoard(piece.coord[0] + i, piece.coord[1] + j):
                    if grid[piece.coord[0] + i][piece.coord[1] + j] == None:
                        possibleMovesFound.append((piece.coord[0] + i, piece.coord[1] + j))
                    if grid[piece.coord[0] + i][piece.coord[1] + j] != None and miscFunctions.canCapture(grid[piece.coord[0] + i][piece.coord[1] + j], grid[piece.coord[0]][piece.coord[1]]):
                        possibleMovesFound.append((piece.coord[0] + i, piece.coord[1] + j))

    #If in check, where can you move
    if not checkOverride:
        
        if miscFunctions.checkIfKingInCheck(grid, piece.color):
            tempPossMoves = []
            for move in possibleMovesFound:
                if miscFunctions.doesMoveSolveCheck(grid, piece, move):
                    tempPossMoves.append(move)
            possibleMovesFound = tempPossMoves.copy()

        #remove kings
        tempPossMoves2 = []
        for move in possibleMovesFound:
            try:
                if grid[move[0]][move[1]] == None or not grid[move[0]][move[1]].typeOfPiece == "King":
                    tempPossMoves2.append(move)
            except:
                print(move)

        possibleMovesFound = tempPossMoves2
    
    return possibleMovesFound
