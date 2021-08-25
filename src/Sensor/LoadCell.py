# Author: Max van Meijeren

# This class will read the values form the Load Cell Amp from adafruit connected to a L711

from Sensor.Sensor import Sensor

class LoadCell(Sensor):

    import RPi.GPIO as io
    from Sensor.HX711 import HX711

    def __init__(self, loadCellPins, referenceUnit, threshold):
        import logging
        self.logger = logging.getLogger('LoadCell')
        self.logger.debug('Made LoadCell object.')
        self.threshold = threshold
        self.initHX711(loadCellPins, referenceUnit)

    def initHX711(self, loadCellPins, referenceUnit):
        self.logger.debug('Initializing loadCell')
        self.loadCell = self.HX711(loadCellPins[0], loadCellPins[1])    # Data pin, Clock pin
        self.loadCell.set_reading_format("MSB", "MSB")                  # MSB or LSB
        self.loadCell.set_reference_unit(referenceUnit)
        self.loadCell.reset()
        self.loadCell.tare()
        self.logger.debug('Done initializing loadCell')

    def readValue(self):
        val = 0
        try:
            val = self.loadCell.get_weight(5)

            #without this values became unreliable
            self.loadCell.power_down()
            self.loadCell.power_up()
        except Exception:
            pass
        return val

    def read(self):
        super().read()
        if self.readValue() > self.threshold:
            return True
        else:
            return False
