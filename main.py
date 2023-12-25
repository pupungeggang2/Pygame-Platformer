import pygame
import sys

import var

import title

var.clock = pygame.time.Clock()

def main():
    var.screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Desserterria-Platform')
    
def loop():
    while True:
        var.clock.tick(60)
        
        loop_scene()
        input_handle()
        
def loop_scene():
    if var.scene == 'title':
        title.loop()
    
def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
        
        if event.type == pygame.KEYDOWN:
            key = event.key
        
        if event.type == pygame.KEYUP:
            key = event.key
        
main()
loop()
