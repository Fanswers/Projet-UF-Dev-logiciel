import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.credit = 0
        self.vel = 5
        self.image = pygame.image.load("images/vaisseau.png").convert_alpha()
        self.affImg = 0
        self.rect = self.image.get_rect()
        self.rect.x = 285
        self.rect.y = 544

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