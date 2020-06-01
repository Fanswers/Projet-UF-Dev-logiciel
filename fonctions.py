import pygame, time
from pygame.locals import *
import classes as cla

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

    fenetre = pygame.display.set_mode((640, 640))
    fond = pygame.image.load("images/backgroundPlay.jpeg").convert()

    game = cla.Game() ########### Initialisation de la classe Game qui elle meme contient tout les classes###########

    jouer = True
    while jouer:
        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 590:
            game.player.move_right()
        elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
            game.player.move_left()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jouer = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

        fenetre.blit(fond, (0, 0))
        fenetre.blit(game.player.image, game.player.rect)
        pygame.display.flip()