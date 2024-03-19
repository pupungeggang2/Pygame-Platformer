import asset
import const
import var
import UI

import fdraw
import fphysics

import pygame

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    pygame.draw.rect(var.screen, const.Color.black, UI.Field.button_menu, 2)

    if var.menu == True:
        fdraw.draw_menu()

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.menu == True:
            if fphysics.point_inside_rect_array(x, y, UI.Menu.button_resume):
                var.menu = False

            if fphysics.point_inside_rect_array(x, y, UI.Menu.button_exit):
                var.menu = False
                var.scene = 'title'
                var.state = ''

        if var.menu == False:
            if fphysics.point_inside_rect_array(x, y, UI.Field.button_menu):
                var.menu = True

            if var.state == '':
                pass

def key_down(key):
    pass

def key_up(key):
    pass