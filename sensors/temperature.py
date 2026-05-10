import Adafruit_DHT
import RPi.GPIO as GPIO
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 26

fan_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)

print("temperature monitor started")

while True:

    humidity, temperature = Adafruit_DHT.read(
        DHT_SENSOR,
        DHT_PIN
    )

    if temperature is not None:

        print("Temperature =", temperature)

        if temperature >= 35:

            GPIO.output(fan_pin, GPIO.HIGH)

            print("fan on")

        else:

            GPIO.output(fan_pin, GPIO.LOW)

            print("fan off")

    else:

        print("sensor not reading")

    time.sleep(3)
