# Author: Max van Meijeren

# This program will start the robot.

#=================================================
from Controller import Controller

#=================Functions=================

# Initialize the controller with a json configuration file
controller = Controller('config.json')

# check if this file is imported or called directly by python.
# if it isn't imported start the controller loop
if __name__ == "__main__":
    controller.loop()
