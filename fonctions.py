import pygame, time
from pygame.locals import *
from game import Game

def credits(): ##### Fonction d'affichage des credits #####

    fenetre = pygame.display.set_mode((640, 640))

    fond = pygame.image.load("images/backgroundMenu.jpg").convert()

    arrow = pygame.image.load("images/arrow.png").convert()
    position_arrow = arrow.get_rect()
    position_arrow = position_arrow.move(100,100)
    fenetre.blit(arrow, position_arrow)

    myFont = pygame.font.SysFont("Arial", 50)
    Alexis = myFont.render("Alexis Larrode", 1, (255, 255, 0))
    Julien = myFont.render("Julien Cruz", 1, (255, 255, 0))
    Quitter = myFont.render("Quitter", 1, (255, 255, 0))

    cred = True
    while cred:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cred = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                cred = False

        fenetre.blit(fond, (0, 0))
        fenetre.blit(Alexis, (220, 200))
        fenetre.blit(Julien, (220, 300))
        fenetre.blit(arrow, (400, 580))
        fenetre.blit(Quitter, (510, 580))
        pygame.display.flip()



def play(): ##### Fonction de lancement du jeu #####

    # Ouverture de la fenêtre Pygame
    pygame.display.set_caption("Space shooter")
    fenetre = pygame.display.set_mode((640, 640))

    # Affichage du fond
    fond = pygame.image.load("images/backgroundPlay.jpg").convert()

    # Charger notre jeu
    game = Game()

    # Boucle infinie
    continuer = 1
    pygame.key.set_repeat(10, 10)

    while continuer:

        fenetre.blit(fond, (0, 0))

        # appliquer image joueur
        fenetre.blit(game.player.image, game.player.rect)

        # recuperer projectile joueur
        for projectile in game.player.all_projectiles:
            projectile.move()

        # Charger ensemble image groupe projectile
        game.player.all_projectiles.draw(fenetre)

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
            # tir joueur
            if event.type == KEYUP:
                if event.key == pygame.K_SPACE:
                    game.player.launch_projectile()
                    print("space")
