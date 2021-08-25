# Author: Max van Meijeren

# This class is the parrent class of all movement classes.
# This class is used for the stratagy design pattern.
# This class can be used on its own for testing movement logic.
class Movement:

    def __init__(self):
        import logging
        self.logger = logging.getLogger('Movement')
        self.logger.debug('Made Movement object.')
        self.logger.warning('This Movement class does not actually move anything.')

    #############################################################
    # These functions make the robot move a certain direction.
    # - The rightMotor values are inverted because the motor is
    #   turned 180 degrees compared to the leftmotor
    def moveStop(self):
        self.logger.debug('Stopped')

    def moveForward(self):
        self.logger.debug('Moving Forward')

    def moveForwardLeft(self):
        self.logger.debug('Moving Forward left')

    def moveForwardRight(self):
        self.logger.debug('Moving Forward right')

    def moveBackward(self):
        self.logger.debug('Moving Backward')

    def moveBackwardLeft(self):
        self.logger.debug('Moving Backward left')

    def moveBackwardRight(self):
        self.logger.debug('Moving Backward right')

    #Not all types of movement will be able to do this
    def moveLeft(self):
        self.logger.debug('Moving Right')

    def moveRight(self):
        self.logger.debug('Moving Left')
