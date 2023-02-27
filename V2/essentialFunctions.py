#Essential Functions [CHESS AI]


#Contains useful functions for the rest of the program

# MAJOR RULE OF THUMB: Y before X

def isNone(x):
  if x == None:
    return True
  return False

def returnLetterForPiece(x):
  if x == None:
    return " "
  elif x.typeOfPiece == "Knight":
    return "N"

  return x.typeOfPiece[0]

def outOfBoard(y, x):
  if x < 0 or x > 7 or y < 0 or y > 7:
    return True
  return False

#"Can piece1 be taken by piece2"
def canCapture(piece1, piece2):
  if piece1.color != piece2.color:
    return True
  return False

################################### ROOK
def checkRookMoves(grid, piece):
  availableMoves = []
  for i in range(-1, 2, 2):
    for j in range(1, 9):
      if not outOfBoard(piece.coord[0] + i*j, piece.coord[1]):
        if grid[piece.coord[0] + i*j][piece.coord[1]] == None:
          availableMoves.append((piece.coord[0] + i*j, piece.coord[1]))
        else:
          if canCapture(grid[piece.coord[0] + i*j][piece.coord[1]], grid[piece.coord[0]][piece.coord[1]]):
            availableMoves.append((piece.coord[0] + i*j, piece.coord[1]))
            break
          else:
            break
  for i in range(-1, 2, 2):
    for j in range(1, 9):
      if not outOfBoard(piece.coord[0], piece.coord[1] + i*j):
        if grid[piece.coord[0]][piece.coord[1] + i*j] == None:
          availableMoves.append((piece.coord[0], piece.coord[1] + i*j))
        else:
          if canCapture(grid[piece.coord[0]][piece.coord[1] + i*j], grid[piece.coord[0]][piece.coord[1]]):
            availableMoves.append((piece.coord[0], piece.coord[1] + i*j))
            break
          else:
            break
  return availableMoves

################################  BISHOP

def checkBishopMoves(grid, piece):
  availableMoves = []
  for i in range(-1, 2, 2):
    for j in range(1, 9):
      if not outOfBoard(piece.coord[0] + i*j, piece.coord[1] + j):
        if grid[piece.coord[0] + i*j][piece.coord[1] + j] == None:
          availableMoves.append((piece.coord[0] + i*j, piece.coord[1] + j))
        else:
          if canCapture(grid[piece.coord[0] + i*j][piece.coord[1] + j], grid[piece.coord[0]][piece.coord[1]]):
            availableMoves.append((piece.coord[0] + i*j, piece.coord[1] + j))
            break
          else:
            break
  for i in range(-1, 2, 2):
    for j in range(1, 9):
      if not outOfBoard(piece.coord[0] + i*j, piece.coord[1] - j):
        if grid[piece.coord[0] + i*j][piece.coord[1] - j] == None:
          availableMoves.append((piece.coord[0] + i*j, piece.coord[1] - j))
        else:
          if canCapture(grid[piece.coord[0] + i*j][piece.coord[1] - j], grid[piece.coord[0]][piece.coord[1]]):
            availableMoves.append((piece.coord[0] + i*j, piece.coord[1] - j))
            break
          else:
            break
  return availableMoves

######################################## KNIGHT

def checkKnightMoves(grid, piece):
  availableMoves = []

  for j in range (-1, 2, 2):
    for i in range(-1, 2, 2):
      if not outOfBoard(piece.coord[0] + j*2, piece.coord[1] - i):
        if grid[piece.coord[0] + j*2][piece.coord[1] - i] == None:
          availableMoves.append((piece.coord[0] + j*2, piece.coord[1] - i))
        else:
          if canCapture(grid[piece.coord[0] + j*2][piece.coord[1] - i], grid[piece.coord[0]][piece.coord[1]]):
            availableMoves.append((piece.coord[0] + j*2, piece.coord[1] - i))
  for j in range (-1, 2, 2):
    for i in range(-1, 2, 2):
      if not outOfBoard(piece.coord[0] + i, piece.coord[1] + j*2):
        if grid[piece.coord[0] + i][piece.coord[1] + j*2] == None:
          availableMoves.append((piece.coord[0] + i, piece.coord[1] + j*2))
        else:
          if canCapture(grid[piece.coord[0] + i][piece.coord[1] + j*2], grid[piece.coord[0]][piece.coord[1]]):
            availableMoves.append((piece.coord[0] + i, piece.coord[1] - j*2))
  return availableMoves

################################## PAWN

def checkPawnMoves(grid, piece):
  availableMoves = []

  if not piece.hasTakenFirstMove:
    if not outOfBoard(piece.coord[0] + (((piece.color * 2) - 1) * 2), piece.coord[1]):
      if grid[piece.coord[0] + (((piece.color * 2) - 1) * 2)][piece.coord[1]] == None:
        availableMoves.append((piece.coord[0] + (((piece.color * 2) - 1) * 2), piece.coord[1]))

  if not outOfBoard(piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1]):
      if grid[piece.coord[0] + ((piece.color * 2) - 1)][piece.coord[1]] == None:
          availableMoves.append((piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1]))
  
  for i in range(-1, 2, 2):
    if not outOfBoard(piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1] + i):
        if grid[piece.coord[0] + ((piece.color * 2) - 1)][piece.coord[1] + i] != None and canCapture(grid[piece.coord[0] + ((piece.color * 2) - 1)][piece.coord[1] + i], grid[piece.coord[0]][piece.coord[1]]):
            availableMoves.append((piece.coord[0] + ((piece.color * 2) - 1), piece.coord[1] + i))

  return availableMoves

############################################### KING

def checkKingMoves(grid, piece):
  availableMoves = []
  
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == j == 0:
        continue
      if not outOfBoard(piece.coord[0] + i, piece.coord[1] + j):
        if grid[piece.coord[0] + i][piece.coord[1] + j] == None:
          availableMoves.append((piece.coord[0] + i, piece.coord[1] + j))
        if grid[piece.coord[0] + i][piece.coord[1] + j] != None and canCapture(grid[piece.coord[0] + i][piece.coord[1] + j], grid[piece.coord[0]][piece.coord[1]]):
          availableMoves.append((piece.coord[0] + i, piece.coord[1] + j))

  return availableMoves

######################################################
def determineAvailableMoves(grid, piece):
  availableMoves = []
  if piece.typeOfPiece == "Rook":
    for move in checkRookMoves(grid, piece):
      availableMoves.append(move)

  elif piece.typeOfPiece == "Bishop":
    for move in checkBishopMoves(grid, piece):
      availableMoves.append(move)

  elif piece.typeOfPiece == "Queen":
    for move in checkBishopMoves(grid, piece):
      availableMoves.append(move)
    for move in checkRookMoves(grid, piece):
      availableMoves.append(move)

  elif piece.typeOfPiece == "Knight":
    for move in checkKnightMoves(grid, piece):
      availableMoves.append(move)

  elif piece.typeOfPiece == "Pawn":
    for move in checkPawnMoves(grid, piece):
      availableMoves.append(move)

  elif piece.typeOfPiece == "King":
    for move in checkKingMoves(grid, piece):
      availableMoves.append(move)
    
  return availableMoves

def printAvailableMoves(moves):
  for move in moves:
    print(move)
