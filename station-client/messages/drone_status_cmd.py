#!/usr/bin/env python
# coding: utf-8

import struct
from messages.commands_def import Commands

class DroneStatusCmd:
    """ Commande permettant d'envoyer le status du drone position et le niveau de batterie """
    def __init__(self, sender):
        """ La classe représentant l'envoyeur du message (permet d'accéder à la socket en écriture) """
        self.sender = sender
    def send(self,droneId, batteryLevel,lat, lon):
        print("SEND: Drone id ", droneId, " send request from position (", lat,",",lon ,") battery level: ", batteryLevel)
        """
            Format de la trame:
            B : entier représentant l'identifiant du message (non signé sur 1 octet)
            H(1) : Entier non signé représentant l'identifiant du drone (sur 2 octet)
            H(2) : Entier non signé représentant le niveau de batterie du drone (sur 2 octet)
            f(1) : Position -> latitude (decimal)
            f(2) : Position -> longitude (decimal)
        """
        packed = struct.pack('BHHff',  Commands.DRONE_STATUS.value, droneId, batteryLevel, lat, lon)
        """ Envoi de la trame """
        self.sender.clientsock.send(packed)
