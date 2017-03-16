#!/usr/bin/env python
# coding: utf-8

import struct

class NearestStationCmd:
    """ Commande retournant les coordonnées de Les/la station la plus proche """
    def __init__(self, sender):
        """ La classe représentant l'envoyeur de la commande (permet d'accéder au socket en écriture) """
        self.sender = sender

    def onReceive(self, recvstr, sendersocket):
        unpacker = struct.Struct('BHff')
        unpacked = unpacker.unpack(recvstr)
        self.droneId = unpacked[1]
        """ Position (lat , lon ) """
        self.dronePosition = (unpacked[2], unpacked[3])
        print("RECEIVED: Drone id ", self.droneId, " send request from position ", self.dronePosition," get nearest station" )
