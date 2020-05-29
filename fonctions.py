import pygame, time
from pygame.locals import *

def menu(Play, credits, fenetre):


    fond = pygame.image.load("images/backgroundMenu.jpg").convert()
    fenetre.blit(fond, (0, 0))

    arrow = pygame.image.load("images/arrow.png").convert()
    position_arrow = arrow.get_rect()
    position_arrow = position_arrow.move(100,100)
    fenetre.blit(arrow, position_arrow)

    myFont = pygame.font.SysFont("Arial", 50)
    start = myFont.render("Jouer", 1, (255, 255, 0))
    instruction = myFont.render("Instruction", 1, (255, 255, 0))
    credit = myFont.render("Credits", 1, (255, 255, 0))
    quitter = myFont.render("Quitter", 1, (255, 255, 0))

    fenetre.blit(start, (150, 100))
    fenetre.blit(instruction, (280, 200))
    fenetre.blit(credit, (280, 300))
    fenetre.blit(quitter, (280, 400))

    pygame.key.set_repeat(400, 30)

    continuer = True
    cursorPos = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP and cursorPos != 1:
                    position_arrow = position_arrow.move(0, -100)
                    cursorPos -= 1
                if event.key == K_DOWN and cursorPos != 4:
                    position_arrow = position_arrow.move(0,100)
                    cursorPos += 1
                if event.key == K_SPACE:
                    if cursorPos == 1:
                        Play
                    if cursorPos == 2:
                        print("select 2")
                    if cursorPos == 3: ##################################### Credits #####################################
                        credits
                        print("lance crédit")
                    if cursorPos == 4:
                        continuer = False

        fenetre.blit(fond, (0, 0))
        fenetre.blit(arrow, position_arrow)
        fenetre.blit(start, (280, 100))
        fenetre.blit(instruction, (280, 200))
        fenetre.blit(credit, (280, 300))
        fenetre.blit(quitter, (280, 400))
        pygame.display.flip()

def credits(fenetre): #Test mais fonctionne pas du coup direct dans la fonction menu


    fond = pygame.image.load("images/backgroundMenu.jpg").convert()
    fenetre.blit(fond, (0, 0))

    arrow = pygame.image.load("images/arrow.png").convert()
    position_arrow = arrow.get_rect()
    position_arrow = position_arrow.move(100,100)
    fenetre.blit(arrow, position_arrow)


    myFont = pygame.font.SysFont("Arial", 50)

    Alexis = myFont.render("Alexis Larrode", 1, (255, 255, 0))
    Julien = myFont.render("Julien Cruz", 1, (255, 255, 0))
    Quitter = myFont.render("Quitter", 1, (255, 255, 0))
    credits = True
    while credits:
        for event in pygame.event.get():
            if event.type == QUIT:
                credits = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    credits = False


        fenetre.blit(fond, (0, 0))
        fenetre.blit(Alexis, (220, 200))
        fenetre.blit(Julien, (220, 300))
        fenetre.blit(arrow, (400, 580))
        fenetre.blit(Quitter, (510, 580))
        pygame.display.flip()

def play():
    pygame.init()
    fenetre = pygame.display.set_mode((640, 640))

    fond = pygame.image.load("images/backgroundPlay.jpeg").convert()
    fenetre.blit(fond, (0, 0))

    jouer = True
    while jouer:
        for event in pygame.event.get():
            if event.type == QUIT:
                jouer = False

        fenetre.blit(fond, (0, 0))
        pygame.display.flip()