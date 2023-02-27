#Main [CHESS AI]

import grid, piece, essentialFunctions, ui, game, pygame


board = grid.Grid()
ui = ui.UserInterface(board)
game = game.Game(board, ui)

board.initializeStandardBoard()

game.textBasedGame()
