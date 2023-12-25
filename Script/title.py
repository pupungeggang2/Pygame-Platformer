import pygame

import var
import const
import UI

import physics

def loop():
    display()
    
def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(var.Font.main.render('Desserterria', False, const.Color.black), UI.UI.text_title)
    pygame.draw.rect(var.screen, const.Color.black, UI.UI.Title.button_start, 2)
    var.screen.blit(var.Font.main.render('Start Game', False, const.Color.black), UI.UI.Title.text_start)
    pygame.draw.rect(var.screen, const.Color.black, UI.UI.Title.button_erase, 2)
    var.screen.blit(var.Font.main.render('Erase Data', False, const.Color.black), UI.UI.Title.text_erase)
    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.pause == False:
            if var.state == '':
                if physics.point_inside_rect_array(x, y, UI.UI.Title.button_start):
                    var.scene = 'field'
                    var.state = ''