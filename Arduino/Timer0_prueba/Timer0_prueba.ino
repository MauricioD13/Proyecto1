#include "timers.h"
#include "ADC.h"
void setup() {
  Serial.begin(9600);

  pinMode(13, OUTPUT);

  limit_count(77, 1024);
  // Activar CTC
  char mode[5] = "CTC";
  timer_mode(mode);
  config_adc(0);
  timer_interruption('A');
}
//Funcion que es llamada por
void print_LED() {
  byte result;
  
  Serial.write(ADCL);
  
  Serial.write(ADCH);
  
}

void loop() {
  print_LED();
}
