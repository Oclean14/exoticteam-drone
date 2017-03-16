from threading import Thread
from time import sleep
import socket

'''
    Fonction appelée par le thread de reception
'''
def receive(arg):
    print("Waiting for bytes...")
    bytes = arg.clientsock.recv(4096)
    if bytes:
        print("%s received" % (bytes))

class DroneClient:
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
