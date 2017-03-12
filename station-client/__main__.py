import sys
from drone_client import DroneClient
from messages.commands_def import Commands
from messages.drone_status_cmd import DroneStatusCmd
import time
import random
from random import randint

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    client = DroneClient()

    """Run the server"""
    client.connect("127.0.0.1", 8000)
    client.addCmd(Commands.DRONE_STATUS, DroneStatusCmd(client))
    droneStatusCmd = client.getCmd(Commands.DRONE_STATUS)

    while True:
        lat = random.uniform(40.0, 45.0)
        lon = random.uniform(40.0, 45.0)
        droneId = randint(0, 20)
        batteryLevel = randint(0, 100)
        droneStatusCmd.send(droneId,batteryLevel,lat,lon)
        time.sleep(1)

if __name__ == "__main__":
    main()