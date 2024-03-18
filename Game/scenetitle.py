import asset
import const
import var
import UI

import pygame

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(asset.Font.neodgm_32.render('Platformer', False, const.Color.black), UI.Title.text_title)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_start, 2)
    var.screen.blit(asset.Font.neodgm_32.render('Start Game', False, const.Color.black), UI.Title.text_start)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_new, 2)
    var.screen.blit(asset.Font.neodgm_32.render('New Game', False, const.Color.black), UI.Title.text_new)
    pygame.display.flip()

def mouse_up(x, y, button):
    pass

def key_down(key):
    pass

def key_up(key):
    pass