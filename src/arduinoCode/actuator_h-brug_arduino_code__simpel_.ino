/*  Arduino DC Motor Control - PWM | H-Bridge | L298N  -  Example 01

    by Dejan Nedelkovski, www.HowToMechatronics.com
*/

#define enA 9
#define in1 6
#define in2 7


int rotDirection = 0;
int incomingByte = 0;

void setup() {
  Serial.begin(9600);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  // Set initial rotation direction
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
}

void loop() {

  int pwmOutput = 230;
  analogWrite(enA, pwmOutput); // Send PWM signal to L298N Enable pin
  
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
    if(incomingByte == 49)
    {
      Serial.println("changing direction");
      changeDirection();
    }
  }
}

void changeDirection()
{
  int directionChanged = 0;
  if(rotDirection == 0 && directionChanged == 0)
  {
    Serial.println("backward");
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    rotDirection = 1;
    directionChanged = 1;
    delay(200);
  }
  if(rotDirection == 1 && directionChanged == 0)
  {
    Serial.println("forward");
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    rotDirection = 0;
    directionChanged = 1;
    delay(200);
  }
}
