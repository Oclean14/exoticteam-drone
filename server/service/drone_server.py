#!/usr/bin/env python
# coding: utf-8

import socket
from drone_client_thread import DroneClientThread

class DroneServer:
    """ Classe définissant le daemon recevant les requêtes des drones"""
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serversocket.bind((self.ip, self.port))
        self.cmds = dict({})

    ''' Méthode de démarrage du serveur '''
    def run(self):
        self.running = True
        self.serversocket.listen(10)
        print("Running on port ", self.port, " with address ", self.ip)

        """ Boucle infinie de réception des commandes """
        while self.running:
            ''' Bloquant !! Attente d'une connexion cliente '''
            (clientsocket, (ip, port)) = self.serversocket.accept()
            clientthread = DroneClientThread(self, ip, port, clientsocket)
            """ Démarrage du thread client pour recevoir les commandes """
            clientthread.start()

    def addCmd(self, cmdId, cmd):
        self.cmds[cmdId] = cmd
