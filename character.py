import pygame
from game_object import game_object

class character(game_object):
    
    def __init__(self, x, y, width, height, player):
        super().__init__(x,y,width,height)
        self.player = player
        self.config = {'one': {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}, 'two': {'left':pygame.K_a, 'right':pygame.K_d }}

    def update(self, screen):
        pygame.draw.rect(screen, (0,0,0), [self.x,self.y,self.width,self.height])

    def move(self, speed, screen):
        keys = pygame.key.get_pressed()
        
        
        if keys[self.config[self.player]['left']]:
            self.x -= speed 
        if keys[self.config[self.player]['right']]:
            self.x += speed

        self.update(screen)
    