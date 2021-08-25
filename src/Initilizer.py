# Author: Max van Meijeren

# This class will initialize all parts needed by Controller.py

class Initilizer:

    def __init__(self):
        pass

    def initCamera(self, configDataCamera):
        from Camera.PyCamera import PyCamera
        from Camera.Camera import Camera
        self.logger.debug('Initializing Camera')
        #self.logger.critical('No Camera to initialize')
        camera = PyCamera(configDataCamera['framesPerSecond'], configDataCamera['timeLimitInSeconds'])
        #camera = Camera()
        return camera

    def initMovement(self, configDataMove, configDataGPIOMove):
        from Movement.MovementController import MovementController
        self.logger.debug('Initializing MovementContoller')
        moveContr = MovementController(configDataMove['movementUsed'],
                                       configDataMove['maxAvgDistBetweenSides'],
                                       configDataMove['maxStandStillTimes'],
                                       configDataGPIOMove['hBridgePins'])
        return moveContr

    def initSensors(self, configDataSensors, configDataGPIOSensor):
        #from Sensor.LoadCell import LoadCell
        from Sensor.FSR import FSR
        #from Sensor.Piezo import Piezo
        from Sensor.Sensor import Sensor
        self.logger.debug('Initializing Sensors')
        # configDataGPIOSensor['hx711Pins'] contains two pins the first being
        # the data pin the second being the clock pin
        # loadCell = LoadCell(configDataGPIOSensor['hx711Pins'],
        #                     configDataSensors['hx711']['referenceUnit'],
        #                     configDataSensors['hx711']['threshold'])
        fsr = FSR(configDataGPIOSensor['fsrPin'])
        # piezoFrontVar = Piezo(configDataGPIOSensor['piezo1'], configDataSensors['piezo1']['threshold'])
        # piezoBackVar = Piezo(configDataGPIOSensor['piezo2'], configDataSensors['piezo2']['threshold'])
        loadCell = Sensor()
        # fsr = Sensor()
        piezoFrontVar = Sensor()
        piezoBackVar = Sensor()
        return fsr, loadCell, piezoFrontVar, piezoBackVar

    def initShovel(self, configDataShovel, configDataGPIOShovel):
        #from Shovel.LinearShovel import LinearShovel
        from Shovel.Shovel import Shovel
        self.logger.debug('Initializing Shovel')
        self.logger.critical('No Shovel to initialize')
        shovel = Shovel()
        return shovel

    def initDisposal(self, configDataDisposal, configDataGPIODisposal):
        from Disposal.LinearDisposal import LinearDisposal
        self.logger.debug('Initializing Disposal')
        # configDataGPIODisposal['hBridgePins'] contains three pins the first being
        # the first being the pwm pin
        disposal = LinearDisposal(configDataDisposal['sleeptime'], configDataGPIODisposal['hBridgePins'])
        return disposal

    def initLogging(self, configDataLog):
        import logging
        self.selectLoggingLevel(configDataLog['fileName'], configDataLog['level'], configDataLog['format'])
        logger = logging.getLogger('Initilizer')
        mainLogger = logging.getLogger('__main__')
        logger.info('Starting Dakhaas Version ...')
        return logger, mainLogger

    # This function sets the log name, minimum logging level and the logging format.
    def selectLoggingLevel(self, fileName='log.log', loggingLevel='WARNING', format='%(levelname)s:%(module)s:%(message)s'):
        import logging
        if loggingLevel == 'DEBUG':
            logging.basicConfig(filename=fileName, level=logging.DEBUG, format=format)
        elif loggingLevel == 'INFO':
            logging.basicConfig(filename=fileName, level=logging.INFO, format=format)
        elif loggingLevel == 'WARNING':
            logging.basicConfig(filename=fileName, level=logging.WARNING, format=format)
        elif loggingLevel == 'ERROR':
            logging.basicConfig(filename=fileName, level=logging.ERROR, format=format)
        elif loggingLevel == 'CRITICAL':
            logging.basicConfig(filename=fileName, level=logging.CRITICAL, format=format)

    def initParts(self, configData):
        self.logger, mainLogger = self.initLogging(configData['logging'])
        camera = self.initCamera(configData['camera'])
        moveContr = self.initMovement(configData['movement'], configData['gpioPins']['movement'])
        fsr, hx, piezoFrontVar, piezoBackVar = self.initSensors(configData['sensors'], configData['gpioPins']['sensors'])
        shovel = self.initShovel(configData['shovel'], configData['gpioPins']['shovel'])
        disposal = self.initDisposal(configData['disposal'], configData['gpioPins']['disposal'])
        return mainLogger, camera, moveContr, fsr, hx, shovel, disposal, piezoFrontVar, piezoBackVar
