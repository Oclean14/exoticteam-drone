from threading import Thread
from time import sleep
import socket


def receive(arg):
    print("Waiting for bytes...")
    bytes = arg.clientsock.recv(4096)
    if bytes:
        print("%s received" % (bytes))

class DroneClient:
    '''
        La classe client permettant de communiquer avec le serveur. Ce programme python doit être lancé sur le drone
    '''
    def __init__(self):
            self.clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.cmds = dict({})

    def connect(self, host, port):
        self.clientsock.connect((host, port))
        receiveThread = Thread(target=receive, args=(self,))
        receiveThread.start();

    def addCmd(self, cmdId, cmd):
        self.cmds[cmdId] = cmd
    def getCmd(self, cmdId):
        return self.cmds[cmdId]