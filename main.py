from JSNSR04T import SR04Sensor
from Thermistor import Thermistor
import time

ultrasonic = SR04Sensor(trig_pin=0, echo_pin=1)
thermistor = Thermistor(pin = 26)

while True:
    distance = ultrasonic.get_distance()
    temperature = thermistor.get_temperature()
    print(f"Temperature: {temperature} °C")
    if 20 < distance < 400:
        print("Distance:", distance, "cm")
    else:
        print("Out Of Range")
    time.sleep(5)