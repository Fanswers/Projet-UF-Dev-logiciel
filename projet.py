import pygame
import time

pygame.init()
window = pygame.display.set_mode((600, 300))
myFont = pygame.font.SysFont("Arial", 60)
label = myFont.render("Hello pyGame!", 1, (255, 255, 0))
window.blit(label, (100, 100))
pygame.display.update()
time.sleep(5)
pygame.quit()
