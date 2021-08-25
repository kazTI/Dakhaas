# Author: Max van Meijeren

class Sensor:

    def __init__(self):
        import logging
        self.logger = logging.getLogger('Sensor')
        self.logger.debug('Made Sensor object.')
        self.logger.warning('This Sensor class does not actually sense anything.')

    def read(self):
        self.logger.debug('Reading Sensor value')
