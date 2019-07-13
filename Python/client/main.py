# -*- coding: gb2312 -*-
import pygame
import sys, os
from components import scenes
from components import logger
from components.global_variable import *
from pygame.locals import *

pygame.init()

GLOBAL_LOGGER = logger.get_public_logger()

def main():
    GLOBAL_LOGGER.info('Game started!')
    pygame.display.set_icon(image('resources/icon_placeholder.png'))
    pygame.display.set_caption('Prophesy War a0.1')
    while True:
        action = scenes.main_menu.main()
        if action == 'play':
            scenes.interval.zoom_ball()
            room = scenes.select_room.main()
            if room:
                scenes.game.main()
            scenes.interval.shrink_ball()
        elif action == 'setting':
            setting()
        elif action == 'exit':
            break
    terminate()


def setting():
    pass


def game(sock):
    pass


def terminate():
    global_quit()  # global_variable


if __name__ == '__main__':
    main()
