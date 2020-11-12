
void setup() {
  Serial.begin(9600);

}

void loop() {
  int randNumber = random(1,50);
  char x[10];
  int number;
  
  
  for(float i=0;i<1;i+=0.01){
    number=(sin(i)*10);
    sprintf(x,"%d",number);
    Serial.write(x);
  }
}
