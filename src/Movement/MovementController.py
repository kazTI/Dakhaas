# Author: Max van Meijeren

# This class decides where the robot needs to go and makes use of the Movement
# class.

class MovementController:

    def __init__(self, movementUsed, maxAvgDistBetweenSides, maxStandStillTimes = 2, pinsUsed = -1):
        import logging
        self.logger = logging.getLogger('MovementController')
        self.logger.debug('Made MovementController object.')
        self.selectMovement(movementUsed, pinsUsed)
        self.maxAvgDistBetweenSides = maxAvgDistBetweenSides
        self.standStillCounter = 0
        self.maxStandStillTimes = maxStandStillTimes

    # This function decides what type of movement will be used and
    # will give it the gpio pins it needs.
    # The options are:
    # Movement, Tracks
    def selectMovement(self, movementUsed, pinsUsed = -1):
        self.logger.debug('Selecting Movement used...')
        if movementUsed == 'Movement':
            from Movement.Movement import Movement
            self.movement = Movement()
        elif movementUsed == 'Tracks':
            from Movement.Tracks import Tracks
            self.movement = Tracks(pinsUsed)

    # This function gets the states of the sensors.
    def setSensorStates(self, binState = False, shovelMoveState = False, backBumperState = False, frontBumperState = False, leftDistance = 0, rightDistance = 0):
        self.logger.debug('Getting updated sensor states: ')
        self.logger.debug('Values: bS:%d, sMS:%d, bBS:%d, fBS:%d, lD:%d, rD:%d', binState, shovelMoveState, backBumperState, frontBumperState, leftDistance, rightDistance)
        self.binState = binState
        self.shovelMoveState = shovelMoveState
        self.backBumperState = backBumperState
        self.frontBumperState = frontBumperState
        self.leftDistance = leftDistance
        self.rightDistance = rightDistance

    # This funtion decides where the robot needs to move towards.
    # Returns Values
    # -3                when standing still at the beginning after it
    #                   couldn't go further anymore or got stuck
    # -2                when going backwards because it got stuck
    # -1                when going backwards
    # 0                 when standing still
    # 1                 when standing still at the beginning
    # 2                 when going forwards
    def move(self):
        if self.standStillCounter == -1:
            if self.goToBigBin():
                return -3
            else:
                return -2
        elif self.binState:
            if self.goToBigBin():
                return 1
            else:
                return -1
        elif self.frontBumperState:
            self.standStillCounter +=1
            if self.standStillCounter < self.maxStandStillTimes:
                self.movement.moveStop()
                return 0
            else:
                self.logger.info('Can\'t move forward going back to beginning possition')
                self.standStillCounter = -1
                if self.goToBigBin():
                    return -3
                else:
                    return -2
        elif self.shovelMoveState:
            self.logger.info('Shovel can\'t move debris going back to beginning possition')
            self.standStillCounter = -1
            if self.goToBigBin():
                return -3
            else:
                return -2
        else:
            self.moveFB(1)
            return 2

    # Move the robot back to the back of the gutter.
    def goToBigBin(self):
        if self.backBumperState:
            self.movement.moveStop()
            return True
        else:
            self.moveFB(0)
            return False

    # This function makes the robot move forwards or backwards with an equal
    # amount of space between the sides of the robot and the walls
    # direction = 0     The robot moves backwards
    # direction = 1     The robot moves forwards
    def moveFB(self, direction):
        if direction:
            self.logger.debug('Moving forwards')
        else:
            self.logger.debug('Moving backwards')

        # Gets the left over size differrence between the sides
        distBetweenSides = self.leftDistance - self.rightDistance

        # If there is a bigger leeway than defined
        if distBetweenSides > self.maxAvgDistBetweenSides or distBetweenSides < (-1 * self.maxAvgDistBetweenSides):
            if distBetweenSides < 0:
                if direction:
                    self.movement.moveForwardRight()
                else:
                    self.movement.moveBackwardRight()
            else:
                if direction:
                    self.movement.moveForwardLeft()
                else:
                    self.movement.moveBackwardLeft()
        else:
            if direction:
                self.movement.moveForward()
            else:
                self.movement.moveBackward()
