from game_manager import GameManager
from Levels import *

Level1 = Level_01()
game = GameManager()
game.start_game_loop(Level1)

