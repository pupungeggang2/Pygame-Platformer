import pygame

import asset
import var
import const
import UI

def draw_player():
    pygame.draw.rect(var.screen, const.Color.black, var.Player.rect)

def draw_field():
    pass