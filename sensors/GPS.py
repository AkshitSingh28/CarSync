import serial
import pynmea2

port = serial.Serial(
    "/dev/ttyAMA0",
    baudrate=9600,
    timeout=1
)

print("gps started")

while True:

    try:

        line = port.readline().decode(
            'ascii',
            errors='replace'
        )

        if '$GPRMC' in line:

            msg = pynmea2.parse(line)

            print("Latitude :", msg.latitude)
            print("Longitude:", msg.longitude)

            if msg.spd_over_grnd:

                speed = float(msg.spd_over_grnd) * 1.852

                print("Speed =", round(speed, 1), "km/h")

            print("----------------------")

    except Exception as e:

        print("gps error", e)
