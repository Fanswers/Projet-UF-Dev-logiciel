import pygame, time
import fonctions as fonc
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480))
start = fonc.menu(fonc.play(),fonc.credits(fenetre), fenetre)