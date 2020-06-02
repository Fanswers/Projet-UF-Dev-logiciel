import pygame

# Class projectile
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.vel = 4
        self.player = player
        self.image = pygame.image.load("images/projectile.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 50

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.vel

        # On vérifié si le projectile entre en collision avec un ennemi
        for ennemies in self.player.game.collider(self, self.player.game.all_ennemies):
            #Supression du projectile au contact des ennemis
            self.remove()

            #Inflige des dégats a l'ennemi en contact avec le projectile
            ennemies.take_damage(self.player.atk)

        # verifier si projectile hors ecran
        if self.rect.y < 0:
            self.remove()

class Projectile2(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.vel = 4
        self.player = player
        self.image = pygame.image.load("images/projectile.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 65
        self.rect.y = player.rect.y + 50

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.vel

        # On vérifié si le projectile entre en collision avec un ennemi
        for ennemies in self.player.game.collider(self, self.player.game.all_ennemies):
            #Supression du projectile au contact des ennemis
            self.remove()

            #Inflige des dégats a l'ennemi en contact avec le projectile
            ennemies.take_damage(self.player.atk)

        # verifier si projectile hors ecran
        if self.rect.y < 0:
            self.remove()