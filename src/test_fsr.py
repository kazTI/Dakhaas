from Sensor.FSR import FSR

fsr = FSR(4)

while True:
	print(fsr.read())
