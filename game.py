import pygame
import random
from player import Player
from ennemies import Ennemies

class Game :

    def __init__(self):
        # generer joueur nouvelle partie
        self.player = Player(self)
        self.pressed = {}
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self.player)
        self.all_ennemies = pygame.sprite.Group()
        self.Spawn_ennemies()
        self.Spawn_ennemies()

    def Spawn_ennemies(self):
        ennemies = Ennemies(self)
        self.all_ennemies.add(ennemies)

    def collider(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


