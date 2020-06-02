import pygame
from projectile import Projectile, Projectile2


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.credit = 0
        self.atk = 50
        self.vel = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("images/vaisseau.png").convert_alpha()
        self.affImg = 0
        self.rect = self.image.get_rect()
        self.rect.x = 285
        self.rect.y = 544

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.all_projectiles.add(Projectile2(self))

    def move_left(self):
        self.rect.x -= self.vel
        self.affImg = 1
        self.image = pygame.image.load("images/vaisseauGauche.png").convert_alpha()
        self.affImg = 0

    def move_right(self):
        self.rect.x += self.vel
        self.affImg = 1
        self.image = pygame.image.load("images/vaisseauDroite.png").convert_alpha()
        self.affImg = 0

    def move_up(self):
        self.rect.y -= self.vel
        if self.affImg != 1:
            self.image = pygame.image.load("images/vaisseau.png").convert_alpha()

    def move_down(self):
        self.rect.y += self.vel
        if self.affImg != 1:
            self.image = pygame.image.load("images/vaisseau.png").convert_alpha()
        print(self.health)

    def take_damage(self):
        if self.game.collider(self, self.game.all_ennemies):
            self.health -= 100