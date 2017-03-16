#!/usr/bin/env python
# coding: utf-8

import struct

class DroneStatusCmd:
    """  """
    def __init__(self, sender):
        self.sender = sender

    def onReceive(self, recvstr, sendersocket):
        """
            Format de la trame:
            B : entier représentant l'identifiant du message (non signé sur 1 octet)
            H(1) : Entier non signé représentant l'identifiant du drone (sur 2 octet)
            H(2) : Entier non signé représentant le niveau de batterie du drone (sur 2 octet)
            f(1) : Position -> latitude (decimal)
            f(2) : Position -> longitude (decimal)
        """
        unpacker = struct.Struct('BHHff')
        unpacked = unpacker.unpack(recvstr)
        self.droneId = unpacked[1]
        self.batteryLevel = unpacked[2]
        """ ( latitude , longitude ) """
        self.dronePosition = (unpacked[3], unpacked[4])
        print("RECEIVED: Drone id ", self.droneId, " is at position ", self.dronePosition," with a battery level of ", self.batteryLevel)
