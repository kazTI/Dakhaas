#define pin1 6
#define pin2 7
#define pin3 8
#define pin4 9

void setup() {
  // put your setup code here, to run once:
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin4, OUTPUT);
  //stop
  moveRobot(0, 0);
  delay(5000);
  //def moveForward(self):
  moveRobot(1, -1);
  delay(5000);
  //def moveForwardLeft(self):
  moveRobot(0, -1);
  delay(5000);
  //def moveForwardRight(self):
  moveRobot(1, 0);
  delay(5000);
  //def moveBackward(self):
  moveRobot(-1, 1);
  delay(5000);
  //def moveBackwardLeft(self):
  moveRobot(0, 1);
  delay(5000);
  //def moveBackwardRight(self):
  moveRobot(-1, 0);
  delay(5000);
  //def moveLeft(self):
  moveRobot(-1, -1);
  delay(5000);
  //def moveRight(self):
  moveRobot(1, 1);
  delay(5000);
}

void loop() {
  // put your main code here, to run repeatedly:
  moveRobot(1, -1);
}

void moveRobot(int left, int right)
{
  if (left == -1)
  {
    digitalWrite(pin2, 0);
    delayMicroseconds(1);
    digitalWrite(pin1, 1);
  }
  else if (left == 0)
  {
    digitalWrite(pin1, 0);
    digitalWrite(pin2, 0);
  }
  else if (left == 1)
  {
    digitalWrite(pin1, 0);
    delayMicroseconds(1);
    digitalWrite(pin2, 1);
  }

  if (right == -1)
  {
    digitalWrite(pin4, 0);
    delayMicroseconds(1);
    digitalWrite(pin3, 1);
  }
  else if (right == 0)
  {
    digitalWrite(pin3, 0);
    digitalWrite(pin4, 0);
  }
  else if (right == 1)
  {
    digitalWrite(pin3, 0);
    delayMicroseconds(1);
    digitalWrite(pin4, 1);
  }
}
