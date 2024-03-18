import sys
import pygame

import asset
import const
import var
import UI

import scenetitle
import scenefield

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.resolution)
    pygame.display.set_caption('Pygame Platformer')
    var.clock = pygame.time.Clock()

    load_image()
    load_font()

def main():
    while True:
        var.clock.tick(var.FPS)

        handle_input()
        handle_scene()

def load_image():
    pass

def load_font():
    pygame.font.init()
    asset.Font.neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'field':
        scenefield.loop()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]
            button = event.button

            if var.scene == 'title':
                scenetitle.mouse_up(x, y, button)

            elif var.scene == 'field':
                scenefield.mouse_up(x, y, button)

        elif event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_down(key)

            elif var.scene == 'scene':
                scenefield.key_down(key)

        elif event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_up(key)

            elif var.scene == 'scene':
                scenefield.key_up(key)

if __name__ == '__main__':
    init()
    main()