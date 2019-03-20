import pygame
from constants import *

class Sprite(object):

    ##constructor
    sprite_sheet = None

    def __init__(self, filename):

        #Load the sprite sheet
        self.sprite_sheet = pygame.image.load(filename).convert()

    def getImage(self, x, y, width, height):
        """Grabes a single image out of a big sprtie sheet"""

        #blank image
        image = pygame.Surface([width, height])
        

        #copy the sprte form the large sheet onto the smaller one
        image.blit(self.sprite_sheet, (0,0), (x,y,width,height) )
        alpha = image.get_at((0,0))
        image.set_colorkey(alpha)
        return image
        #assuming black workds as the transparent make the background transparent



