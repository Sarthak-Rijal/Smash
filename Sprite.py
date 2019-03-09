import pygame
from pygame_functions import *

class Sprite(pygame.sprite.Sprite):

    ##constructor
    sprite_sheet = None

    def __init__(self, filename, frames):

        self.sprite_sheet = pygame.image.load(filename).convert()

    def getImage(self, x, y, width, height):
        """Grabes a single image out of a big sprtie sheet"""

        #blank image
        image = pygame.Surface([640,480], pygame.SRCALPHA, 32)
        image = image.convert_alpha()

        #copy the sprte form the large sheet onto the smaller one
        image.blit(self.sprite_sheet, (0,0), (x,y,width,height) )
        return image
        #assuming black workds as the transparent make the background transparent



