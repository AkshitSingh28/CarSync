

import time
import RPi.GPIO as GPIO
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)

reverse_pin = 17

GPIO.setup(reverse_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

camera = PiCamera()

camera.resolution = (800, 480)
camera.rotation = 180
camera.framerate = 20

camera_running = False

print("reverse camera ready")

try:

    while True:

        gear = GPIO.input(reverse_pin)

        # reverse gear active
        if gear == 1:

            if camera_running == False:

                print("camera started")

                camera.start_preview(
                    fullscreen=True,
                    window=(0, 0, 800, 480)
                )

                camera_running = True

        # reverse gear removed
        else:

            if camera_running == True:

                print("camera stopped")

                camera.stop_preview()

                camera_running = False

        time.sleep(0.1)

except KeyboardInterrupt:

    print("closing camera")

    camera.stop_preview()
    camera.close()

    GPIO.cleanup()
