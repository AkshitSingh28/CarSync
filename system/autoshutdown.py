import os
import time
import RPi.GPIO as GPIO

shutdown_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(
    shutdown_pin,
    GPIO.IN,
    pull_up_down=GPIO.PUD_DOWN
)

print("shutdown protection active")

try:

    while True:

        power = GPIO.input(shutdown_pin)

        print("power state =", power)

        if power == 0:

            print("external power removed")

            time.sleep(2)

            # check again before shutdown
            if GPIO.input(shutdown_pin) == 0:

                print("shutting down raspberry pi")

                os.system("sudo shutdown -h now")

        time.sleep(1)

except KeyboardInterrupt:

    GPIO.cleanup()
