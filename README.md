# Fosdem20CircuitPython
Example code for IoT CircuitPython demo

This is work in progress for "Hello World" kind of demonstration of Circuit Python.

To run one demo file choose a demo file, verify it is for your hardware and rename it to 'main.py'.

All the wifi demo require that you write a "secret.py" file that contain connection parameter.
Some demo require Adafruit IO account, also to be writen in secret.py.

All the files in the lib library are from the CircuitPython library bundle: adafruit-circuitpython-bundle-5.x-mpy-20200127

Code are written and test with beta 3 or 4 release of Circuit Python 5.0.

Hardware available for the demo:
* PyPortal: SAMD51 M4 + Airlift + Screen (also contain RGB LED, Red LED, light sensor, touch screen)
* nRF52840: microprocessor with BLE capabilities + Airlift Featherwing
* Circuit Playground Bluefruit: BLE and a lot of sensor, RGB LED, button, ...

