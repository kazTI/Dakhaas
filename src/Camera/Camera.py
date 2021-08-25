# Author: Max van Meijeren
#     Ramon Rooijens

class Camera:

    def __init__(self):
        import logging
        self.logger = logging.getLogger('Camera')
        self.logger.debug('Made Camera object.')
        self.logger.warning('This Camera class does not actually sense anything.')

    def checkCamera(self):
        self.logger.debug('Call checkCamera')
