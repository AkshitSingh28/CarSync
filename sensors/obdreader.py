

import obd
import time

print("connecting to obd")

connection = obd.OBD()

print("obd connected")

speed_cmd = obd.commands.SPEED
rpm_cmd = obd.commands.RPM

while True:

    try:

        speed = connection.query(speed_cmd)

        rpm = connection.query(rpm_cmd)

        print("Speed :", speed.value)
        print("RPM   :", rpm.value)

        print("----------------")

        time.sleep(2)

    except Exception as e:

        print("obd error", e)
