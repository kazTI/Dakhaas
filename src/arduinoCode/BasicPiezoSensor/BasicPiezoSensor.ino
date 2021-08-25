#define piezoSensor A0 // the piezo is connected to analog pin 0
#define threshold 100  // threshold value to decide when the robot bumping into something has enougb impact

int piezoValue = 0;      // variable to store the value read from the sensor pin

void setup() {
  Serial.begin(9600);       // use the serial port
}

void loop() {
  // read the sensor and store it in the variable sensorReading:
  piezoValue = analogRead(piezoSensor);

  if (piezoValue >= threshold) {
 //   Serial.println("Knock!");
  }
  Serial.print("Raw value: ");
  Serial.println(piezoValue);
  Serial.println();
  delay(100);  // delay to avoid overloading the serial port buffer
}
