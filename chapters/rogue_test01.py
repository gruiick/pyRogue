#!/usr/bin/env python3
# coding: utf-8
#
# $Id: rogue_test01.py 894 $
# SPDX-License-Identifier: BSD-2-Clause
#

"""
    from http://www.roguebasin.com/index.php?title=Roguelike_Tutorial,_using_python3%2Btdl,_part_1
"""

import tdl

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20


def handle_keys():
    global playerx, playery

    """
    # realtime-based game
    keypress = False
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
           user_input = event
           keypress = True
    if not keypress:
        return
    """

    # turn-based game
    user_input = tdl.event.key_wait()

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle fullscreen
        tdl.set_fullscreen(not tdl.get_fullscreen())
    elif user_input.key == 'ESCAPE':
        return True  # exit game

    # movement keys
    if user_input.key == 'UP':
        playery -= 1
    elif user_input.key == 'DOWN':
        playery += 1
    elif user_input.key == 'LEFT':
        playerx -= 1
    elif user_input.key == 'RIGHT':
        playerx += 1


tdl.set_font('dejavu10x10_gs_tc.png', greyscale=True, altLayout=True)
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen=False)
tdl.setFPS(LIMIT_FPS)  # for real-time game, ignore if turn-based

playerx = SCREEN_WIDTH // 2
playery = SCREEN_HEIGHT // 2

while not tdl.event.is_window_closed():
    console.draw_char(playerx, playery, '@', bg=None, fg=(255, 255, 255))
    tdl.flush()

    console.draw_char(playerx, playery, ' ', bg=None)
    # handle keys and exit game if needed
    exit_game = handle_keys()
    if exit_game:
        break
