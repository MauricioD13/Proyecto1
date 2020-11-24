  
// Testing interrupt-based analog reading
// ATMega328p
#include "timers.h"
// Note, many macro values are defined in <avr/io.h> and
// <avr/interrupts.h>, which are included automatically by
// the Arduino interface
#include "ADC.h"
// High when a value is ready to be read
volatile int readFlag;

// Value to store analog result
volatile int analogVal;

volatile int port;



char result[10];
// Initialization
void setup(){
  
  pinMode(7,OUTPUT);
  Serial.begin(9600);
  limit_count(82,64);// f = 16M/(2*prescaler*(1 + count))
  timer_mode(1);
  timer_interruption('A');
  config_adc();
  port = 1;
  port_selection(port);
 
}


// Processor loop
void loop(){

 //Mirar si ha habido conversion
  if (readFlag == 1){
   
   //Actualizar bandera
   
    readFlag = 0;
  }
  
 
}


// Interrupt service routine for the ADC completion
ISR(ADC_vect){

  // Done reading
  readFlag = 1;

 
  // Must read low first
  analogVal = ADCL;
  //Cambio de canal 
  //Debe ser cuando se termine una conversion
  if(ADMUX == 0x40){
    ADMUX &= 0xF0; 
    ADMUX |= 0x01;
    analogVal=analogVal | (ADCH << 8);
    Serial.print(analogVal);
    Serial.print("\t");
   Serial.flush();
   
  }else if (ADMUX == 0x41){
    ADMUX &= 0xF0; 
    ADMUX |= 0x02;
    analogVal=analogVal | (ADCH << 8);
    Serial.print(0);
    Serial.print("\t");
    Serial.flush();
  }else if (ADMUX == 0x42){
    ADMUX &= 0xF0; 
    ADMUX |= 0x00;
    analogVal=analogVal | (ADCH << 8);
    Serial.println(0);

    
  }else if (ADMUX == 0x41){
    ADMUX &= 0xF0; 
    ADMUX |= 0x00;
    analogVal=analogVal | (ADCH << 8);
    Serial.println(analogVal);

    Serial.flush();
    
  }else{
    int number = ADMUX;
    Serial.print(number);
    Serial.println(" Error");
    Serial.flush();
  }
 
  //PORTD |= analogVal <<8; //Salida por el puerto 7
  
 
}
