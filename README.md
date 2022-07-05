ESP32_ADC.py : Sample Micropython ADC averaging code for ESP32 (TinyPico board). Exclude highest reading and lowest reading.

ESP32_ADC_avg results : VBAT ADC results and ADC stability results with 1.000V applied.

ESP32_ADC_1V_range_plot : ADC noise plot with 1.000V applied (Y axis = LSB).

ESP32_DAC2_at_3_29V_VDD_plot : DAC plot of all codes (8 bit) at 3.29V VDD.

ESP32_DAC2_output_voltage : All DAC codes (8 bit) at 3.29V VDD.

ESP32_Loopback.py: DAC2 (8 bit) connected to ADC2 (12 bit SAR).

ESP32_Loopback_DAC_ADC_plot : DAC2 to ADC2 plot (ADC 1V range, 0dB atten), (DAC codes 0 to 80).

ESP32_Loopback_11dB_atten : DAC2 to ADC2 plot (ADC 11dB atten), (DAC codes 0 to 255), use 0dB and R divider for better performance.
