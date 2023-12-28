import pygame

import var
import asset
import const
import UI
import data

import physics

def loop():
    display()
    
def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(asset.Font.main.render('Desserterria', False, const.Color.black), UI.UI.text_title)
    pygame.draw.rect(var.screen, const.Color.black, UI.UI.Title.button_start, 2)
    var.screen.blit(asset.Font.main.render('Start Game', False, const.Color.black), UI.UI.Title.text_start)
    pygame.draw.rect(var.screen, const.Color.black, UI.UI.Title.button_erase, 2)
    var.screen.blit(asset.Font.main.render('Erase Data', False, const.Color.black), UI.UI.Title.text_erase)

    var.screen.blit(asset.Image.arrow_right, UI.UI.Title.arrow_position[var.Selected.title])

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.pause == False:
            if var.state == '':
                if physics.point_inside_rect_array(x, y, UI.UI.Title.button_start):
                    var.scene = 'field'
                    var.state = ''
                    var.Selected.title = 0

def key_up(key):
    if var.pause == False:
        if var.state == '':
            if key == pygame.K_UP:
                if var.Selected.title > 0:
                    var.Selected.title -= 1
            
            if key == pygame.K_DOWN:
                if var.Selected.title < 1:
                    var.Selected.title += 1

            if key == pygame.K_RETURN:
                if var.Selected.title == 0:
                    var.scene = 'field'
                    var.state = ''
                    var.Selected.title = 0