#Game [CHESS AI]

#Plays a game

import essentialFunctions, os

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
      os.system("clear")
      num += 1

  def pygameGame(self):
    while True:
      self.ui.draw()
