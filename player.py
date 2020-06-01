import pygame
from projectile import Projectile, Projectile2

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.credit = 0
        self.vel = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("images/vaisseau1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 285
        self.rect.y = 544

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.all_projectiles.add(Projectile2(self))

    def move_left(self):
        self.rect.x -= self.vel
        self.image = pygame.image.load("images/vaisseau1G.png").convert_alpha()

    def move_right(self):
        self.rect.x += self.vel
        self.image = pygame.image.load("images/vaisseau1D.png").convert_alpha()

    def move_up(self):
        self.rect.y -= self.vel
        self.image = pygame.image.load("images/vaisseau1.png").convert_alpha()

    def move_down(self):
        self.rect.y += self.vel
        self.image = pygame.image.load("images/vaisseau1.png").convert_alpha()