import pygame
from pygame_functions import *
from Sprite import *
from constants import *
from GameObject import *

imamePos = "PlayerImages/dummyCharacter/"
class character(GameObject):
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height        
        self.config = {'one': {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}, 'two': {'left':pygame.K_a, 'right':pygame.K_d }}

        #frames of walk left
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.stand_frame = []

        self.direction = "R"

        #loads the standing image
        image = pygame.image.load(imamePos+"standing/standing.png")
        actualImage = pygame.transform.scale(image,character1_size)
        self.stand_frame.append(actualImage)

        #loads running sitting images
        for i in range(8): 
            image = pygame.image.load(imamePos+"/running/"+str(i)+".png")
            actualImage = pygame.transform.scale(image, character1_size)
            self.walking_frames_r.append(actualImage)        
    
    def update(self, i, screen):
        screen.blit(self.walking_frames_r[i], (self.x,self.y)) 
            
    def move(self, speed, screen):
        keys = pygame.key.get_pressed()
        
        
        if keys[self.config[self.player]['left']]:
            self.x -= speed 
        if keys[self.config[self.player]['right']]:
            self.x += speed

        self.update(screen)
    