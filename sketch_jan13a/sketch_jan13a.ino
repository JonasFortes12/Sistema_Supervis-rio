int sensorValue;
void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(A0, INPUT);   
}
void loop() { 
  sensorValue = analogRead(A0);

  Serial.println(sensorValue, DEC);
  delay(70);
}
