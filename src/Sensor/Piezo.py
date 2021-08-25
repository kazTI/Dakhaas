#Author: Max van Meijeren
#    Ramon Rooijens

from Sensor.Sensor import Sensor

class Piezo(Sensor):

    import RPi.GPIO as io

    def __init__(self, GPIOpin, threshold):
        import logging
        self.logger = logging.getLogger('Piezo')
        self.logger.debug('Made Piezo object.')
        self.io.setmode(self.io.BCM)
        self.io.setup(GPIOpin, self.io.IN)
        self.GPIOpin = GPIOpin

    def read(self):
        super().read()
        if(self.io.input(self.GPIOpin)): #If FS threshhold is met
            return True
        else:
            return False
