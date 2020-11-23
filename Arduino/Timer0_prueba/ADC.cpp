#include "Arduino.h"
#include "ADC.h"

void config_adc(){

   ADMUX &= 0xDF; // ADLAR en cero, ajuste a la derecha
 
   ADMUX |= 1 << REFS0; // AVcc para la referencia de voltaje

   ADMUX &= 0xF0;// Limpiar bits para ajustar la entrada
   
   ADMUX |= 1<<REFS0; // Referencia de voltaje
   
   ADCSRA |= (1<<ADEN); // Activar ADC
 
   ADCSRA |= (1<<ADATE); // Activar auto-trigger
 
  
   ADCSRB &= 0xF8; // Limpiar bits para la fuente

   ADCSRB |= (0<<ADTS2|1<<ADTS1|1<<ADTS0); // Fuente de inicio Timer/Couter0 compare match A

  
   ADCSRA |= 0x07; // Prescaler 128, recomendacion ADC por encima de 200k no es confiable
  //CLKADC = 16MHz/128 = 125Hz
 
  //Activar interrupciones del ADC
   ADCSRA |= B00001000;
 
  // Enable global interrupts
  // AVR macro included in <avr/interrupts.h>, which the Arduino IDE
  // supplies by default.
   sei();
 
  // Bandera de actualizacion
  
  //ADSC para iniciar la conversion
  ADCSRA |= 1<<ADSC;
    
}
void port_selection(int port){
  ADMUX |= port;
}
byte read_adc(){
    byte result0 = ADCL;
    byte result1 = ADCH;
    return result0;
}
