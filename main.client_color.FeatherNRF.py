### main.client_color.FeatherNRF.py

"""
### This is the "client" that connect to the "Central".
### Start this "client" on Feather nRF52840
### Start the "Central" on ItsyBitsy nRF52840

Demonstration of a Bluefruit BLE Central/client.
Connects to the first BLE UART peripheral it finds.
Sends Bluefruit ColorPackets, 3 per second.
Green if switch is not pushed.
Red if switch is pushed.
"""

import time

import board
from digitalio import DigitalInOut, Direction, Pull

#from adafruit_bluefruit_connect.packet import Packet
# Only the packet classes that are imported will be known to Packet.
from adafruit_bluefruit_connect.color_packet import ColorPacket

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

import neopixel
rgb = neopixel.NeoPixel(board.NEOPIXEL, 1)

rgb.brightness = 0.3
rgb[0] = (255, 255, 255)

ble = BLERadio()

led = DigitalInOut(board.RED_LED)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

uart_connection = None

# See if any existing connections are providing UARTService.
if ble.connected:
    for connection in ble.connections:
        if UARTService in connection:
            uart_connection = connection
        break

while True:
    if not uart_connection:
        for adv in ble.start_scan(ProvideServicesAdvertisement, timeout=5):
            if UARTService in adv.services:
                uart_connection = ble.connect(adv)
                break
        # Stop scanning whether or not we are connected.
        ble.stop_scan()

    if uart_connection and uart_connection.connected:
        led.value = True
    else:
        led.value = False

    while uart_connection and uart_connection.connected:
        if switch.value:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)
        rgb[0] = color
        print(color)
        color_packet = ColorPacket(color)
        try:
            uart_connection[UARTService].write(color_packet.to_bytes())
        except OSError:
            pass
        led.value = not led.value
        time.sleep(0.3)
