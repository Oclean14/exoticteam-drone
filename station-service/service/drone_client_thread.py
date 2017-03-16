#!/usr/bin/env python
# coding: utf-8

import socket
import threading
import struct

class DroneClientThread(threading.Thread):

    ''' Cette classe représente une connection cliente. Pour chaque client, un nouveau thread est démarré '''
    def __init__(self, thisServer, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        self.thisServer = thisServer
        print("[+] New client thread created for %s:%s" % (self.ip, self.port) )

    def run(self):
        self.connected = True
        while self.connected:
            r = self.clientsocket.recv(4096)
            ''' Extraction de l'identifiant de la commande de la trame '''
            cmdId = r[0]
            ''' Execution de la commande correspondante '''
            self.thisServer.cmds[cmdId].onReceive(r, self.clientsocket)

        print("Client disconnected")
