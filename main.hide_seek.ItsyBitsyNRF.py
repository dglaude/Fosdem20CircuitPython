"""
ItsyBitsy nRF52840 Express transmitter for the "Circuit Playground Bluefruit Ornament Proximity" demo

If you don't have two Circuit Playground Bluefruit but still want to play the hide and seek.
You can use this code on a ItsyBitsy nRF52840 Express to advertise a color.
The buttons change the color when advertising.

Use your Circuit Playground Bluefruit to seek your ItsyBitsy nRF52840
"""
### Original code https://learn.adafruit.com/hide-n-seek-bluefruit-ornament/code-with-circuitpython

import time
import board

### Configure the user switch of the ItsyBitsy nRF52840
from digitalio import DigitalInOut, Direction, Pull
switch = DigitalInOut(board.SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

### Configure the DotStar available on the ItsyBitsy nRF52840
import adafruit_dotstar as dotstar

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
rgb = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
rgb.brightness = 0.3
rgb[0] = (0, 0, 0)

from adafruit_ble import BLERadio
from adafruit_ble.advertising.adafruit import AdafruitColor

ble = BLERadio()
advertisement = AdafruitColor()

# The color pickers will cycle through this list with buttons A and B.
color_options = [0x110000,
                 0x111100,
                 0x001100,
                 0x001111,
                 0x000011,
                 0x110011,
                 0x111111,
                 0x221111,
                 0x112211,
                 0x111122]

i = 0
### Trick to force a first color "change"
last_i = -1

print("Broadcasting color")

### The original code has two mode, the Feather nRF52840 version is broadcasts only.
while True:

### If the color has change, or if this is the first time, start advertising the color and set the RGB as feedback indicator.
    if last_i != i:
        last_i = i
        color = color_options[i]
        rgb[0] = ( (color>>16)&0xFF , (color>>8)&0xFF , color&0xFF )
        print("New color {:06x}".format(color))
        advertisement.color = color
        ble.stop_advertising()
        ble.start_advertising(advertisement)
        time.sleep(0.5)

### Verify if the user press the button (false if pressed) and change color.
    if not switch.value:
        i += 1
        i %= len(color_options)

### We should never reach this point because of the infinit loop.
ble.stop_advertising()