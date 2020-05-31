import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 640))

#Affichage du fond
fond = pygame.image.load("images/backgroundPlay.jpg").convert()
fenetre.blit(fond, (0, 0))

#Affichage du vaisseau
vaisseau = pygame.image.load("images/vaisseau.png").convert_alpha()
vaisseauDroite = pygame.image.load("images/vaisseauDroite.png").convert_alpha()
vaisseauGauche = pygame.image.load("images/vaisseauGauche.png").convert_alpha()
position_vaisseau = vaisseau.get_rect()



#Rafraîchissement de l'écran
pygame.display.flip()


#Boucle infinie
continuer = 1
pygame.key.set_repeat(50, 5)

#Set vaisseau
vaisseauSpeed = 5
taille_vaisseau = vaisseau.get_rect().size
aff = 0



while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		pressed = pygame.key.get_pressed()
		if pressed[K_z] and position_vaisseau[1] > 0: #Si "touche z"
			position_vaisseau = position_vaisseau.move(0, -vaisseauSpeed)
			aff = 1
		if pressed[K_q] and position_vaisseau[0] > 0: #Si "touche q"
			position_vaisseau = position_vaisseau.move(-vaisseauSpeed, 0)
			aff = 2
		if pressed[K_s] and position_vaisseau[1] < 640 - taille_vaisseau[1]: #Si "touche s"
			position_vaisseau = position_vaisseau.move(0, vaisseauSpeed)
			aff = 1
		if pressed[K_d] and position_vaisseau[0] < 640 - taille_vaisseau[0]: #Si "touche d"
			position_vaisseau = position_vaisseau.move(vaisseauSpeed, 0)
			aff = 3
	#Re-collage
	fenetre.blit(fond, (0,0))
	if aff == 1:
		fenetre.blit(vaisseau, position_vaisseau)
	elif aff == 2:#afficher vaisseauGauche quand tourne à gauche
		fenetre.blit(vaisseauGauche, position_vaisseau)
	elif aff == 3:#afficher vaisseauDroite quand tourne à droite
		fenetre.blit(vaisseauDroite, position_vaisseau)

	#Rafraichissement
	pygame.display.flip()