from typing import List, Union

import pygame, pickle
from projectile import Projectile, Projectile2

take = pickle.load(open("playerData.dat", "rb"))
take[0][0] = 1
#take = [[1], ['new', '0', '50', '150'], ['new', '0', '50', '150'], ['new', '0', '50', '150'],[0]]
#take2 = [['0', '500', '0', '500'], ['0', '500', '0', '500'], ['0', '500', '0', '500']]
pickle.dump(take, open("playerData.dat", "wb"))
#pickle.dump(take2, open("shopData.dat", "wb"))

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
        self.score = 0
        self.atk = int(self.playerData[self.playerDataIdentify][2])
        self.shootingDelay = int(self.playerData[self.playerDataIdentify][3])
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("images/vaisseau1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 285
        self.rect.y = 544
        #shopData
        self.playerDataShop = pickle.load(open("shopData.dat", "rb"))
        self.playerDataIdentifyShop = int(self.playerData[0][0]) - 1
        self.comptAtk = int(self.playerDataShop[self.playerDataIdentifyShop][0])
        self.prixAtk = int(self.playerDataShop[self.playerDataIdentifyShop][1])
        self.comptVitAtk = int(self.playerDataShop[self.playerDataIdentifyShop][2])
        self.prixVitAtk = int(self.playerDataShop[self.playerDataIdentifyShop][3])
        print(self.playerDataShop)

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

    def take_damage(self):
        if self.game.collider(self, self.game.all_ennemies):
            self.health -= 100