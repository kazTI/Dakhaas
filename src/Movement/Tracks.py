# Author: Max van Meijeren

# This class is inherited from the Movement class and
# will make the movement with tracks possible.

from Movement.Movement import Movement

class Tracks(Movement):

    import RPi.GPIO as io
    from time import sleep

    def __init__(self, hBridgePins):
        import logging
        self.logger = logging.getLogger('Movement')
        self.logger.debug('Made Tracks object.')

        self.io.setwarnings(True)
        self.io.setmode(self.io.BCM)

        self.setPins(hBridgePins)
        self.io.setup(13, self.io.OUT)

    # This funtion stores the pin numbers and sets the pins to output
    # hBridgePins[0] and [1] are for the left motor
    # hBridgePins[2] and [3] are for the right motor
    def setPins(self, hBridgePins):
        self.logger.debug('H-Brige pins: %d, %d, %d, %d', hBridgePins[0], hBridgePins[1], hBridgePins[2], hBridgePins[3])
        self.hBridgePins = hBridgePins
        for i in range(0,4):
            self.io.setup(hBridgePins[i], self.io.OUT)

    # This function controls the motors.
    # leftMotor and rightMotor expect these values:
    # -1 Turns the motor backwards
    # 0  Stops the motors
    # 1  Turns the motor forward
    def moveTracks(self, leftMotor, rightMotor):
        #making the left motor turn
        if leftMotor == -1:
            self.io.output(self.hBridgePins[1], 0)
            self.sleep(0.01)
            self.io.output(self.hBridgePins[0], 1)
        elif leftMotor == 0:
            self.io.output(self.hBridgePins[0], 0)
            self.io.output(self.hBridgePins[1], 0)
        elif leftMotor == 1:
            self.io.output(self.hBridgePins[0], 0)
            self.sleep(0.01)
            self.io.output(self.hBridgePins[1], 1)

        if rightMotor == -1:
            self.io.output(self.hBridgePins[3], 0)
            self.sleep(0.01)
            self.io.output(self.hBridgePins[2], 1)
        elif rightMotor == 0:
            self.io.output(self.hBridgePins[2], 0)
            self.io.output(self.hBridgePins[3], 0)
        elif rightMotor == 1:
            self.io.output(self.hBridgePins[2], 0)
            self.sleep(0.01)
            self.io.output(self.hBridgePins[3], 1)

    #############################################################
    # These functions make the robot move a certain direction.
    # - The rightMotor values are inverted because the motor is
    #   turned 180 degrees compared to the leftmotor
    def moveStop(self):
        super().moveStop()
        self.moveTracks(0, 0)

    def moveForward(self):
        super().moveForward()
        self.moveTracks(1, -1)

    def moveForwardLeft(self):
        super().moveForwardLeft()
        self.moveTracks(0, -1)

    def moveForwardRight(self):
        super().moveForwardRight()
        self.moveTracks(1, 0)

    def moveBackward(self):
        super().moveBackward()
        self.moveTracks(-1, 1)

    def moveBackwardLeft(self):
        super().moveBackwardLeft()
        self.moveTracks(0, 1)

    def moveBackwardRight(self):
        super().moveBackwardRight()
        self.moveTracks(-1, 0)

    def moveLeft(self):
        super().moveLeft()
        self.moveTracks(-1, -1)

    def moveRight(self):
        super().moveRight()
        self.moveTracks(1, 1)
