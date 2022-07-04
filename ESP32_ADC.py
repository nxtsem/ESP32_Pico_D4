# Import required libraries
from micropython import const
from machine import Pin, ADC
import time

# TinyPICO Hardware Pin Assignments
BAT_VOLTAGE = const(35)  # ADC1, GPIO 32-35
BAT_CHARGE = const(34)

#  ADC channels
ADC2_1 = const(32)  # ADC2, through VBAT resistor divider
ADC2_2 = const(33)  # ADC2, direct input (0 to 1.2V range)

def get_ADC_avg(PAD_num):
    sum = 0
    high = 0
    low = 4095
    readings = 10  # total number of ADC measurements
    adc = ADC(Pin(PAD_num))  # ADC pin to read
    
    # adc.atten(ADC.ATTN_0DB)    # default, 1.2V range
    
    for _ in range(readings):
        time.sleep_ms(5)  # some loop delay might be necessary
        adc_read = adc.read()  # Read the value
        sum = sum + adc_read
        if adc_read > high:
            high = adc_read
        if adc_read < low:
            low = adc_read
            
    sum = sum - high - low  # throw out high and low measurements
    avg = sum / (readings - 2)    
    v_avg = avg / 4000   # 4000 = 1.000V ... on my TinyPicos (1/4mV per LSB)
    
    print("Debug ADC: avg high low ", avg, high, low, end="")  #debug print
    return v_avg
    
# TinyPico VBAT divider ratio is .26578 (160K/602K).  With 3.7V VBAT, there should be 
# about 983mV applied to the ADC (3.7 * .26578).  Calc ADC reading is 3932 (983 * 4).       

VBAT = get_ADC_avg(BAT_VOLTAGE) * 3.7  # Multiply by 3.7V, our reference voltage
print("\nVBAT= {:.3f}V".format(VBAT))
      
ADC_avg = get_ADC_avg(ADC2_1)
print("\nADC1 avg= {:.3f}V".format(ADC_avg))
    
