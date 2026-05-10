

import time
import RPi.GPIO as GPIO

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("parking sensor started")

def get_distance():

    GPIO.output(TRIG, False)

    time.sleep(0.05)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        stop = time.time()

    distance = (stop - start) * 34300 / 2

    return round(distance, 1)

try:

    while True:

        dist = get_distance()

        print("Distance =", dist, "cm")

        if dist < 25:
            print("STOP")

        elif dist < 50:
            print("VERY CLOSE")

        elif dist < 100:
            print("CAUTION")

        else:
            print("SAFE")

        print("----------------")

        time.sleep(0.5)

except KeyboardInterrupt:

    GPIO.cleanup()
