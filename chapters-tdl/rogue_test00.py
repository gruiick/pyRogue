#!/usr/bin/env python3
# coding: utf-8
#
# $Id: rogue_test00.py 876 $
# SPDX-License-Identifier: BSD-2-Clause
#

"""
    http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod (python2)
    http://www.roguebasin.com/index.php?title=Roguelike_Tutorial,_using_python3%2Btdl (python3)
    Unused code and variants
"""

import tdl
from tcod import image_load
from random import randint
import math
import textwrap
import shelve
import roguecolors


def handle_keys():
    """
        This version use keypad (hence KP?). Not tested.
    """
    global fov_recompute
    global mouse_coord

    keypress = False
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
            user_input = event
            keypress = True
        if event.type == 'MOUSEMOTION':
            mouse_coord = event.cell

    if not keypress:
        return 'didnt-take-turn'

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle fullscreen
        tdl.set_fullscreen(not tdl.get_fullscreen())

    elif user_input.key == 'ESCAPE':
        return 'exit'  # exit game

    if game_state == 'playing':
        # movement keys
        if user_input.key == 'UP' or user_input.key == 'KP8':
            player_move_or_attack(0, -1)
        elif user_input.key == 'DOWN' or user_input.key == 'KP2':
            player_move_or_attack(0, 1)
        elif user_input.key == 'LEFT' or user_input.key == 'KP4':
            player_move_or_attack(-1, 0)
        elif user_input.key == 'RIGHT' or user_input.key == 'KP6':
            player_move_or_attack(1, 0)
        elif user_input.key == 'HOME' or user_input.key == 'KP7':
            player_move_or_attack(-1, -1)
        elif user_input.key == 'PAGEUP' or user_input.key == 'KP9':
            player_move_or_attack(1, -1)
        elif user_input.key == 'END' or user_input.key == 'KP1':
            player_move_or_attack(-1, 1)
        elif user_input.key == 'PAGEDOWN' or user_input.key == 'KP3':
            player_move_or_attack(1, 1)
        elif user_input.key == 'KP5':
            pass  # do nothing ie wait for the monster to come to you


# TODO: Item potion of Vision (1/100)
def place_objects(room):

    item_chances['vision'] = from_dungeon_level([[4, 1]])
    item_chances['sword'] = from_dungeon_level([[2, 10], [3, 5], [5, 0]])
    item_chances['axe'] = from_dungeon_level([[4, 5]])
    item_chances['shield'] = from_dungeon_level([[1, 5], [5, 0]])
    item_chances['elfic shield'] = from_dungeon_level([[4, 6]])

                elif choice == 'vision':
                # create a vision scroll (1% chance)
                item_component = Item(use_function=cast_vision)
                item = GameObject(x, y, '#', 'scroll of vision',
                                  roguecolors.light_yellow, item=item_component)



            elif choice == 'sword':
                # create a sword
                equipment_component = Equipment(slot='right hand', power_bonus=3)
                item = GameObject(x, y, '/', 'sword', roguecolors.sky,
                                  equipment=equipment_component)
            elif choice == 'axe':
                # create an axe
                equipment_component = Equipment(slot='right hand', power_bonus=3)
                item = GameObject(x, y, 'T', 'axe', roguecolors.sky,
                                  equipment=equipment_component)
            elif choice == 'shield':
                # create a shield
                equipment_component = Equipment(slot='left hand', defense_bonus=1)
                item = GameObject(x, y, '[', 'shield', roguecolors.darker_orange,
                                  equipment=equipment_component)
            elif choice == 'elfic shield':
                # create an elfic shield
                equipment_component = Equipment(slot='left hand', defense_bonus=1)
                item = GameObject(x, y, '[', 'elfic shield', roguecolors.darker_green,
                                  equipment=equipment_component)


def cast_vision():
    """
        reveal all rooms and tunnels
    """
    global my_map
    message('All rooms and tunnels are now revealed', roguecolors.light_blue)

    # go through all tiles, and set their background color
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            my_map[x][y].explored = True


# TODO: Fighter Mimic (imite un Item, avec une attaque et une puissance trés faible, 1/100)
# dans "def place_objects(room):"

                # create a mimic (1% chance)
                fighter_component = Fighter(hp=1, defense=1, power=1, xp=50,
                                            death_function=monster_death)
                ai_component = BasicMonster()
                # créer le mimic dans sa fonction à lui
                monster = GameObject(x, y, 'o', 'orc',
                                     roguecolors.light_green,
                                     blocks=True, fighter=fighter_component,
                                     ai=ai_component)


# Unused code (variants)

def random_choice_index(chances):
    """
        choose one option from list of chances, returning its index
        the dice will land on some number between 1 and the sum of the
        chances
    """
    #dice = libtcod.random_get_int(0, 1, sum(chances))
    dice = randint(1, sum(chances))

    # go through all chances, keeping the sum so far
    running_sum = 0
    choice = 0
    for w in chances:
        running_sum += w

        # see if the dice landed in the part that corresponds to this choice
        if dice <= running_sum:
            return choice
        choice += 1


monster_chances = [80, 20]
item_chances = [70, 10, 10, 10]

# et dans place_objects()
choice = random_choice_index(item_chances)
if choice == 0:
    #create a healing potion
