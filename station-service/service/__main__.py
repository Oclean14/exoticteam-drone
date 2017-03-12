import sys
from drone_server import DroneServer
from messages.commands_def import Commands
from messages.nearest_station_cmd import NearestStationCmd
from messages.drone_status_cmd import DroneStatusCmd

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    server = DroneServer("127.0.0.1", 8000)

    """ Add commands here """
    """NEAREST STATION COMMAND"""
    server.addCmd(Commands.NEAREST_STATION.value, NearestStationCmd(server))
    server.addCmd(Commands.DRONE_STATUS.value, DroneStatusCmd(server))

    """Run the server"""
    server.run()

if __name__ == "__main__":
    main()