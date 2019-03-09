import pygame

class game_object():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def update(self, screen):
        pygame.draw.rect(screen, (0,0,0), [self.x,self.y,self.width,self.height])

    