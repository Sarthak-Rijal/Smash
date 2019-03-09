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

    def start_game_loop(self):
        while True:
            self.loop()

    def loop(self):
        x,y = pygame.mouse.get_pos()
        print(view_width(1000, self.size[0]))
        # event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #toggles full screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if self.screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode(size)
                else:
                    pygame.display.set_mode(size, pygame.FULLSCREEN)
    



            pygame.display.update()
            self.clock.tick(self.FPS)