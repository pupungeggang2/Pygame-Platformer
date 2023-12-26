import pygame

import var
import asset
import const
import UI

import draw

import physics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    draw.draw_player()
    pygame.display.flip()

def mouse_up(x, y, button):
    pass

def key_down(key):
    pass

def key_up(key):
    pass