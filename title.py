import pygame
import var

i = 0

def loop():
    display()
    
def display():
    global i
    var.screen.fill((0, 0, 0))
    pygame.draw.rect(var.screen, (255, 255, 255), (i, 0, 80, 80))
    pygame.display.flip()
    i += 1
