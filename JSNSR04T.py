from machine import Pin
import time

class SR04Sensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.trig.value(0)

    def get_distance(self):
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)

        while self.echo.value() == 0:
            pulse_start = time.ticks_us()

        while self.echo.value() == 1:
            pulse_end = time.ticks_us()

        
        pulse_duration = time.ticks_diff(pulse_end, pulse_start)
        distance = pulse_duration * 0.0343 / 2 
        return round(distance, 2) 
