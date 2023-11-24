# TODO list

$Id: TODO.md 8 $

## Escape from the tutorial

One of the main goals of the tutorial is 'all-in-one' file. This reduce
possibilities of evolutions.

* remove tdl, as it's deprecated, and switch to pure libtcod: **IN PROGRESS**
  https://github.com/libtcod/python-tcod
  follow http://rogueliketutorials.com/tutorials/tcod/v2/

Then, maybe:

* improve player's displacements (diags) **DONE**

* move all CONSTANTS to a separate file (or yml config file?)

* improve use of colors (roguecolors was good following the tutorial, but now, move to something simpler)
    * themes? greyscale, high contrast for color impaired, dark, light?

* 'h' for help?

* mouse menus? (Tk, pySimpleGUI)

* New items:
    * Potion of Vision (1/100): reveal all tiles/items/monsters of a map
    * Mimic (monster, 1/100): mimic something (item), weak attack (2), weak life (2)

