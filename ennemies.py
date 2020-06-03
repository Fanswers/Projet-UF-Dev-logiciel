import pygame, pickle
import random
from pygame.locals import *

class Ennemies(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.swift = 2
        self.image = pygame.image.load('images/blueEnnemi.png')
        self.rect = self.image.get_rect()
        self.rect.y = -50
        self.rect.x = random.randint(0, 580)

    def forward(self):
        if not self.game.collider(self, self.game.all_player):
            self.rect.y += self.swift

    #fonction faire mourir ennemis
    def remove(self):
        self.game.all_ennemies.remove(self)

    #fonction faire subir des dommages aux ennemis
    def take_damage(self, amount):
        self.health -= amount

        if self.health <= 0: #Lorsque l'ennemi n'a plus de pv il se supprime et le joueur gagne des crédits
            self.remove()
            into = int(self.game.player.playerData[self.game.player.playerDataIdentify][1]) + 5
            self.game.player.playerData[self.game.player.playerDataIdentify][1] = str(into)
            pickle.dump(self.game.player.playerData, open("playerData.dat", "wb"))

            self.game.player.score += 1


        # Lorsque l'ennemi n'a plus que 50% de ses pdv, son apparence change
        if self.health <=50:
            self.image = pygame.image.load('images/blueEnnemiBroken.png')

    #fonction game over lorsqu'un ennemi touche le bas de l'écran
    def game_over(self):
        if self.rect.y >= 630:
            self.game.player.health -= 100

