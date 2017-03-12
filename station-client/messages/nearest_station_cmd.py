#!/usr/bin/env python
# coding: utf-8

import struct

class NearestStationCmd:
    """ Commande retournant les coordonnées de Les/la station la plus proche """
    def __init__(self):
        """ This class represent a command call from the client to get the nearest station """
    def onReceive(self, recvstr, sendersocket):
        unpacker = struct.Struct('BHff')
        unpacked = unpacker.unpack(recvstr)
        self.droneId = unpacked[1]
        """ (lat , lon ) """
        self.dronePosition = (unpacked[2], unpacked[3])
        print("RECEIVED: Drone id ", self.droneId, " send request from position ", self.dronePosition," get nearest station" )

