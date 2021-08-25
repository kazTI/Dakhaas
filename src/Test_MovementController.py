# Author: Max van Meijeren

# This program will test the movement controller class.

movementToTest = 'Movement'
logfileName = 'TestsData/Movement_test.log'
sensorStatesFileName = 'TestsData/Test_MovementController.csv'


import logging
import csv

from Movement.MovementController import MovementController

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def getTestData(fileName):
    csvSensorStates = []
    csvExpectedOutcome = []
    with open(fileName) as csvFile:
        reader = csv.reader(csvFile, quoting=csv.QUOTE_NONE)
        for row in reader:
            curRow = []
            for cell in row:
                if check_int(cell) == True:
                    curRow.append(float(cell))
                else:
                    csvExpectedOutcome.append(cell)
            csvSensorStates.append(curRow)
    return csvSensorStates, csvExpectedOutcome

def initLogging(fileName):
    #deleting old log file if there is any.
    open(fileName, 'w').close()

    logging.basicConfig(filename=fileName, level=logging.DEBUG)
    return logging.getLogger('Expected outcome')

def checkLog(fileName):
    #checking if everything went correctly
    logfile = open(fileName,'r')

    lastExpectedChanged = 0
    lastMovementChanged = 0

    everythingCorrect = 1

    for line in logfile:
        if 'Expected outcome:' in line:
            lastExpectedChanged = 1
            lastExpected = line.split('Expected outcome:')[1]
        if 'DEBUG:Movement:' in line and not 'Movement:Made' in line:
            lastMovementChanged = 1
            lastMovement = line.split('Movement:')[1]
        if 'MovementController:Values:' in line:
            lastValues = line.split('MovementController:Values:')[1]
        if lastExpectedChanged and lastMovementChanged:
            lastExpectedChanged = 0
            lastMovementChanged = 0
            if not lastExpected == lastMovement:
                everythingCorrect = 0
                print('Values:', lastValues)
                print('Expected:', lastExpected)
                print('Movement:', lastMovement)

    if everythingCorrect:
        return True
    else:
        return False

logger = initLogging(logfileName)

moveContr = MovementController(movementToTest, 2, 2, [2,3,14,15])

sensorStates, expectedOutcome = getTestData(sensorStatesFileName)

for counter, states in enumerate(sensorStates):
    moveContr.setSensorStates(states[0],states[1],states[2],states[3],states[4],states[5])
    logger.debug(expectedOutcome[counter])
    moveContr.move()

#stopping the logging and closing the logger file
logging.shutdown()

if checkLog(logfileName):
    print('Test ended without any issues')
