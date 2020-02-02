Slide for Fosdem'20 presentation: https://fosdem.org/2020/schedule/event/iotcircuitpython/

**Title page**

IoT with CircuitPython

Look mam, no development environment.

David Glaude

- https://github.com/dglaude/Fosdem20CircuitPython

**Partial disclosure**

- Not related to my job
(so I will not disclose)

- Not affiliated with Adafruit
(but I have stickers for you)

**What is CircuitPython**

CircuitPython is a fork of MicroPython

MicroPython is a re-implementation of Python 3 language optimised for MicroProcessor

MicroPython Damien George was initially working on STM32F405RG (M4)

PyBoard

Another KickStarter campain to port on ESP8266

Now PyBoard-D

**CircuitPython vs MicroPython**

Be aware as of 11/2016 the master branch of Adafruit's MicroPython GitHub repository has a new API which is not directly compatible with other MicroPython libraries.

- Different harware support with some overlap (STM32)
- MicroPython support interupt, asynchronous
- CircuitPython has multilingual error
- MicroPython has uLibrary
- Different Wifi offloading board
- Different BLE API (both low level)

**CircuitPython 1.0.0**
JULY 19, 2017
https://blog.adafruit.com/2017/07/19/circuitpython-1-0-0/
Based on MicroPython 1.8.7.
Support Atmel SAMD21 (aka M0) and ESP8266

**CircuitPython 2.0.0**
SEPTEMBER 12, 2017
https://blog.adafruit.com/2017/09/12/circuitpython-2-0-0/
Based on MicroPython 1.9.2.

**CircuitPython 3.0.0**
JULY 9, 2018
https://blog.adafruit.com/2018/07/09/circuitpython-3-0-0-released-adafruit-circuitpython/
Support for the SAMD51 (aka M4)
Based on MicroPython 1.9.3.

**CircuitPython 4.0.0**
MAY 20, 2019
https://blog.adafruit.com/2019/05/20/circuitpython-4-0-0-released/
Remove ESP8266 support
Support Nordic nRF52840
Add bleio
Displayio replace framebuffer
Based on MicroPython 1.9.4 @25ae98f.

**CircuitPython 5.0**
SOON
https://blog.adafruit.com/2020/01/21/circuitpython-5-0-0-beta-4-release-adafruit-circuitpython/
Support for STM32F4, iMX RT10xx and Sony Spresense microcontrollers
Better BLE

**Adafruit**

Maker company from NYC
Women-owned company founded by Limor engineer from mit
open hardware and open source

A company with values: Gender Inclusive, voting day, STEM education, Support for ...

https://www.adafruit.com/

**Ressource**

https://circuitpython.org/

100+ boards: Adafruit and other

https://learn.adafruit.com/category/circuitpython
sensor => library => example => learn guide

**Community**

- Discord: https://adafru.it/discord
- Forum: https://forums.adafruit.com/

**CircuitPython library**

- 200+ Libraries

- py: Python library
- mpy: Bytecode compiled
- frozen = build into core

**Blinka**

Circuit Python Library for
- Micro controler
- Single Board
- Personal Computer: Linux Windows Mac

https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h

**User Friendly experience**

- Appear as a USB storage
- Just edit code.py or main.py
- Add library by copying files
- Serial over USB available for REPL
- Drag and drop new firmware (UF2)

https://learn.adafruit.com/welcome-to-circuitpython

**Hello World Demo**

- REPL

- print("Hello World!")

**Mu, the recommended Editor**

- Auto-detect CircuitPython board
- Python highlight and checking
- Immediatly save the complete file
- Serial support for REPL
- Draw graphic from output
- https://madewith.mu/
- https://codewith.mu/

**Blinkt Demo**

The microcontroller Hello World

- https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code

**IoT**

- Adafruit IO
- Airlift
- PyPortal
- BLE with nRF52840

**Adafruit IO**

- Adafruit IO is a platform designed Adafruit to display, respond, and interact with your project's data.

- https://io.adafruit.com/
- https://learn.adafruit.com/welcome-to-adafruit-io

We also keep your data private (data feeds are private by default) 
and secure (we will never sell or give this data away to another company) for you. 
It's the internet of things - for everyone!

- https://learn.adafruit.com/mqtt-in-circuitpython

**AIRLIFT**

- ESP32 used as a Wifi coprocessor
- Based on Nina Fw
- Use SPI rather than uart
- On board, add-on, DIY
- Require M4, nRF52840 or above

**Demo Cheerlight**

CheerLights is an #internetofthings project by @scharler to synchronize lights to the same color at the same time all around the world.

https://cheerlights.com/
https://twitter.com/cheerlights

- PyGamer + AirLift
- PyPortal text
- PyPortal json

**BLE**

- recommendation: nRF54840 board
- GAP: Central or Periferical
- GATT: Server or Client

- https://learn.adafruit.com/circuitpython-nrf52840
- https://learn.adafruit.com/ble-hid-keyboard-buttons-with-circuitpython/understanding-ble
- https://learn.adafruit.com/category/bluefruit-slash-ble

**Demo BLE**

- Hide n Seek (beacon)
- Central/client Color (Adafruit UART protocol)


**jargon (and trademark)**

- Circuit Python: Adafruit fork of Micro Python (see rules)
- Blinka: Software layer to use Circuit Python Library on computer
- Feather: Adafruit form factor for microcontroler board
- Feather Wing: Adafruit addon board that plug on a Feather to add feature
- Circuit Playground: Adafruit round form factor board for education
- DotStar: Adafruit name for individually-addressable RGB color based on APA102/SK98225 LED
- NeoPixel: Adafruit name for individually-addressable RGB color based on the WS2812, WS2811 or SK6812 LED/drivers
- Bluefruit (LE): Adafruit name for board that support Bluetooth (and BLE)
- Airlift: Adafruit name for ESP32 based (Nina FW) Wifi/HTTPS co-processor for microprocessor
- Crickit: Robotics interface board for Circuit Playground, Microbit or Feather
- Stemma: 4 pin JST PH (2.0mm pitch) used for I2C connector
- Stemma QT: smaller 4 pin JST SH (1.0mm pitch) use for I2C connection
- Express: Board typically supporting Circuit Python that have additional storage
- Adafruit IO: Online service for IoT, dashboard, mqtt, ...

**Adafruit form factor**

- Arduino
- Feather
- ItsyBitsy
- Circuit Playground
- Micro-bit

**Peoples**

- Limor
- Phil
- Scott
- Dan
- Kattni
- ...

**Thank you**

* Thank you to the Circuit Python community for answering my question
* Question (if any time left)
* Stickers

