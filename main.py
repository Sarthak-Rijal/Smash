from game_manager import GameManager
from Levels import *

game = GameManager()
Level1 = Level_01(game.size)
game.start_game_loop(Level1)
