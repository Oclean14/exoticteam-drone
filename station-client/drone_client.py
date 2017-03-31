from threading import Thread
from time import sleep
import socket
import time
import random
from random import randint
from math import *

'''
    Fonction appelée par le thread de reception
'''


def receive(arg):
    print("Waiting for bytes...")
    bytes = arg.clientsock.recv(4096)
    if bytes:
        print("%s received" % (bytes))


class DroneClient:
    """
    on créé la map 3D dans laquelle les drones évoluent
    Le sol représenté ci dessous
    A
    |
    Width(y)
    |
    |_____Length(x)_____>
    Length > Width pour la construction de la map et l'altitude est en z
    """
    mapWidth = randint(100, 200)
    mapLength = randint(100, 200)
    mapAlt = randint(100, 200)
    airSpaceMin = 90
    airSpaceMax = mapAlt

    speed = 50
    batteryLevel = 100
    executing = False
    flying = False
    coords = [randint(0, mapLength), randint(0, mapLength), randint(0, mapAlt)]
    if mapWidth > mapLength:
        a = mapLength
        mapLength = mapWidth
        mapWidth = a

    '''
        La classe client permettant de communiquer avec le serveur. Ce programme python doit être lancé sur le drone.
    '''

    def __init__(self):

        self.clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cmds = dict({})

    '''
        Cette methode permet de se connecter au serveur recevant les commandes des drones
    '''

    def connect(self, host, port):
        self.clientsock.connect((host, port))
        receiveThread = Thread(target=receive, args=(self,))
        receiveThread.start();

    '''
        Ajout d'une nouvelle commande qui doit être aussi ajouté sur le serveur
    '''

    def addCmd(self, cmdId, cmd):
        self.cmds[cmdId] = cmd

    '''
        Permet de récupérer la commande spécifiée par le cmdId
    '''

    def getCmd(self, cmdId):
        return self.cmds[cmdId]

    def getLocation(self):
        return self.coords

    def moveTo(self, coords):

        while self.coords[3] < self.airSpaceMin + randint(0, self.airSpaceMax - self.airSpaceMin):
            self.coords[3] += 1
            print("INFO : Going up to the airSpace")
            time.sleep(1)
            self.batteryLevel -= 1

            a = coords[1] - self.coords[1]
            b = coords[2] - self.coords[2]
            norme = sqrt(a * a + b * b)
        print("INFO : I'm in the legal airspace")
        while not (self.isOnTopOf(coords)):
            print("INFO : Moving to the destination")

            self.coords[1] = self.coords[1] + (coords[1] - self.coords[1]) / norme
            self.coords[2] = self.coords[2] + (coords[2] - self.coords[2]) / norme
            time.sleep(1)
        print("INFO : I'm on top of the destination")

        while self.coords[3] > 0:
            print("INFO : I'm landing on the destination")
            self.coords[3] -= 1
            time.sleep(1)
        print("INFO : It is done.")

    def isOnTopOf(self, coords):
        if self.coords[1] == coords[1] and self.coords[2] == coords[2]:
            return True
        else:
            return False

    def executeDelivery(self, stockCoords, destinationCoords):
        self.executing = True
        print("INFO : Starting Delivery")
        print("INFO : Going to the stock")
        self.moveTo(stockCoords)
        print("INFO : Going to the destination")
        self.moveTo(destinationCoords)
        print("INFO : Delivery done ! Ready for an other mission")
        self.executing = False
