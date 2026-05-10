import time
import os
import board
import adafruit_bh1750

i2c = board.I2C()

sensor = adafruit_bh1750.BH1750(i2c)

print("auto brightness started")

while True:

    try:

        lux = sensor.lux

        print("Lux =", round(lux, 2))

        # daytime
        if lux > 130:

            os.system(
                'sudo sh -c "echo 120 > /sys/class/backlight/rpi_backlight/brightness"'
            )

            print("day mode")

        # night
        else:

            os.system(
                'sudo sh -c "echo 255 > /sys/class/backlight/rpi_backlight/brightness"'
            )

            print("night mode")

        time.sleep(1)

    except Exception as e:

        print("sensor error", e)

        time.sleep(2)
