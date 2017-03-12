#!/usr/bin/env python
# coding: utf-8

import struct

class NearestStationCmd:
    """ Commande retournant les coordonnées de Les/la station la plus proche """
    def __init__(self, sender):
        """ This class represent a command call from the client to get the nearest station """
        self.sender = sender
    def onReceive(self, recvstr, sendersocket):
        unpacker = struct.Struct('BHHff')
        unpacked = unpacker.unpack(recvstr)
        self.droneId = unpacked[1]
        self.droneBatteryLevel = unpacked[2]
        """ (lat , lon ) """
        self.dronePosition = (unpacked[3], unpacked[4])
        print("RECEIVED: Drone id ", self.droneId, " send his position ", self.dronePosition," battery level", self.droneBatteryLevel )

