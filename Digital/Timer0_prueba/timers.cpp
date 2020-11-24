#include "Arduino.h"
#include "timers.h"


void limit_count(int count,int prescaler){
  TCCR0A = 0;
  TCCR0B = 0;
  TCNT0 = 0;
  OCR0A = count;
  if(prescaler == 1024){
    TCCR0B |= (1<<CS02|0<<CS01|1<<CS00);
  }
  else if (prescaler == 256){
    TCCR0B |= (1<<CS02|0<<CS01|0<<CS00);
  }
  else if (prescaler == 64){
    TCCR0B |= (0<<CS02|1<<CS01|1<<CS00);
  }
  else if (prescaler == 8){
    TCCR0B |= (0<<CS02|1<<CS01|0<<CS00);
  }
  else if (prescaler == 0){
    TCCR0B |= (1<<CS02|0<<CS01|1<<CS00);
  }
}
void timer_mode(int mode){
  if(mode == 1){
    // Activar CTC
    TCCR0A |= 0x02;
    TCCR0B |= (0<<WGM02);
  }
  else if(mode == 2){
    // Activar Normal
    TCCR0A |= (0<<WGM01|0<<WGM00);
    TCCR0B |= (0<<WGM02);
  }
}
void timer_interruption(char module){
  if(module == 'A'){
    //Activar interrupcion de la comparacion A
    TIMSK0 |= (1<<OCIE0A);
    sei();
  }
  else if(module == 'B'){
    //Activar interrupcion de la comparacion B
    TIMSK0 |= (1<<OCIE0B);
    sei();
  }
  else if (module == 'N'){
    TIMSK0 |= (0<<OCIE0B);
    sei();
  }
}
