import pygame, time
import random
from pygame.locals import *
from game import Game

def instruction(): ##### Fonction d'affichage des credits #####

    fenetre = pygame.display.set_mode((640, 640))

    fond = pygame.image.load("images/backgroundMenu.jpg").convert()

    arrow = pygame.image.load("images/arrow.png").convert_alpha()
    Blue = pygame.image.load("images/blueEnnemi.png").convert()
    Gray = pygame.image.load("images/grayEnnemi.png").convert()
    Purple = pygame.image.load("images/purpleEnnemi.png").convert()
    Red = pygame.image.load("images/redEnnemi.png").convert()
    Yellow = pygame.image.load("images/yellowEnnemi.png").convert()




    myFont = pygame.font.SysFont("Arial", 45)
    ToucheZ = myFont.render("Z : HAUT", 1, (255, 255, 0))
    ToucheQ = myFont.render("Q : GAUCHE", 1, (255, 255, 0))
    ToucheS = myFont.render("S : BAS", 1, (255, 255, 0))
    ToucheD = myFont.render("D : DROITE", 1, (255, 255, 0))
    Espace = myFont.render("ESPACE : TIRER", 1, (255, 255, 0))
    ToucheM = myFont.render("M : MAGASIN", 1, (255, 255, 0))
    Quitter = myFont.render("Quitter", 1, (255, 255, 0))
    Continuer = myFont.render("Continuer", 1, (255, 255, 0))

    Regle = myFont.render("Ne pas laisser les blocs vous toucher,", 1, (255, 255, 0))
    Regle2 = myFont.render("ni atteindre le bas de l'écran .", 1, (255, 255, 0))
    Regle3 = myFont.render("Survivre le plus longtemps !", 1, (255, 255, 0))





    myFontdesc = pygame.font.SysFont("Arial", 30)
    DescBlue = myFontdesc.render("Normal", 1, (255, 255, 0))
    DescRed = myFontdesc.render("Résistant", 1, (255, 255, 0))
    DescPurple = myFontdesc.render("Rapide", 1, (255, 255, 0))
    DescGray = myFontdesc.render("Très résistant / lent", 1, (255, 255, 0))
    DescYellow = myFontdesc.render("Bonus", 1, (255, 255, 0))




    cred = True
    while cred:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cred = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                cred = False

        fenetre.blit(fond, (0, 0))
        fenetre.blit(ToucheZ, (100, 50))
        fenetre.blit(ToucheQ, (100, 100))
        fenetre.blit(ToucheS, (100, 150))
        fenetre.blit(ToucheD, (100, 200))
        fenetre.blit(Espace, (100, 250))
        fenetre.blit(ToucheM, (100, 300))
        fenetre.blit(Blue, (50, 400))
        fenetre.blit(DescBlue, (150, 400))
        fenetre.blit(Red, (300, 400))
        fenetre.blit(DescRed, (400, 400))
        fenetre.blit(Purple, (50, 450))
        fenetre.blit(DescPurple, (150, 450))
        fenetre.blit(Gray, (300, 450))
        fenetre.blit(DescGray, (400, 450))
        fenetre.blit(Yellow, (50, 500))
        fenetre.blit(DescYellow, (150, 500))
        fenetre.blit(arrow, (370, 580))
        fenetre.blit(Continuer, (455, 580))
        pygame.display.flip()

    cred2 = True
    while cred2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cred2 = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                cred2 = False

        fenetre.blit(fond, (0, 0))
        fenetre.blit(Regle, (20, 100))
        fenetre.blit(Regle2, (20, 150))
        fenetre.blit(Regle3, (20, 250))
        fenetre.blit(arrow, (400, 580))
        fenetre.blit(Quitter, (510, 580))
        pygame.display.flip()


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


    # Variable de défaite
    gameover = False

    ############ Initialisation des variables des prix du shop #############
    prixAtk = 50
    maxAtk = 5
    ComptAtk = 0
    prixVitAtk = 50
    maxVitAtk = 5
    ComptVitAtk = 0
    prixVit = 100
    maxVit = 3
    ComptVit = 0
    prixChance = 1000
    maxChance = 2
    ComptChance = 1


    # Boucle infinie
    continuer = True
    t = 0
    while continuer:
        pygame.time.delay(10)
        pygame.key.set_repeat(400, 30)
        fenetre.blit(fond, (0, 0))

        # ajout d'un délait qui arrete le programme légérement pour que les déplacement soit plus lent
        pygame.time.delay(10)

        # appliquer image joueur
        fenetre.blit(game.player.image, game.player.rect)

        if game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
            game.player.move_left()
        if game.pressed.get(pygame.K_d) and game.player.rect.x < 640 - 69:
            game.player.move_right()
        if game.pressed.get(pygame.K_z) and game.player.rect.y > 0:
            game.player.move_up()
        if game.pressed.get(pygame.K_s) and game.player.rect.y < 640 - 96:
            game.player.move_down()
        if game.pressed.get(pygame.K_SPACE):
            if pygame.time.get_ticks() > (t + game.player.shootingDelay):
                game.player.launch_projectile()
                t = pygame.time.get_ticks()

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
            pressed = pygame.key.get_pressed()
            # fermeture fenetre
            if event.type == QUIT:
                continuer = False
            # detecter mouvement joueur

            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == K_p: ###################################### MAGASIN ######################################
                    fondShop = pygame.image.load("images/backgroundMenu.jpg").convert()
                    myFont = pygame.font.SysFont("Arial", 85)
                    myFont2 = pygame.font.SysFont("Arial", 45)
                    myFont3 = pygame.font.SysFont("Arial", 30)
                    Shop = myFont.render("Magasin", 1, (255, 255, 0))
                    Quitter = myFont2.render("Quitter", 1, (255, 255, 0))
                    Atk = myFont3.render("Attaque :", 1, (255, 255, 0))
                    VitAtk = myFont3.render("Vit d'attaque :", 1, (255, 255, 0))
                    Vit = myFont3.render("Vitesse :", 1, (255, 255, 0))
                    Chance = myFont3.render("Chance :", 1, (255, 255, 0))

                    arrowShop = pygame.image.load("images/arrow.png").convert_alpha()
                    position_arrowShop = arrowShop.get_rect()
                    position_arrowShop = position_arrowShop.move(30, 350)




                    shop = True
                    cursorShop = 0
                    while shop: ############Boucle du Shop#############
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                shop = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == K_p:
                                    shop = False
                                elif event.key == K_UP and cursorShop == 3:
                                    position_arrowShop = position_arrowShop.move(0, -100)
                                    cursorShop = 1
                                elif event.key == K_UP and cursorShop == 4:
                                    position_arrowShop = position_arrowShop.move(0, -100)
                                    cursorShop = 2
                                elif event.key == K_UP and cursorShop == 5:
                                    position_arrowShop = position_arrowShop.move(-120, -130)
                                    cursorShop = 4
                                elif event.key == K_DOWN and cursorShop == 1 or event.key == K_DOWN and cursorShop == 0:
                                    position_arrowShop = position_arrowShop.move(0, 100)
                                    cursorShop = 3
                                elif event.key == K_DOWN and cursorShop == 2 or event.key == K_DOWN and cursorShop == 0:
                                    position_arrowShop = position_arrowShop.move(0, 100)
                                    cursorShop = 4
                                elif event.key == K_DOWN and cursorShop == 3:
                                    position_arrowShop = position_arrowShop.move(390, 130)
                                    cursorShop = 5
                                elif event.key == K_DOWN and cursorShop == 4:
                                    position_arrowShop = position_arrowShop.move(120, 130)
                                    cursorShop = 5
                                elif event.key == K_RIGHT and cursorShop == 1 or event.key == K_RIGHT and cursorShop == 0:
                                    position_arrowShop = position_arrowShop.move(270, 0)
                                    cursorShop = 2
                                elif event.key == K_RIGHT and cursorShop == 3:
                                    position_arrowShop = position_arrowShop.move(270, 0)
                                    cursorShop = 4
                                elif event.key == K_LEFT and cursorShop == 2:
                                    position_arrowShop = position_arrowShop.move(-270, 0)
                                    cursorShop = 1
                                elif event.key == K_LEFT and cursorShop == 4:
                                    position_arrowShop = position_arrowShop.move(-270, 0)
                                    cursorShop = 3

                                elif event.key == K_SPACE:
                                    if cursorShop == 1 and game.player.credit > prixAtk and ComptAtk < maxAtk:
                                        game.player.credit -= prixAtk
                                        prixAtk = prixAtk * 2
                                        ComptAtk += 1
                                    if cursorShop == 2 and game.player.credit > prixVitAtk and ComptVitAtk < maxVitAtk:
                                        game.player.credit -= prixVitAtk
                                        prixVitAtk = prixVitAtk * 2
                                        ComptVitAtk += 1
                                    if cursorShop == 3 and game.player.credit > prixVit and ComptVit < maxVit:
                                        game.player.credit -= prixVit
                                        prixVit = prixVit * 2
                                        ComptVit += 1
                                    if cursorShop == 4 and game.player.credit > prixChance and ComptChance < maxChance:
                                        game.player.credit -= prixChance
                                        prixChance = prixChance * 2
                                        ComptChance += 1
                                        game.Ennemies5.proba += 1
                                        print("Achat effectué")
                                        print(game.Ennemies5.proba)
                                    if cursorShop == 5:
                                        shop = False


                        fenetre.blit(fondShop, (0, 0))
                        fenetre.blit(arrowShop, position_arrowShop)
                        fenetre.blit(Atk, (120, 357))

                        fenetre.blit(VitAtk, (390, 357))

                        fenetre.blit(Vit, (120, 457))

                        fenetre.blit(Chance, (390, 457))

                        fenetre.blit(Quitter, (510, 580))
                        fenetre.blit(Shop, (200, 150))
                        pygame.display.flip()


            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
                if event.key == K_q:
                    game.player.image = pygame.image.load("images/vaisseau1.png").convert_alpha()
                if event.key == K_d:
                    game.player.image = pygame.image.load("images/vaisseau1.png").convert_alpha()



            if event.type == USEREVENT: # User event toute les secondes et demis // Spawn d'ennemis
                    game.Spawn_ennemies()


        if game.player.health < 0:
            gameover = True
            continuer = False



    if gameover == True:
        fond = pygame.image.load("images/backgroundMenu.jpg").convert()
        myFont = pygame.font.SysFont("Arial", 85)
        myFont2 = pygame.font.SysFont("Arial", 45)
        Fin = myFont.render("GAME OVER", 1, (255, 255, 0))
        Score = myFont2.render("score :", 1, (255, 255, 0))
        #Credit = game.player.credit
        #Score2 = myFont2.render(Credit, 1, (255, 255, 0))
        print("mort")
        end = True
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    end = False
            fenetre.blit(fond, (0, 0))
            fenetre.blit(Fin, (100, 150))
            fenetre.blit(Score, (120, 300))
            #fenetre.blit(Score2, (200, 250))
            pygame.display.flip()








