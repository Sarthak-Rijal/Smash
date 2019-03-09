import pygame
import sys
from util import view_width, view_height

class GameManager(object):
    def __init__(self, size=(800, 600), fullscreen=False):
        pygame.init()
        self.size = size
        if fullscreen:
            self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def start_game_loop(self, level):
        while True:
            self.loop()
            level.draw(self.screen)

    def loop(self):
        x,y = pygame.mouse.get_pos()
        # event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #toggles full screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if self.screen.get_flags() & pygame.FULLSCREEN:
                    #broken will fuck shit up, dont try
                    pygame.display.set_mode(size)
                else:
                    #broken will fuck shit up, dont try
                    pygame.display.set_mode(size, pygame.FULLSCREEN)
    



            pygame.display.update()
            self.clock.tick(self.FPS)