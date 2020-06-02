import pygame
import random
from player import Player
from ennemies import Ennemies
from ennemies2 import Ennemies2
from ennemies3 import Ennemies3
from ennemies4 import Ennemies4
from ennemies5 import Ennemies5

class Game :

    def __init__(self):
        # generer joueur nouvelle partie
        self.player = Player(self)
        self.Ennemies5 = Ennemies5(self)
        self.pressed = {}
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self.player)
        self.all_ennemies = pygame.sprite.Group()



    def Spawn_ennemies(self, SpawnMin, SpawnMax):
        tabSpawn= [0, 64, 128, 192, 256, 320, 384, 448, 512, 576]

        AleaSpawn = random.randint(SpawnMin, SpawnMax)
        i = 0
        x = 9
        while i < AleaSpawn:
            AleaSpawn2 = random.randint(0, x)
            AleaSpawn3 = random.randint(0, 100)
            if AleaSpawn3 <= self.Ennemies5.proba:
                ennemies = Ennemies5(self)
                ennemies.rect.x = tabSpawn[AleaSpawn2]
                tabSpawn.pop(AleaSpawn2)
                x -= 1
                self.all_ennemies.add(ennemies)
                i += 1
            elif AleaSpawn3 > self.Ennemies5.proba and AleaSpawn3 <= 7:
                ennemies = Ennemies4(self)
                ennemies.rect.x = tabSpawn[AleaSpawn2]
                tabSpawn.pop(AleaSpawn2)
                x -= 1
                self.all_ennemies.add(ennemies)
                i += 1
            elif AleaSpawn3 > 7 and AleaSpawn3 <= 17:
                ennemies = Ennemies2(self)
                ennemies.rect.x = tabSpawn[AleaSpawn2]
                tabSpawn.pop(AleaSpawn2)
                x -= 1
                self.all_ennemies.add(ennemies)
                i += 1
            elif AleaSpawn3 > 17 and AleaSpawn3 <= 37:
                ennemies = Ennemies3(self)
                ennemies.rect.x = tabSpawn[AleaSpawn2]
                tabSpawn.pop(AleaSpawn2)
                x -= 1
                self.all_ennemies.add(ennemies)
                i += 1
            elif AleaSpawn3 > 37 and AleaSpawn3 <= 100:
                ennemies = Ennemies(self)
                ennemies.rect.x = tabSpawn[AleaSpawn2]
                tabSpawn.pop(AleaSpawn2)
                x -= 1
                self.all_ennemies.add(ennemies)
                i += 1

    def collider(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


