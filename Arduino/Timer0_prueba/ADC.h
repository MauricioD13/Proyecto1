#ifndef ADC_H
#define ADC_H
#include "Arduino.h"
void config_adc();
void port_selection(int port);
byte read_adc();
#endif
