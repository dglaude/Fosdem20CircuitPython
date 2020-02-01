### main.count_down_badge.PyPortal.py

"""
Most of the code coming from:
https://learn.adafruit.com/pyportal-event-countdown-clock
Enhancement: Countdown during the event.

This example will figure out the current local time using the internet.
It draw out a countdown clock until an event occurs!
When the event is happening, make a countdown until end of event.
Once the event is over, a final graphic is shown.
"""

import time
import board
from adafruit_pyportal import PyPortal
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text.label import Label

# The time of the thing!
EVENT_YEAR = 2020
EVENT_MONTH = 2
EVENT_DAY = 2
EVENT_HOUR = 12
EVENT_MINUTE = 30

# we'll make a python-friendly structure
event_time = time.struct_time((EVENT_YEAR, EVENT_MONTH, EVENT_DAY,
                               EVENT_HOUR, EVENT_MINUTE, 0,  # we don't track seconds
                               -1, -1, False))  # we dont know day of week/year or DST

# Time of the end of the thing!
END_YEAR = 2020
END_MONTH = 2
END_DAY = 2
END_HOUR = 12
END_MINUTE = 30

# we'll make a python-friendly structure
end_time = time.struct_time((END_YEAR, END_MONTH, END_DAY,
                               END_HOUR, END_MINUTE, 0,  # we don't track seconds
                               -1, -1, False))  # we dont know day of week/year or DST

# determine the current working directory
# needed so we know where to find files
cwd = ("/"+__file__).rsplit('/', 1)[0]
# Initialize the pyportal object and let us know what data to fetch and where
# to display it
pyportal = PyPortal(status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/countdown_background.bmp")

big_font = bitmap_font.load_font(cwd+"/fonts/Helvetica-Bold-36.bdf")
big_font.load_glyphs(b'0123456789') # pre-load glyphs for fast printing
on_air_background = cwd+"/on_air_background.bmp"
its_over_background = cwd+"/its_over_background.bmp"

days_position = (8, 115)
hours_position = (100, 115)
minutes_position = (210, 115)
text_color = 0xFFFFFF

text_areas = []
for pos in (days_position, hours_position, minutes_position):
    textarea = Label(big_font, max_glyphs=3)
    textarea.x = pos[0]
    textarea.y = pos[1]
    textarea.color = text_color
    pyportal.splash.append(textarea)
    text_areas.append(textarea)
refresh_time = None

while True:
    # only query the online time once per hour (and on first run)
    if (not refresh_time) or (time.monotonic() - refresh_time) > 3600:
        try:
            print("Getting time from internet!")
            pyportal.get_local_time()
            refresh_time = time.monotonic()
        except RuntimeError as e:
            print("Some error occured, retrying! -", e)
            continue

    now = time.localtime()
    print("Current time:", now)
    remaining = time.mktime(event_time) - time.mktime(now)
    print("Time remaining (s):", remaining)
    if remaining < 0:
        # oh, the event started!
        # how much time until the end?
        remaining = time.mktime(end_time) - time.mktime(now)
        if remaining < 0:
            # oh, the event is over!
            pyportal.set_background(its_over_background)
            while True:  # that's all folks
                pass
        else:
            pyportal.set_background(on_air_background)

    secs_remaining = remaining % 60
    remaining //= 60
    mins_remaining = remaining % 60
    remaining //= 60
    hours_remaining = remaining % 24
    remaining //= 24
    days_remaining = remaining
    print("%d days, %d hours, %d minutes and %s seconds" %
          (days_remaining, hours_remaining, mins_remaining, secs_remaining))
    text_areas[0].text = '{:>2}'.format(days_remaining)  # set days textarea
    text_areas[1].text = '{:>2}'.format(hours_remaining) # set hours textarea
    text_areas[2].text = '{:>2}'.format(mins_remaining)  # set minutes textarea

    # update every 10 seconds
    time.sleep(10)
