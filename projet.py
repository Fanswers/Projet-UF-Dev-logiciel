import pygame, time
import fonctions as fonc
import classes as cla
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640, 640))
# start = fonc.menu(fonc.play(),fonc.credits(fenetre), fenetre)
start = fonc.play()