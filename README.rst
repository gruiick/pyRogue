=======
pyRogue
=======

.. meta::
    :date: 2018-12-17
    :modified: 2023-11-22
    :status: tutorial, playable
    :version: $Id: README.rst 1.17 $
    :licence: SPDX-License-Identifier: BSD-2-Clause

This is a little *Rogue-like* game, following the `roguebasin python3 tutorial <http://rogueliketutorials.com/tutorials/tcod/v2/>`_.

There's room for lots and lots of improvements. See TODO. Opensource licence obviously, feel free to fork and PR back.

Installation:
=============

You'll need a python3 virtual env. Easiest way:

.. code::bash

.. github display on

    mkdir -p ~/python
    python3 -m venv ~/python

Copy (or git clone) pyRogue/ into this directory, then:

.. code::bash

.. github display on

    source ~/python/bin/activate
    (python) gruiick@localhost:~/python/pyRogue$ python3 main.py

Install missing python modules:

.. code::bash

.. github display on

    (python) gruiick@localhost:~/python$ python3 -m pip install -r requirements.txt

When you're done, deactivate (exit) your virtual environment, simply with:

.. code::bash

.. github display on

    deactivate

Replace:
========

Some deprecated stuffs

  * ``tcod.Console`` with ``tcod.console.Console``
  * ``tcod.event.K_`` with ``tcod.event.KeySym.``
  * ``console.tiles_rgb["bg"][x, y]`` with ``console.rgb["bg"][x, y]``
  * constants: ``tcod.CENTER`` with ``tcod.libtcodpy.CENTER`` (for example)



Rogue Game:
===========

.. WARNING::

    NOT actually playable. It shouldn't crash althought.

Playable and 'Fun'. Don't overthink: Flee, avoid, run away. Grab, use and try to survive as long as you can, on infinite levels...

It's a rogue game. You will die soon, or sooner. And you'll start all over again.

``There's nothing to find, apart from wretched death...``

.. figure:: pyrogue_screenshot.png
   :alt: pyRogue screenshot (level 1)
   :height: 641px
   :width: 976px
   :align: center


Controls:

* 'arrows' to move and attack (KeyPad and 'vi mode' also)
* 'g': grab item
* 'i': show inventory
* 'v': show logs
* 'x': show player's statistics **TODO**
* 'm': return to Main Menu **TODO**
* '<': go downstairs (one way, there is no turning back!)
* 'ESC' to quit (or 'q' at main menu)

Display:

* '@': you
* 'A': any capital letter is the name of the room **TODO**
* '!': a potion
* '~": a scroll
* 'o': an Orc
* 'T': a Troll
* '/': a sword **TODO**
* '[': a shield **TODO**
* '<': stairs, they go deeper...

Current state will be saved (savegame.sav), if you quit.

What's in chapters:
===================

Code snippets. They were used to test code, from each tutorial's chapter.

* dejavu10x10_gs_tc.png   <- font, as image
* dundalk12x12_gs_tc.png  <- another font, also as image
* menu_background1.png    <- image for the menu (from http://roguecentral.org/doryen )

