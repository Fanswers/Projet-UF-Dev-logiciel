import pygame

# Class projectile
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.vel = 15
        self.player = player
        self.image = pygame.image.load("images/projectile.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 50

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.vel

        # verifier si projectile hors ecran
        if self.rect.y < 0:
            self.remove()

class Projectile2(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.vel = 15
        self.player = player
        self.image = pygame.image.load("images/projectile.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 65
        self.rect.y = player.rect.y + 50

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.vel

        # verifier si projectile hors ecran
        if self.rect.y < 0:
            self.remove()