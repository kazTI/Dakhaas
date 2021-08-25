# Author: Max van Meijeren

class Disposal:

    def __init__(self):
        import logging
        self.logger = logging.getLogger('Disposal')
        self.logger.debug('Made Disposal object.')
        self.logger.warning('This Disposal class does not actually dispose of anything.')

    def dumpTrash(self):
        self.logger.debug('Dumping Trash')
