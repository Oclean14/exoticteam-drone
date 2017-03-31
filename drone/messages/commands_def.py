#!/usr/bin/env python
# coding: utf-8

from enum import Enum, unique
@unique
class Commands(Enum):
    """ On défini les identifiants des commandes ICI. Chaque commande doit être unique """
    """ Cette commande renvoie la station la plus proche """
    NEAREST_STATION = 0x1
    """ Cette commande permet de connaitre le status du drone """
    DRONE_STATUS = 0x2
