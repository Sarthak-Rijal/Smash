import pygame
import sys
from game_object import GameObject, Player

class GameManager(object):
    def __init__(self, size=(1280, 720), fullscreen=False):
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
        platform_dimensions = (400, 50)
        platform_position = (500-int(platform_dimensions[0]/2), 600)
        player_one_dimensions = (100, 150)
        player_two_dimensions = (100, 200)
        player_one_position = (platform_position[0], platform_position[1] - int(player_one_dimensions[1]))
        player_two_position = (platform_position[0] + platform_dimensions[0] - player_two_dimensions[0], platform_position[1] - int(player_two_dimensions[1]))
        player_one_controls = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}
        player_two_controls = {'left': pygame.K_j, 'right': pygame.K_k}
        self.player_one = Player(player_one_position, player_one_dimensions, self.size, player_one_controls)
        self.player_two = Player(player_two_position, player_two_dimensions, self.size, player_two_controls)
        self.players.add(self.player_one)
        self.players.add(self.player_two)
        self.platform = GameObject(platform_position, platform_dimensions, self.size)
        self.platform_group.add(self.platform)
        self.FPS = 60

    def start_game_loop(self):
        while True:
            self.loop()

    def loop(self):
        # REAL GAME CODE
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit(0)
        # Draw / render
        if self.player_one.did_collide(self.platform):
            self.player_one.falling = False
        else:
            self.player_one.falling = True

        if self.player_two.did_collide(self.platform):
            self.player_two.falling = False
        else:
            self.player_two.falling = True
        self.players.update()
        self.platform_group.update()
        self.screen.fill((0, 23, 0))
        self.players.draw(self.screen)
        self.platform_group.draw(self.screen)
        pygame.display.update()
        self.clock.tick(self.FPS)