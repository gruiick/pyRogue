=======
pyRogue
=======

.. meta::
    :date: 2018-12-17
    :modified: 2021-11-12

:status: tutorial, playable
:version: $Id: README.rst 1.14 $
:licence: SPDX-License-Identifier: BSD-2-Clause

This is a little *Rogue-like* game, following the old `roguebasin.com <http://www.roguebasin.com/index.php?title=Roguelike_Tutorial,_using_python3%2Btdl>`_ python3 + tdl tutorial.

Warning: 'old-tdl/' parts won't work anymore, as ``tdl module is now deprecated.``, need ``libffi-dev``, ``libsdl2-dev`` installed. 

There's room for lots and lots of improvements. See TODO. Opensource licence obviously.

Rogue Game:
===========

Was playable and 'Fun'. Don't overthink: Flee, avoid, run away. Grab, use and try to survive as long as you can, on infinite levels...

It's a rogue game. You will die soon, or sooner. And you'll start all over again.

``There's nothing to find, apart from wretched death...``

.. figure:: pyrogue_screenshot.png
   :alt: pyRogue screenshot (level 1)
   :height: 641px
   :width: 976px
   :align: center


Controls:

* 'arrows' to move and attack (no diagonals)
* 'g': grab thing
* 'i': show inventory
* 'x': show player's statistics
* '<': go downstairs (one way, there is no turning back!)
* 'ESC' to quit (or 'c' at main menu)

Display:

* '@': you
* 'A': any capital letter is the name of the room
* '+': a potion
* '#": a scroll
* 'o': an Orc
* 'T': a Troll
* '/': a sword
* '[': a shield
* '<': stairs, they go deeper...

Current state will be saved (savegame.db), if you quit.

What's in chapters:
===================

Code snippets. They were used to test code, from each tutorial's chapter.

* dejavu10x10_gs_tc.png   <- font, as image
* dundalk12x12_gs_tc.png  <- another font, also as image
* menu_background1.png    <- image for the menu (from http://roguecentral.org/doryen )

