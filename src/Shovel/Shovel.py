# Author: Max van Meijeren

class Shovel:

    def __init__(self):
        import logging
        self.logger = logging.getLogger('Shovel')
        self.logger.debug('Made Shovel object.')
        self.logger.warning('This Shovel class does not actually shovel anything.')
