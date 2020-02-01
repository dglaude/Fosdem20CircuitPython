### main.Central_color.ItsyBitsy.py
###
### This is "Central" to run on ItsyBitsy nRF52840
### Please connect a "client" such as:
### * Bluefruit app on Android phone
### * "client" on Feather nRF52840
#
# https://github.com/adafruit/Adafruit_CircuitPython_BLE/blob/master/examples/ble_bluefruit_color_picker.py
# https://learn.adafruit.com/circuitpython-nrf52840/neopixel-color
# CircuitPython NeoPixel Color Picker Example

# Adapted for ItsyBitsy and it's DotStar
import board

### Configure the DotStar available on the ItsyBitsy nRF52840
import adafruit_dotstar as dotstar

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket

from digitalio import DigitalInOut, Direction
led = DigitalInOut(board.BLUE_LED)
led.direction = Direction.OUTPUT

ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
pixels = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
pixels.brightness = 0.3
pixels[0] = (0, 0, 0)

while True:
    led.value = True
    pixels[0] = (0, 0, 0)
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        led.value = False
        packet = Packet.from_stream(uart_server)
        if isinstance(packet, ColorPacket):
            pixels.fill(packet.color)