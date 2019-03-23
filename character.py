import pygame
from pygame_functions import *
from Sprite import *
from constants import *
from GameObject import *

imamePos = "PlayerImages/dummyCharacter/"
class character(GameObject):
    
    def __init__(self, x, y, width, height, playerNo):
        self.playerNo = playerNo
        self.x = x
        self.y = y
        self.width = width
        self.height = height        
        self.config = {'one': {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}, 'two': {'left':pygame.K_a, 'right':pygame.K_d }}
        self.nextFrame =  pygame.time.get_ticks()
        self.frame = 0
        
        self.animation = {}
        #default animation positon
        self.animation_pos = "stand"

        #frames of walk left
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.stand_frame = []


        #loads the standing image
        image = pygame.image.load(imamePos+"standing/standing.png")
        actualImage = pygame.transform.scale(image,character1_size)
        self.stand_frame.append(actualImage)
        self.animation["stand"] = self.stand_frame

        #loads running sprites
        for i in range(8): 
            image = pygame.image.load(imamePos+"/running/"+str(i)+".png")
            actualImage = pygame.transform.scale(image, character1_size)
            self.walking_frames_r.append(actualImage)
        self.animation["right_run"] = self.walking_frames_r

        for i in range(len(self.walking_frames_r)):
            image = pygame.transform.flip(self.walking_frames_r[i], True, False)
            self.walking_frames_l.append(image)
        self.animation["left_run"] = self.walking_frames_l
                
    
    def update(self, animate,  noSprites, speed, screen):
        #need to reset self.frame once the animation changes. 
        if pygame.time.get_ticks() > self.nextFrame:
            self.frame = (self.frame+1)%len(self.animation[animate])
            self.nextFrame += speed
        screen.blit(self.animation[animate][self.frame], (self.x,self.y)) 

            
    def move(self, noSprites, frameSpeed, speed, screen):
        keys = pygame.key.get_pressed()
        
        
        if keys[self.config[self.playerNo]['left']]:
            self.x -= speed 
            self.animation_pos = "left_run"
        elif keys[self.config[self.playerNo]['right']]:
            self.x += speed
            self.animation_pos = "right_run"
             # once the animation state changes, this resets the frame
        else:
            self.animation_pos = "stand"
            self.frame = 0 # once the animation state changes, this resets the frame

        self.update(self.animation_pos, noSprites, frameSpeed, screen)
    