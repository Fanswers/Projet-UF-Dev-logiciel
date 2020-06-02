import pygame, time
import random
from pygame.locals import *
from game import Game

def credits(): ##### Fonction d'affichage des credits #####

    fenetre = pygame.display.set_mode((640, 640))

    fond = pygame.image.load("images/backgroundMenu.jpg").convert()

    arrow = pygame.image.load("images/arrow.png").convert_alpha()
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

    # Création d'un userevent qui s'effectuera toutes les secondes et demies
    pygame.time.set_timer(USEREVENT, 1500)

    # Boucle infinie
    continuer = 1

    pygame.key.set_repeat(10, 10)

    while continuer:

        fenetre.blit(fond, (0, 0))

        # ajout d'un délait qui arrete le programme légérement pour que les déplacement soit plus lent
        pygame.time.delay(10)

        # appliquer image joueur
        fenetre.blit(game.player.image, game.player.rect)

        # recuperer projectile joueur
        for projectile in game.player.all_projectiles:
            projectile.move()

        # recuperer les monsters
        for ennemies in game.all_ennemies:
            ennemies.forward()

        # recuperer le joueur
        for player in game.all_player:
            player.take_damage()

        # Charger ensemble image groupe projectile
        game.player.all_projectiles.draw(fenetre)

        # Charger ensemble image groupe ennemis
        game.all_ennemies.draw(fenetre)





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
            if pressed[K_d] and game.player.rect.x < 640 - 74:  # Si "touche d"
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
                if event.key == pygame.K_d:
                    game.player .image = pygame.image.load("images/vaisseau.png").convert_alpha()
                if event.key == pygame.K_q:
                    game.player.image = pygame.image.load("images/vaisseau.png").convert_alpha()
            if event.type == USEREVENT: # User event toute les secondes et demis // Spawn d'ennemis
                AleaSpawn = random.randint(2, 4)
                i = 0
                while i < AleaSpawn:
                    game.Spawn_ennemies()
                    i += 1

        if game.player.health < 0:
            print("mort")

        print(game.player.credit)
        print()
