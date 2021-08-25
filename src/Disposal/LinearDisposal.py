#Author Kazimir Piek

from Disposal.Disposal import Disposal

class LinearDisposal(Disposal):

    import sys
    import time
    import RPi.GPIO as io
    

    def __init__(self, sleeptime, hBridgePins):
        import logging
        self.logger = logging.getLogger('LinearDisposal')
        self.logger.debug('Made LinearDisposal object.')

        self.io.setwarnings(True)
        self.io.setmode(self.io.BCM)
        self.sleeptime = sleeptime
        self.setPins(hBridgePins)

    def setPins(self, hBridgePins):
        self.logger.debug('H-Bridge pins: %d, %d, %d', hBridgePins[0], hBridgePins[1], hBridgePins[2])
        self.hBridgePins = hBridgePins
        for i in range(0,3):
            self.io.setup(hBridgePins[i], self.io.OUT)

    def dumpTrash(self):
        pi_pwm = self.io.PWM(self.hBridgePins[0], 150)
        pi_pwm.start(100)
        self.io.output(self.hBridgePins[1], 0)
        self.time.sleep(0.01)
        self.io.output(self.hBridgePins[2], 1)
        self.time.sleep(self.sleeptime)
        self.io.output(self.hBridgePins[1], 1)
        self.time.sleep(0.01)
        self.io.output(self.hBridgePins[2], 0)
        self.time.sleep(self.sleeptime)
