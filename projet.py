import pygame, time
import fonctions as fonc
from pygame.locals import *
import random
pygame.init()

fenetre = pygame.display.set_mode((640, 640))

fond = pygame.image.load("images/backgroundMenu.jpg")

arrow = pygame.image.load("images/arrow.png").convert_alpha()
position_arrow = arrow.get_rect()
position_arrow = position_arrow.move(100, 100)

myFont = pygame.font.SysFont("Arial", 50)
start = myFont.render("Jouer", 1, (255, 255, 0))
instruction = myFont.render("Instruction", 1, (255, 255, 0))
credit = myFont.render("Credits", 1, (255, 255, 0))
quitter = myFont.render("Quitter", 1, (255, 255, 0))

fenetre.blit(start, (150, 100))
fenetre.blit(instruction, (280, 200))
fenetre.blit(credit, (280, 300))
fenetre.blit(quitter, (280, 400))



cursorPos = 1 ### Variable qui permet de savoir ou se trouve la sélection du joueur dans le menu ###

lancement = True
while lancement: ##### Boucle principale / menu avant lancement u jeu #####
    pygame.key.set_repeat(400, 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lancement = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP and cursorPos != 1:
                position_arrow = position_arrow.move(0, -100)
                cursorPos -= 1
            elif event.key == K_DOWN and cursorPos != 4:
                position_arrow = position_arrow.move(0, 100)
                cursorPos += 1
            elif event.key == K_SPACE:
                if cursorPos == 1: ##################################### fonction play #####################################
                    fonc.sauvegarde()
                elif cursorPos == 2:
                    fonc.instruction()
                elif cursorPos == 3:  ##################################### fonction Credits #####################################
                    fonc.credits()
                elif cursorPos == 4:
                    lancement = False
                    pygame.quit()

    fenetre.blit(fond, (0, 0))
    fenetre.blit(arrow, position_arrow)
    fenetre.blit(start, (280, 100))
    fenetre.blit(instruction, (280, 200))
    fenetre.blit(credit, (280, 300))
    fenetre.blit(quitter, (280, 400))
    pygame.display.flip()


