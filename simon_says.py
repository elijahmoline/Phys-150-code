# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import random
import numpy
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1
game = numpy.zeros((1, 9))
num = 0

for i in range(9):                      # generate an array of 10 numbers 0-3
    num = random.randrange(0, 3, 1)
    print(num)
    game[i] = num
    
while True:
    
    for j in range(9):
        for k in range(j):
            if (game[k] == 0):                    # first quadrant
                cp.pixels.fill((0, 0, 0))
                cp.pixels[5] = ((255, 0, 0))
                cp.pixels[6] = ((255, 0, 0))
                cp.pixels[7] = ((255, 0, 0))
                cp.play_tone(262, 1)
            if (game[k] == 1):                   # second quadrant
                cp.pixels.fill((0, 0, 0))
                cp.pixels[7] = ((0, 255, 0))
                cp.pixels[8] = ((0, 255, 0))
                cp.pixels[9] = ((0, 255, 0))
                cp.play_tone(270, 1)    
            if (game[k] == 2):                   # third quadrant
                cp.pixels.fill((0, 0, 0))
                cp.pixels[0] = ((0, 0, 255))
                cp.pixels[1] = ((0, 0, 255))
                cp.pixels[2] = ((0, 0, 255))
                cp.play_tone(278, 1)
            if (game[k] == 3):                   # fourth quadrant
                cp.pixels.fill((0, 0, 0))
                cp.pixels[2] = ((255, 255, 0))
                cp.pixels[3] = ((255, 255, 0))
                cp.pixels[4] = ((255, 255, 0))
                cp.play_tone(288, 1)
            
            if ((cp.touch_A1 & game[k] == 0) | ((cp.touch_A2 | cp.touch_A3) & game[k] == 1) | ((cp.touch_A4 | cp.touch_A5) & game[k] == 2) | ((cp.touch_A6 | cp.touch_TX) & game[k] == 3)):
                
            else:
                cp.play_tone(266, 1)
                cp.play_tone(300, 1)

    if cp.touch_A1:
        print("Touched A1!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[5] = ((255, 0, 0))
        cp.pixels[6] = ((255, 0, 0))
        cp.pixels[7] = ((255, 0, 0))
        cp.play_tone(262, 1)
    if cp.touch_A2:
        print("Touched A2!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[7] = ((0, 255, 0))
        cp.pixels[8] = ((0, 255, 0))
        cp.pixels[9] = ((0, 255, 0))
        cp.play_tone(270, 1)
    if cp.touch_A3:
        print("Touched A3!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[7] = ((0, 255, 0))
        cp.pixels[8] = ((0, 255, 0))
        cp.pixels[9] = ((0, 255, 0))
        cp.play_tone(270, 1)
    if cp.touch_A4:
        print("Touched A4!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = ((0, 0, 255))
        cp.pixels[1] = ((0, 0, 255))
        cp.pixels[2] = ((0, 0, 255))
        cp.play_tone(278, 1)
    if cp.touch_A5:
        print("Touched A5!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = ((0, 0, 255))
        cp.pixels[1] = ((0, 0, 255))
        cp.pixels[2] = ((0, 0, 255))
        cp.play_tone(278, 1)
    if cp.touch_A6:
        print("Touched A6!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[2] = ((255, 255, 0))
        cp.pixels[3] = ((255, 255, 0))
        cp.pixels[4] = ((255, 255, 0))
        cp.play_tone(288, 1)
    if cp.touch_TX:
        print("Touched TX!")
        cp.pixels.fill((0, 0, 0))
        cp.pixels[2] = ((255, 255, 0))
        cp.pixels[3] = ((255, 255, 0))
        cp.pixels[4] = ((255, 255, 0))
        cp.play_tone(288, 1)
    time.sleep(0.1)
