# Author: Max van Meijeren

# This class will initialize all the components of the dakhaas and contains the
# main loop of the robot.

#=================================================

class Controller:

    def __init__(self, configFileName):
        from Initilizer import Initilizer
        #Getting configuration data from a file
        configData = self.getConfigurationSettings(configFileName)
        #Initializing all components
        initilizer = Initilizer()
        self.logger, self.camera, self.moveContr, self.fsr, self.hx, self.shovel, self.disposal, self.piezoFrontVar, self.piezoBackVar = initilizer.initParts(configData)
        self.sleepTime = 30

    # This function gets the configurationData from a json file and puts it in a dictonary variable
    def getConfigurationSettings(self, fileName):
        import json
        with open(fileName) as json_data_file:
            configurationData = json.load(json_data_file)
        return configurationData

    # Shutdown the robot
    # To run this command the program needs elevated privileges
    def shutdownPC(self):
        import os
        os.system('poweroff')

    # Makes the program wait for a specified amout of time
    def wait(self, seconds = None):
        if seconds is None:
            seconds = self.sleepTime
        import time
        self.logger.debug('Waiting ' + str(seconds) + ' seconds')
        time.sleep(seconds)

    # This function is the main loop of the robot.
    def loop(self):
        self.wait()
        self.logger.debug('Starting main loop')
        currentMovement = 0
        while currentMovement != -3:
            self.logger.debug('Getting sensor values')
            hxVar = self.hx.read()
            piezoFrontVar = self.read()
            piezoBackVar = self.read()
            fsrVar = self.fsr.read()

            self.logger.debug('Setting sensor values for movementController')

            self.moveContr.setSensorStates(shovelMoveState = fsrVar, backBumperState = piezoBackVar, frontBumperState = piezoFrontVar)

            self.logger.debug('Getting the current movement direction of the dakhaas')
            currentMovement = self.moveContr.move()
            self.logger.debug('Current movement direction: %d', currentMovement)

            if currentMovement == 0:
                #self.shovel.method()
                pass
            elif currentMovement == 1:
                self.disposal.dumpTrash()
