// Testing interrupt-based analog reading
// ATMega328p
#include "timers.h"
// Note, many macro values are defined in <avr/io.h> and
// <avr/interrupts.h>, which are included automatically by
// the Arduino interface

// High when a value is ready to be read
volatile int readFlag;

// Value to store analog result
volatile int analogVal;


// Initialization
void setup(){
  
  pinMode(7,OUTPUT);
  Serial.begin(9600);
  limit_count(77,1024);
  timer_mode(1);
  timer_interruption('A');
  
  ADMUX &= 0xDF; // ADLAR en cero, ajuste a la derecha
 
  ADMUX |= 1 << REFS0; // AVcc para la referencia de voltaje

  ADMUX &= 0xF0;// Limpiar bits para ajustar la entrada
 
  ADMUX |= 0; //Puerto A0

  ADCSRA |= (1<<ADEN); // Activar ADC
 
  ADCSRA |= (1<<ADATE); // Activar auto-trigger
 
  
  ADCSRB &= 0xF8; // Limpiar bits para la fuente

  ADCSRB |= (0<<ADTS2|1<<ADTS1|1<<ADTS0); // Fuente de inicio Timer/Couter0 compare match A

  
  ADCSRA |= 0x07; // Prescaler 128, recomendacion ADC por encima de 200k no es confiable
  //CLKADC = 16MHz/128 = 125Hz
 
  // Set ADIE in ADCSRA (0x7A) to enable the ADC interrupt.
  // Without this, the internal interrupt will not trigger.
  ADCSRA |= B00001000;
 
  // Enable global interrupts
  // AVR macro included in <avr/interrupts.h>, which the Arduino IDE
  // supplies by default.
  sei();
 
  // Kick off the first ADC
  readFlag = 0;
  // Set ADSC in ADCSRA (0x7A) to start the ADC conversion
  ADCSRA |= 1<<ADSC;
}


// Processor loop
void loop(){

  // Check to see if the value has been updated
  if (readFlag == 1){
   
    // Perform whatever updating needed
   
    readFlag = 0;
  }
 
  // Whatever else you would normally have running in loop().
 
}


// Interrupt service routine for the ADC completion
ISR(ADC_vect){

  // Done reading
  readFlag = 1;
 
  // Must read low first
  analogVal = ADCL | (ADCH << 8);
  PORTD |= analogVal <<8; //Salida por el puerto 7
  
 
}
