#!/usr/bin/env python3
# coding: utf-8
#
# $Id: rogue_test05.py 896 $
# SPDX-License-Identifier: BSD-2-Clause
#

"""
    from http://www.roguebasin.com/index.php?title=Roguelike_Tutorial,_using_python3%2Btdl,_part_5
    http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/color.html?c=false&cpp=false&cs=false&py=true&lua=false
"""

import tdl
from random import randint
import roguecolors

# actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# size of the map
MAP_WIDTH = 80
MAP_HEIGHT = 45

# parameters for dungeon generator
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30
MAX_ROOM_MONSTERS = 3

# FOV algorithm, can be BASIC, DIAMOND, SHADOW, PERMISSIVE0 to 9
FOV_ALGO = 'BASIC'
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

REALTIME = False
LIMIT_FPS = 20  # 20 frames-per-second maximum, for realtime mode

color_dark_wall = roguecolors.darkest_grey
color_light_wall = roguecolors.light_grey
color_dark_ground = roguecolors.darkest_sepia
color_light_ground = roguecolors.dark_sepia


class Tile:
    """
        a tile of the map with its properties
    """
    def __init__(self, blocked, block_sight=None):
        """ """
        self.blocked = blocked
        self.explored = False

        # by default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight


class Rect:
    """
        a rectangle on the map. used to characterize a room.
    """
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return (center_x, center_y)

    def intersect(self, other):
        # returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


class GameObject:
    """
        this is a generic object: the player, a monster, an item, stairs...
        it's always represented by a character on screen.
    """
    def __init__(self, x, y, char, name, color, blocks=False):
        """ """
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.color = color
        self.blocks = blocks

    def move(self, dx, dy):
        """
            move by the given amount, if the destination is not blocked
        """
        if not is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def draw(self):
        """
            draw the character that represents this object at its position
            only show if it's visible to the player
        """
        global visible_tiles

        if (self.x, self.y) in visible_tiles:
            con.draw_char(self.x, self.y, self.char, self.color, bg=None)

    def clear(self):
        """
            erase the character that represents this object
        """
        con.draw_char(self.x, self.y, ' ', self.color, bg=None)


def is_blocked(x, y):
    """ """
    # first test the map tile
    if my_map[x][y].blocked:
        return True

    # now check for any blocking objects
    for obj in objects:
        if obj.blocks and obj.x == x and obj.y == y:
            return True
        else:
            return False


def place_objects(room):
    """ """
    # choose random number of monsters
    num_monsters = randint(0, MAX_ROOM_MONSTERS)

    for i in range(num_monsters):
        # choose random spot for this monster
        x = randint(room.x1, room.x2)
        y = randint(room.y1, room.y2)

        # only place it if the tile is not blocked
        if not is_blocked(x, y):
            if randint(0, 100) < 80:  # 80% chance of getting an orc
                # create an orc
                monster = GameObject(x, y, 'o', 'orc',
                                     roguecolors.desaturated_green,
                                     blocks=True)
            else:
                # create a troll
                monster = GameObject(x, y, 'T', 'troll',
                                     roguecolors.darker_green,
                                     blocks=True)

            objects.append(monster)


def create_room(room):
    """ """
    global my_map
    # go through the tiles in the rectangle and make them passable
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            my_map[x][y].blocked = False
            my_map[x][y].block_sight = False


def create_h_tunnel(x1, x2, y):
    """ """
    global my_map
    # horizontal tunnel
    for x in range(min(x1, x2), max(x1, x2) + 1):
        my_map[x][y].blocked = False
        my_map[x][y].block_sight = False


def create_v_tunnel(y1, y2, x):
    """ """
    global my_map
    # vertical tunnel
    for y in range(min(y1, y2), max(y1, y2) + 1):
        my_map[x][y].blocked = False
        my_map[x][y].block_sight = False


def is_visible_tile(x, y):
    """ """
    global my_map

    if x >= MAP_WIDTH or x < 0:
        return False
    elif y >= MAP_HEIGHT or y < 0:
        return False
    elif my_map[x][y].blocked is True:
        return False
    elif my_map[x][y].block_sight is True:
        return False
    else:
        return True


