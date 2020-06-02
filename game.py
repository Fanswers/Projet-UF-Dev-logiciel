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
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_ennemies = pygame.sprite.Group()


    def Spawn_ennemies(self):
        tabSpawn= [0, 64, 128, 192, 256, 320, 384, 448, 512, 576]
        AleaSpawn = random.randint(2, 4)
        i = 0
        x = 9
        while i < AleaSpawn:
            AleaSpawn2 = random.randint(0, x)
            ennemies = Ennemies(self)
            ennemies.rect.x = tabSpawn[AleaSpawn2]
            tabSpawn.pop(AleaSpawn2)
            x -= 1
            self.all_ennemies.add(ennemies)
            i += 1

    def collider(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


