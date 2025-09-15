# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Be sure to check the learn guides for more usage information.

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!

Author(s): Melissa LeBlanc-Williams for Adafruit Industries
"""

import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

from datetime import datetime
# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.D5)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90,                            # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180,  # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
# disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
# pylint: enable=line-too-long

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height

shk = Image.open("shark.png")
shk2 = Image.open("fish.png")
shk3 = Image.open("bubble.png")


# Choose the X offset (in pixels)
x_offset = 10  # move right by 50 pixels
y_offset = 0   # no vertical shift

# Paste the image onto the canvas at the desired offset


while True:

    canvas = Image.new("RGB", (width, height))
    now = datetime.now()

    # Extract hour and minute as integers

    hour = now.hour%12      # 0-23
    if hour == 0: 
        hour = 12
    minute = now.minute  # 0-59
    second= now.second  # 0-59

    #if the hour is from 1 to 5
    for i in range(0, 6):
        if i == hour: 
            break
        canvas.paste(shk, (i * 25, 0))


    if hour >=5 and hour <= 10: 
        for i in range(0, 6):
            if i == hour: 
                break
            canvas.paste(shk, (i * 25, 25))

    if hour >=10 and hour <13: 
        for i in range(0, 2):
            if i == hour: 
                break
            canvas.paste(shk, (i * 25, 50))



    # print(minute)
    # if minute >=0: 
    #     for i in range(0, minute/2 + 1):
    #         canvas.paste(shk2, (i * 25, 75))

    # if minute >=10: 
    #     for i in range(0, minute/2 + 1):
    #         if i == minute/2: 
    #             break
    #         canvas.paste(shk2, (i * 25, 100))

    # if minute >=20: 
    #     for i in range(0, minute/2 + 1):
    #         if i == minute/2: 
    #             break
    #         canvas.paste(shk2, (i * 25, 125))

    # if minute >=30: 
    #     for i in range(0, ):
    #         if i == minute/2: 
    #             break
    #         canvas.paste(shk2, (i * 25, 150))

    # if minute >=40: 
    #     for i in range(0, 6):
    #         if i == minute/2: 
    #             break
    #         canvas.paste(shk2, (i * 25, 175))

    # if minute >=50 and minute <= 60: 
    #     for i in range(0, 6):
    #         if i == minute/2 * : 
    #             break
    #         canvas.paste(shk2, (i * 25, 200))



    check  = minute // 2 + 3 

    for i in range(3, 9): 
        for j in range(0, 6):
            # print(check)
            if check <= 0: 
                break
            canvas.paste(shk2, ((j * 25)+2, i * 25))
            check -=1





    print(second)
    if second >=0: 
        canvas.paste(shk3, (0, 220))

    if second >=12: 
        canvas.paste(shk3, (25, 220))

    if second >=24: 
        canvas.paste(shk3, (50, 220))

    if second >=48: 
        canvas.paste(shk3, (75, 220))

    if second >=60: 
        canvas.paste(shk3, (100, 220))
    disp.image(canvas)

