#include "Arduino.h"
#include "ADC.h"

void config_adc(int port){
    //Seleccionar puerto de salida
    if(port==0){
        ADMUX |= (0<<MUX3|0<<MUX2|0<<MUX1|0<<MUX0);
    }
    else if(port==1){
        ADMUX |= (0<<MUX3|0<<MUX2|0<<MUX1|1<<MUX0);
    }
    else if(port==2){
        ADMUX |= (0<<MUX3|0<<MUX2|1<<MUX1|0<<MUX0);
    }
    else if(port==3){
        ADMUX |= (0<<MUX3|0<<MUX2|1<<MUX1|1<<MUX0);
    }

    //Activar auto-trigger
    ADCSRA |= 1<<ADATE; 

    //Configurar fuente de auto-trigger

    //Timer/Counter0 compare march A
    ADCSRB |= (0<<ADTS2|1<<ADTS1|1<<ADTS0);
    
}
byte read_adc(){
    byte result0 = ADCL;
    byte result1 = ADCH;
    return result0;
}

