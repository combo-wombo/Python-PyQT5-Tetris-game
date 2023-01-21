import pygame
import random
import os

class Speaker():
    pygame.mixer.init()
    current_dir = os.path.dirname (os.path.realpath(__file__))
    block_fallen                = "block_fallen.wav"
    death1                      = "death_1.wav"
    death2                      = "death_2.wav"
    generic_scroll_01           = "generic_scroll_01.wav"
    lvl1                        = "lvl1.wav"
    lvl2                        = "lvl2.wav"
    lvl3                        = "lvl3.wav"
    lvl4                        = "lvl4.wav"
    lvl5                        = "lvl5.wav"
    menu_accept                 = "menu_accept.wav"
    menu_back                   = "menu_back.wav"
    menu_focus                  = "menu_focus.wav"
    null                        = "null.wav"
    row_deleted                 = "row_deleted.wav"
    ui_menu_flip_single_01      = "ui_menu_flip_single_01.wav"
    ui_menu_flip_single_02      = "ui_menu_flip_single_02.wav"    

    def scroll():
        sound = random.randint(1,2)
        if sound == 1:
            Speaker.playsound(Speaker.obj(Speaker.ui_menu_flip_single_01))
        if sound == 2:
            Speaker.playsound(Speaker.obj(Speaker.ui_menu_flip_single_02))

    def obj(name):
        return pygame.mixer.Sound(os.path.join(Speaker.current_dir, "sounds\\"+name))

    def playsound(wave_obj, volume = 1.0):
        wave_obj.play()
        wave_obj.set_volume(volume)
        
    def play_death():
        sound = random.randint(1,2)
        if sound == 1:
            Speaker.playsound(Speaker.obj(Speaker.death1), 0.5)
        if sound == 2:
            Speaker.playsound(Speaker.obj(Speaker.death2), 0.5)
