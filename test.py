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





def play():

    nextFrame = pygame.time.get_ticks()
    frame = 0
    while True:
        if pygame.time.get_ticks() > nextFrame:
            frame = (frame+1)%8
            nextFrame += 10

        screen.fill((255,255,255))

      
        #event listner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        player = character(50,50,100,100)
        player.update(frame, screen)
        #drawing = Sprite("player.png")
        #screen.blit(drawing.getImage(5,0,35,50), (50,50))
        pygame.display.update()
        clock.tick(FPS)

play()