#!/usr/bin/env python
# coding: utf-8

import struct

class NearestStationCmd:
    """ Commande retournant les coordonnées de Les/la station la plus proche """
    def __init__(self, sender):
        self.sender = sender

    def onReceive(self, recvstr, sendersocket):
        """
            Format de la trame:
            B : entier représentant l'identifiant du message (non signé sur 1 octet)
            H(1) : Entier non signé représentant l'identifiant du drone (sur 2 octet)
            f(1) : Position -> latitude (decimal)
            f(2) : Position -> longitude (decimal)
        """
        unpacker = struct.Struct('BHff')
        unpacked = unpacker.unpack(recvstr)
        self.droneId = unpacked[1]
        """ (lat , lon ) """
        self.dronePosition = (unpacked[2], unpacked[3])
        print("RECEIVED: Drone id ", self.droneId, " send his position ", self.dronePosition)
