float delayy = 100;
int sensorValue;
float timee = 0;


void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(A0, INPUT);   
}
void loop() { 
  sensorValue = analogRead(A0);
  timee += delayy/1000; 


  Serial.print("nan, ");
  Serial.print((float)timee, 1);
  Serial.print("\n");

/*
  Serial.print((int)sensorValue);
  Serial.print(", ");
  Serial.print((float)timee, 1);
  Serial.print("\n");

*/

  
  delay(delayy);
}
