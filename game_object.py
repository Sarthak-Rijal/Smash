import pygame
from util import normalize

WHITE = (255, 255, 255)

class GameObject(pygame.sprite.Sprite):
    # controls is a dict containing the keys left, right with their respective keys
    def __init__(self, position, dimensions, size):
        pygame.sprite.Sprite.__init__(self)
        self.width = normalize(dimensions[0], size[0])
        self.height = normalize(dimensions[1], size[1])
        self.size = size
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = normalize(position[0], size[0])
        self.rect.y = normalize(position[1], size[1])

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def did_collide(self, sprite):
        return self.rect.colliderect(sprite.rect)


class Player(GameObject):
    def __init__(self, position, dimensions, size, controls):
        GameObject.__init__(self, position, dimensions, size)
        self.controls = controls
        self.falling = False

    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[self.controls['left']]:
            self.move(-10, 0)
        if pressed_key[self.controls['right']]:
            self.move(10, 0)
        if self.falling:
            self.move(0, 20)
