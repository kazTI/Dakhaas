from Sensor.Piezo import Piezo
import RPi.GPIO as io
import time
testPiezo = Piezo(25,0)
while True:
    time.sleep(0.1)
    var = testPiezo.read()
    print(var)
