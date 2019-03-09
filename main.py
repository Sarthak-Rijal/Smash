import pygame
import sys
import random
import array
import math

pygame.init()

#arbritary screen size and setup 
size = (225, 136)
screen = pygame.display.set_mode(size)


#FPS
clock = pygame.time.Clock()
FPS = 60



def play():

 
    while True:

       #gets the mouse position
        x,y = pygame.mouse.get_pos()

        #event listner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #toggles full screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode(size)
                else:
                    pygame.display.set_mode(size, pygame.FULLSCREEN)

       



        pygame.display.update()
        clock.tick(FPS)

play()