float voltageadjust = 138.0;//starting initial variable output at 2.5V
float check = 0;
float wantedVolts = 554;

void setup() {
  pinMode(3,OUTPUT);//PWM output pin
  //Serial.begin(9600);
}

void loop() {

  float VOLTAGEVALUE = (analogRead(A0));//read ADC value at A0
  //Serial.println(VOLTAGEVALUE);
  float error = wantedVolts-VOLTAGEVALUE;
  if ((check > (VOLTAGEVALUE+0.05))|(check < (VOLTAGEVALUE-0.05))) {
    // if voltage change is higher or lower than 0.5 of previous value (to avoid fluctuations)
    check = VOLTAGEVALUE;//store previous value
  }
  voltageadjust = voltageadjust + error*0.01;
  analogWrite(3,(int)voltageadjust);//provide PWM at PIN3

  delay(10);

}

