const int dir = 12;
const int stp = 13;

int stpState = LOW;
long previousMillis = 0;

long interval = 15;

void setup() {
  pinMode(dir, OUTPUT);
  pinMode(stp, OUTPUT);
  
  digitalWrite(dir, LOW);  
}

void loop()
{ 
  unsigned long currentMillis = millis();
  if(currentMillis - previousMillis > interval) {
    // save the last time you blinked the LED 
    previousMillis = currentMillis;   

    stpState = !stpState;
    // TOGGLE state of motor to provide HIGH LOW toggle
    digitalWrite(stp, stpState);            
  }
}

