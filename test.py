import pygame
from character import *

pygame.init()

#arbritary screen size and setup 
size = (2255, 1360)
screen = pygame.display.set_mode(size)


#FPS
clock = pygame.time.Clock()
FPS = 60


ROW = 30#rows
COL = 50#columns

#GLOBAL CELL ATTRIBUTES

#global reference to time


def play():

    char1= pygame.time.get_ticks()
    char1_Frame = 0
    while True:
        

        screen.fill((255,255,255))

      
        #event listner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player = character(50,50,100,100)
        char1_Frame, char1 = player.update(char1, char1_Frame, 8, 80, screen)
        #drawing = Sprite("player.png")
        #screen.blit(drawing.getImage(5,0,35,50), (50,50))
        pygame.display.update()
        clock.tick(FPS)

play()