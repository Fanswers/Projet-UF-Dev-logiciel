import pygame, time
from pygame.locals import *
class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.atk = 10
        self.atk_base = 10
        self.swift = 1
        self.image = pygame.image.load('images/Vaisseau.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.x = 290
        self.rect.y = 530

    def move_right(self):
        self.rect.x += self.swift

    def move_left(self):
        self.rect.x -= self.swift