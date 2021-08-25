#Author: Ramon Rooijens

from Camera.Camera import Camera

class PyCamera(Camera):
    import time
    import picamera
    frameIndex = 0
    previousTime = 0

    def __init__(self,  framesPerSecond, timeLimitInSeconds):
        import logging
        self.logger = logging.getLogger('PyCamera')
        self.logger.debug('Made PyCamera object.')
    #Init camera
        self.cam = self.picamera.PiCamera()

        self.framesPerSecond = framesPerSecond
    #Maximum time allowed for capturing frames (avoid endless saves)
        self.timeLimitInSeconds = timeLimitInSeconds
    #Maximum amount of frames in timelimit
        self.frameLimit = self.framesPerSecond * self.timeLimitInSeconds
    #Set previous time to runtime
        self.previousTime = self.time.time()

    def checkCamera(self):
        super().checkCamera()
        if(self.frameIndex < self.frameLimit):          #If limit not reached
            if (int(self.time.time() - self.previousTime >=
                    60/self.framesPerSecond)):#If Interval between frames surpassed
                start_time = self.time.time()
                self.captureFrame(self.frame)(self.FRAME)          #Capture frame
                self.previousTime = self.time.time()   #Reset interval timer

    def captureFrame(self, frame):
        self.time.sleep(2)
        self.cam.capture('/home/pi/Documents/dakhaas/Camera Frames/frame%04d.jpg' % frame)

cam = Camera()
