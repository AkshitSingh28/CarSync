

CarSync is a DIY automotive infotainment and smart dashboard system developed using a Raspberry Pi, touchscreen display, Kodi media center, GPS navigation, reverse camera integration and multiple embedded sensor modules.

The project converts a standard car dashboard into a modern connected infotainment console with navigation, media playback, parking assistance and vehicle monitoring features.

---

# Project Overview

This system was developed to create a low-cost customizable in-car infotainment platform using embedded Linux and Python automation.

The setup integrates:
- Kodi media center
- GPS navigation
- reverse camera automation
- parking assistance
- OBD-II diagnostics
- automatic brightness control
- ambient lighting
- temperature monitoring
- safe shutdown protection

The complete system is mounted inside the dashboard and powered directly from the vehicle electrical system.

---

# Main Features

## Infotainment
- Kodi media center integration
- touchscreen interface
- Bluetooth audio support
- media playback
- navigation support

## Smart Vehicle Features
- reverse camera automation
- parking distance sensing
- ambient RGB lighting
- automatic brightness adjustment
- safe shutdown on ignition OFF

## Monitoring
- GPS tracking
- live navigation
- OBD-II diagnostics
- temperature monitoring
- cooling fan control

---

# Hardware Used

| Component | Purpose |
|---|---|
| Raspberry Pi 4 | Main controller |
| 7-inch touchscreen | infotainment display |
| Raspberry Pi camera | reverse camera |
| BH1750 sensor | automatic brightness |
| DHT11 sensor | temperature monitoring |
| HC-SR04 | parking sensor |
| NEO-6M GPS module | GPS navigation |
| ELM327 OBD-II adapter | vehicle diagnostics |
| RGB LEDs | ambient lighting |
| Buck converter | 12V to 5V power |

---

# Software Stack

| Software | Purpose |
|---|---|
| Kodi | infotainment interface |
| Raspberry Pi OS | operating system |
| Python 3 | automation scripts |
| GPIO libraries | sensor control |
| OBD library | diagnostics |

---

# Folder Structure

```text
CarSync/

├── main.py
├── start.sh
├── requirements.txt
├── README.md
│
├── camera/
│   └── reversecamera.py
│
├── sensors/
│   ├── brightness.py
│   ├── temperature.py
│   ├── gps3.py
│   ├── parkingsensor.py
│   └── obdreader.py
│
├── system/
│   ├── autoshutdown.py
│   └── ambientlighting.py
│
├── assets/
├── videos/
├── diagrams/
└── experimental/
