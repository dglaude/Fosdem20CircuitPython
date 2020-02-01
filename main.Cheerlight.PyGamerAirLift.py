### main.Cheerlight.PyGamerAirLift.py

"""
 Cheerlight for PyGamer + AirLift FeatherWing

 Original source from ladyada and friends:
 https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/blob/master/examples/esp32spi_cheerlights.py

 Learn more about Cheerlight: https://cheerlights.com/

 Modification for PyGamer + Airlift by David Glaude
 Use the airlift feather RGB LED for status_light
 Use the five build in NEOPIXEL to cheerlight color

 Requires the following library structure in /lib:
 * adafruit_bus_device
 * adafruit_esp32spi
 * adafruit_fancyled
 adafruit_requests.mpy
 adafruit_rgbled.mpy
 neopixel.mpy
 simpleio.mpy

 You need a file secrets.py that contain your SSID and Wifi password:
 secrets = {
    'ssid' : 'My_SSID',
    'password' : 'My_Password'
    }
"""

import time
import board
import busio
from digitalio import DigitalInOut

from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager

import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("ESP32 SPI webclient test")

DATA_SOURCE = "https://api.thingspeak.com/channels/1417/feeds.json?results=1"
DATA_LOCATION = ["feeds", 0, "field2"]

esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
"""Use below for Most Boards"""
#status_light = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2) # Uncomment for Most Boards
"""Uncomment below for ItsyBitsy M4"""
#status_light = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
"""Uncomment for externally defined RGB LED"""
import adafruit_rgbled
from adafruit_esp32spi import PWMOut
RED_LED = PWMOut.PWMOut(esp, 26)
GREEN_LED = PWMOut.PWMOut(esp, 27)
BLUE_LED = PWMOut.PWMOut(esp, 25)
status_light = adafruit_rgbled.RGBLED(RED_LED, BLUE_LED, GREEN_LED)
### This code for controling the LED on the airlift is borrowed from:
### https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/blob/master/examples/esp32spi_aio_post.py
### And it was added by https://github.com/brentru

wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)

# neopixels
### Internally to the PyGamer there are 5 Neopixel connected to D8
### ( https://learn.adafruit.com/adafruit-pygamer/pinouts )
### But to access the NEOPIXEL I need that wifimanager use another LED status
pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, brightness=0.3)
pixels.fill(0)

# we'll save the value in question
last_value = value = None

while True:
    try:
        print("Fetching json from", DATA_SOURCE)
        response = wifi.get(DATA_SOURCE)
        print(response.json())
        value = response.json()
        for key in DATA_LOCATION:
            value = value[key]
            print(value)
        response.close()
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        continue

    if not value:
        continue
    if last_value != value:
        color = int(value[1:], 16)
        red = color >> 16 & 0xFF
        green = color >> 8 & 0xFF
        blue = color& 0xFF
        gamma_corrected = fancy.gamma_adjust(fancy.CRGB(red, green, blue)).pack()
        pixels.fill(gamma_corrected)
        last_value = value
    response = None
    time.sleep(10)