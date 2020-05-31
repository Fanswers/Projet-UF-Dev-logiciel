import pygame
from game import Game
from pygame.locals import *
pygame.init()

# Ouverture de la fenêtre Pygame
pygame.display.set_caption("Space shooter")
fenetre = pygame.display.set_mode((640, 640))


# Affichage du fond
fond = pygame.image.load("images/backgroundPlay.jpg").convert()

# Charger notre jeu
game = Game()

# Boucle infinie
continuer = 1
pygame.key.set_repeat(50, 5)

while continuer:

    fenetre.blit(fond, (0, 0))

    # appliquer image joueur
    fenetre.blit(game.player.image, game.player.rect)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    for event in pygame.event.get():  # Attente des événements
        # fermeture fenetre
        if event.type == QUIT:
            continuer = 0
        # detecter mouvement joueur
        pressed = pygame.key.get_pressed()
        if pressed[K_q] and game.player.rect.x > 0:  # Si "touche q"
            game.player.move_left()
        if pressed[K_d] and game.player.rect.x < 640 - 69:  # Si "touche d"
            game.player.move_right()
        if pressed[K_z] and game.player.rect.y > 0:  # Si "touche z"
            game.player.move_up()
        if pressed[K_s] and game.player.rect.y < 640 - 96:  # Si "touche d"
            game.player.move_down()