"""
Minimalist Cheerlight for PyPortal:
- Fetch the text API to get color in web format (#FF00FF)
- Use PyPortal and set_background to set color
"""

import time
import board
from adafruit_pyportal import PyPortal

# Set up where we'll be fetching data from
DATA_SOURCE = "http://api.thingspeak.com/channels/1417/field/2/last.txt"

pyportal = PyPortal(url=DATA_SOURCE, status_neopixel=board.NEOPIXEL)

while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
        pyportal.set_background(eval("0x"+value.lstrip("#")))
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    time.sleep(60)