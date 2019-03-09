import pygame

class Levels():
    """Generic class used to define a level"""

    #List of sprities used in all levels
    #there will be moving objects like pickups
    #There will be static platforms to walk on

    platform_list = None
    pickup_list = None

    background = None

    def __init__(self):
        pass

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        
        screen.blit(self.background, [0,0] )

        
class Level_01(Levels):

    def __init__(self):

        #Create Level 1
        Levels.__init__(self)    
        self.background = pygame.image.load("background.png")
