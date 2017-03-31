#!/usr/bin/env python
# coding: utf-8

from enum import Enum, unique
@unique
class Commands(Enum):
    """ On défini les identifiants des commandes ICI. Chaque commande doit être unique """
    NEAREST_STATION = 0x1
    DRONE_STATUS = 0x2