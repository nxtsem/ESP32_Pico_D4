# Import required libraries
from micropython import const
from machine import Pin, ADC, DAC
import time
import array

#  ADC
ADC2_1 = const(32)  # ADC#2, 0 to 1V with resistor divider
ADC2_2 = const(33)  # ADC#2, direct input

# DAC
DAC1 = const(25)
DAC2 = const(26)

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


print("DAC2 connected to ADC2_2")
adc_buf = array.array('f', (0.0 for _ in range(256)))
dac2 = DAC(Pin(DAC2))
for i in range(0, 81):
    dac2.write(i)
    print("DAC code= {}".format(i), end=" ")
    adc_buf[i] = get_ADC_avg(ADC2_2)
    print()
#    print(adc_buf[i])

dac2.write(0)  
# dac2.deinit()  # internally disconnect dac2, not supported
