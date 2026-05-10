
import RPi.GPIO as GPIO
import time

red = 17
green = 27
blue = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

print("ambient lights started")

while True:

    GPIO.output(red, 1)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)

    print("red")

    time.sleep(2)

    GPIO.output(red, 0)
    GPIO.output(green, 1)
    GPIO.output(blue, 0)

    print("green")

    time.sleep(2)

    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 1)

    print("blue")

    time.sleep(2)
