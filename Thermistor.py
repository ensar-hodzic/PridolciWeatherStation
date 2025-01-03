from machine import ADC
import math

class Thermistor:
    def __init__(self, pin, series_resistor=10000.0, offset = 35):
        self.adc = ADC(pin)
        self.series_resistor = series_resistor
        self.offset = offset
        self.c1 = 1.009249522e-03
        self.c2 = 2.378405444e-04
        self.c3 = 2.019202697e-07


    def get_temperature(self):
        adc_value = self.adc.read_u16()
        Vo = adc_value / 65535 * 3.3
        R2 = self.series_resistor * (Vo / (3.3-Vo))
        logR2 = math.log(R2)
        T = (1.0 / (self.c1 + self.c2*logR2 + self.c3*logR2**3))
        T = T - 273.15 + self.offset
        return round(T, 2)
