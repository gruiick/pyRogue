#!/usr/bin/env python3

from enum import auto, Enum


class RenderOrder(Enum):
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()
