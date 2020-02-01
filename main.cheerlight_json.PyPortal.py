### main.cheerlight_json.PyPortal.py

"""
Cheerlight for PyPortal:
- Fetch the JSON API to get color both in text and web format (#FF00FF)
- Use PyPortal to display the data
- Change the background color to match Cheerlight value
cheerlight_json_PyPortal
"""

import time
import board
from adafruit_pyportal import PyPortal

# Set up where we'll be fetching data from
DATA_SOURCE = "https://api.thingspeak.com/channels/1417/feeds/last.json"
COLOR_TEXT = ['field1']
COLOR_HEX = ['field2']

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE,
                    json_path=(COLOR_TEXT, COLOR_HEX),
                    status_neopixel=board.NEOPIXEL,
                    text_font=cwd+"/fonts/Collegiate-50.bdf",
                    text_position=((140, 100),(5, 210)), # text location
                    text_color=(0x0, 0x0), # text color
                    text_maxlen=(30, 10), # max text size for quote & author
                   )

# speed up projects with lots of text by preloading the font!
pyportal.preload_font()

while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
        pyportal.set_background(int(value[1].lstrip("#"), 16))
    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)
    time.sleep(10)