def make_map():
    """ """
    global my_map

    # fill map with blocked (True) tiles, using comprehension list
    my_map = [[Tile(True)
               for y in range(MAP_HEIGHT)]
              for x in range(MAP_WIDTH)]

    rooms = []
    num_rooms = 0

    for r in range(MAX_ROOMS):
        # random width and height
        w = randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        # random position without going out of the boundaries of the map
        x = randint(0, MAP_WIDTH - w - 1)
        y = randint(0, MAP_HEIGHT - h - 1)

        # "Rect" class makes rectangles easier to work with
        new_room = Rect(x, y, w, h)

        # run through the other rooms and see if they intersect with
        # this one
        failed = False
        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break

        if not failed:
            # this means there are no intersections, so this room is
            # valid, "paint" it to the map's tiles
            create_room(new_room)

            # center coordinates of new room, will be useful later
            (new_x, new_y) = new_room.center()
            # optional: print "room number" to see how the map drawing
            # worked. We may have more than ten rooms, so use alphabet
            # TODO: room name should'nt block
            # room_name = GameObject(new_x, new_y, chr(65 + num_rooms),
            #                       'name', roguecolors.gold,
            #                       blocks=False)
            # draw early, so everything else is drawn on top
            # objects.insert(0, room_name)

            if num_rooms == 0:
                # this is the first room, where the player starts at
                player.x = new_x
                player.y = new_y
            else:
                # all rooms after the first:
                # connect it to the previous room with a tunnel

                # center coordinates of previous room
                (prev_x, prev_y) = rooms[num_rooms - 1].center()

                # flip a coin (random number that is either 0 or 1)
                if randint(0, 1):
                    # first move horizontally, then vertically
                    create_h_tunnel(prev_x, new_x, prev_y)
                    create_v_tunnel(prev_y, new_y, new_x)
                else:
                    # first move vertically, then horizontally
                    create_v_tunnel(prev_y, new_y, prev_x)
                    create_h_tunnel(prev_x, new_x, new_y)

            # add some contents to this room, such as monsters
            place_objects(new_room)

            # finally, append the new room to the list
            rooms.append(new_room)
            num_rooms += 1


def render_all():
    """ """
    global fov_recompute
    global visible_tiles

    if fov_recompute:
        fov_recompute = False
        visible_tiles = tdl.map.quickFOV(player.x, player.y,
                                         is_visible_tile,
                                         fov=FOV_ALGO,
                                         radius=TORCH_RADIUS,
                                         lightWalls=FOV_LIGHT_WALLS)

    # go through all tiles, and set their background color
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            visible = (x, y) in visible_tiles
            wall = my_map[x][y].block_sight
            if not visible:
                # if it's not visible right now, the player can only see
                # it if it's explored
                if my_map[x][y].explored:
                    # we're out of player's fov
                    if wall:
                        con.draw_char(x, y, None, fg=None, bg=color_dark_wall)
                    else:
                        con.draw_char(x, y, None, fg=None, bg=color_dark_ground)
            else:
                # it's visible
                if wall:
                    con.draw_char(x, y, None, fg=None, bg=color_light_wall)
                else:
                    con.draw_char(x, y, None, fg=None, bg=color_light_ground)
                # since it's visible, explore it
                my_map[x][y].explored = True

    # draw all objects in the list
    for obj in objects:
        obj.draw()

    # blit the contents of "con" to the root console and present it
    root.blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)


def player_move_or_attack(dx, dy):
    """ """
    global fov_recompute

    # the coordinates the player is moving to/attacking
    x = player.x + dx
    y = player.y + dy

    # try to find an attackable object there
    target = None
    for obj in objects:
        if obj.x == x and obj.y == y:
            target = obj
            break

    # attack if target found, move otherwise
    if target is not None:
        print('The ' + target.name + ' laughs at your puny efforts to attack him!')
    else:
        player.move(dx, dy)
        fov_recompute = True


def handle_keys():
    """ """
    global fov_recompute

    if REALTIME:
        keypress = False
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                keypress = True
        if not keypress:
            return

    else:  # turn-based
        user_input = tdl.event.key_wait()

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle fullscreen
        tdl.set_fullscreen(not tdl.get_fullscreen())

    elif user_input.key == 'ESCAPE':
        return 'exit'  # exit game

    if game_state == 'playing':
        # movement keys
        if user_input.key == 'UP':
            player_move_or_attack(0, -1)

        elif user_input.key == 'DOWN':
            player_move_or_attack(0, 1)

        elif user_input.key == 'LEFT':
            player_move_or_attack(-1, 0)

        elif user_input.key == 'RIGHT':
            player_move_or_attack(1, 0)

        else:
            return 'didnt-take-turn'


##############################
# Initialization & Main Loop #
##############################

tdl.set_font('dejavu10x10_gs_tc.png', greyscale=True, altLayout=True)
root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen=False)
tdl.setFPS(LIMIT_FPS)
con = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)

player = GameObject(0, 0, '@', 'player', roguecolors.white, blocks=True)
objects = [player]

# generate map (at this point it's not drawn to the screen)
make_map()

fov_recompute = True
game_state = 'playing'
player_action = None

while not tdl.event.is_window_closed():
    # draw all objects in the list
    render_all()

    tdl.flush()

    # erase all objects at their old locations, before they move
    for obj in objects:
        obj.clear()

    # handle keys and exit game if needed
    player_action = handle_keys()
    if player_action == 'exit':
        break

    # let monsters take their turn
    if game_state == 'playing' and player_action != 'didnt-take-turn':
        for obj in objects:
            if obj != player:
                pass
                # print('The ' + obj.name + ' growls!')
