#Author: Max van Meijeren
#    Ramon Rooijens

from Sensor.Sensor import Sensor

class FSR(Sensor):

    import RPi.GPIO as io

    def __init__(self, GPIOpin):
        import logging
        self.logger = logging.getLogger('FSR')
        self.logger.debug('Made FSR object.')
        self.io.setmode(self.io.BCM)
        self.io.setup(GPIOpin, self.io.IN)
        self.GPIOpin = GPIOpin

    def read(self):
        super().read()
        if(self.io.input(self.GPIOpin)): #If FS threshhold is met
            return True
        else:
            return False
