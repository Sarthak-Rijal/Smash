import pygame
import sys
from game_object import GameObject, Player

class GameManager(object):
    def __init__(self, size=(800*2, 600*2), fullscreen=False):
        pygame.init()
        self.size = size
        if fullscreen:
            self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        # Initialize players
        self.players = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        platform_dimensions = (500, 50)
        platform_position = (500-int(platform_dimensions[0]/2), 600)
        player_one_dimensions = (100, 150)
        player_two_dimensions = (150, 200)
        player_one_position = (platform_position[0] , platform_position[1] - int(player_one_dimensions[1]))
        player_two_position = (platform_position[0] + platform_dimensions[0] - player_two_dimensions[0], platform_position[1] - int(player_two_dimensions[1]))
        player_one = Player(player_one_position, player_one_dimensions, self.size, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT})
        player_two = Player(player_two_position, player_two_dimensions, self.size, {'left': pygame.K_j, 'right': pygame.K_k})
        self.players.add(player_one)
        self.players.add(player_two)
        platform = GameObject(platform_position, platform_dimensions, self.size)
        self.platform_group.add(platform)
        self.FPS = 60

    def start_game_loop(self):
        while True:
            self.loop()

    def loop(self):
        # REAL GAME CODE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        # Draw / render
        self.players.update()
        self.platform_group.update()
        self.screen.fill((0, 0, 0))
        self.players.draw(self.screen)
        self.platform_group.draw(self.screen)

        pygame.display.update()
        self.clock.tick(self.FPS)