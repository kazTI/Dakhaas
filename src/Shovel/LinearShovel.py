#Author Galvin Bartes


# This class works with data from FSR.
# When threshold doesn't stand continue the operation

# Actuator tested and works with 12 V
# Circuit not tested on raspberry
# Actuator tested with Arduino fails:
# Error response: could not find COM port (Arduino)


# code reference online:
# https://www.bluetin.io/python/gpio-pwm-raspberry-pi-h-bridge-dc-motor-control/
# https://maker.pro/raspberry-pi/tutorial/how-to-control-a-dc-motor-with-an-l298-controller-and-raspberry-pi
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
# https://pythonprogramming.net/gpio-motor-control-raspberry-pi/
# https://geextor.com/2016/11/20/driving-a-dc-motor-with-raspberry-pi/
# https://iot-guider.com/raspberrypi/h-bridge-motor-driver-in-raspberry-pi/
# https://www.raspberrypi.org/forums/viewtopic.php?t=69330
# https://www.robotshop.com/community/forum/t/retracting-linear-actuator-with-raspberry-pi/43024
# https://raspberrypi.stackexchange.com/questions/64284/circuit-to-move-a-12v-actuator-both-ways
# https://raspberrypi.stackexchange.com/questions/82286/controlling-linear-actuator
# http://blog.enthought.com/general/raspberry-pi-sensor-and-actuator-control/#.Xh25M8hKiUl
# 

from Shovel.Shovel import Shovel

class LinearShovel(Shovel):
    import sys
	import time
	import RPi.GPIO as GPIO


    def __init__(self, hBridgePins):
        import logging
        self.logger = logging.getLogger('LineairShovel')
        self.logger.debug('Create LineairShovel object.')
                self.io.setwarnings(True)
                self.io.setmode(self.io.BCM)
        	    self.setPins(hBridgePins)

        def setPins(self, hBridgePins):
    		self.logger.debug('H-Bridge pins: %d, %d, %d', hBridgePins[4], hBridgePins[5], hBridgePins[6])
    		self.hBridgePins = hBridgePins
    		for i in range(4,7):
    			self.io.setup(hBridgePins[i], self.io.OUT)

    
    
        def pushForward(self):
            self.logger.debug('Moving Forward')
            
        def pullBack(self):
            self.logger.debug('Moving Backwards')
            
        def holdAndPause(self):
            self.logger.debug('Pause in current position')
            
        def calcThresholdFromFSR():
            self.logger.debug('Pause in current position')
            
