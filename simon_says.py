# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example uses the capacitive touch pads on the Circuit Playground. They are located around
the outer edge of the board and are labeled A1-A6 and TX. (A0 is not a touch pad.) This example
lights up all the NeoPixels a different color of the rainbow for each pad touched!"""
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1

while True:
    if cp.touch_A1:
        print("Touched A1!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[5]=((255, 0, 0))
        cp.pixels[6]=((255, 0, 0))
        cp.pixels[7]=((255, 0, 0))
        cp.play_tone(262, 1)
    if cp.touch_A2:
        print("Touched A2!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[7]=((0, 255, 0))
        cp.pixels[8]=((0, 255, 0))
        cp.pixels[9]=((0, 255, 0))
        cp.play_tone(270, 1)
    if cp.touch_A3:
        print("Touched A3!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[7]=((0, 255, 0))
        cp.pixels[8]=((0, 255, 0))
        cp.pixels[9]=((0, 255, 0))
        cp.play_tone(270, 1)
    if cp.touch_A4:
        print("Touched A4!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0]=((0, 0, 255))
        cp.pixels[1]=((0, 0, 255))
        cp.pixels[2]=((0, 0, 255))
        cp.play_tone(278, 1)
    if cp.touch_A5:
        print("Touched A5!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0]=((0, 0, 255))
        cp.pixels[1]=((0, 0, 255))
        cp.pixels[2]=((0, 0, 255))
        cp.play_tone(278, 1)
    if cp.touch_A6:
        print("Touched A6!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[2]=((255, 255, 0))
        cp.pixels[3]=((255, 255, 0))
        cp.pixels[4]=((255, 255, 0))
        cp.play_tone(288, 1)
    if cp.touch_TX:
        print("Touched TX!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[2]=((255, 255, 0))
        cp.pixels[3]=((255, 255, 0))
        cp.pixels[4]=((255, 255, 0))
        cp.play_tone(288, 1)
    time.sleep(0.1)
