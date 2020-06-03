from typing import List, Union

import pygame, pickle
from projectile import Projectile, Projectile2

take = pickle.load(open("playerData.dat", "rb"))
take[0][0] = 1
pickle.dump(take, open("playerData.dat", "wb"))

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.playerData = pickle.load(open("playerData.dat", "rb"))
        self.playerDataIdentify = int(self.playerData[0][0])
        print(self.playerData)
        self.credit = int(self.playerData[self.playerDataIdentify][1])
        self.vel = 7
        self.shootingDelay = 150
        self.atk = 50
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
        print(self.health)

    def take_damage(self):
        if self.game.collider(self, self.game.all_ennemies):
            self.health -= 100