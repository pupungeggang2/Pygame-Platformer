import pygame
import sys

import var
import asset

import title
import field

var.clock = pygame.time.Clock()

def main():
    var.screen = pygame.display.set_mode([1280, 800])
    pygame.display.set_caption('Desserterria-Platform')
    load_font()
    load_image()
    
def loop():
    while True:
        var.clock.tick(60)
        
        loop_scene()
        input_handle()
        
def loop_scene():
    if var.scene == 'title':
        title.loop()

    elif var.scene == 'field':
        field.loop()
    
def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            button = event.button

            if var.scene == 'title':
                title.mouse_up(x, y, button)

            elif var.scene == 'field':
                field.mouse_up(x, y, button)
        
        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'field':
                field.key_down(key)
        
        if event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'title':
                title.key_up(key)

            elif var.scene == 'field':
                field.key_up(key)

def load_font():
    pygame.font.init()
    asset.Font.main = pygame.font.Font('../Font/neodgm.ttf', 32)

def load_image():
    asset.Image.arrow_right = pygame.image.load('../Image/ArrowRight.png')

main()
loop()
