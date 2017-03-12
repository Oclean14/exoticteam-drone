#!/usr/bin/env python
# coding: utf-8

import struct
from messages.commands_def import Commands

class DroneStatusCmd:
    """ Commande retournant les coordonnées de Les/la station la plus proche """
    def __init__(self, sender):
        """ This class represent a command call from the client to get the nearest station """
        self.sender = sender
    def send(self,droneId, batteryLevel,lat, lon):
        print("SEND: Drone id ", droneId, " send request from position (", lat,",",lon ,") battery level: ", batteryLevel)
        packed = struct.pack('BHHff',  Commands.DRONE_STATUS.value, droneId, batteryLevel, lat, lon)
        self.sender.clientsock.send(packed)
