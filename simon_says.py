import time
import random
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1
game = 10 * [0]
num = 0

C = 264
D = 293.665
E = 329.628
F = 349.23
G = 391.995
A = 440
B = 493.883

while True:
    if cp.switch:
        for i in range(9):                      # generate an array of 10 numbers 0-3
            num = random.randrange(0, 4, 1)
            print(num)
            game[i] = num

        while True:
            for j in range(9):
                for k in range(j):
                    print(game)
                    if (game[k] == 0):                    # first quadrant
                        cp.pixels.fill((0, 0, 0))
                        cp.pixels[5] = ((255, 0, 0))
                        cp.pixels[6] = ((255, 0, 0))
                        cp.pixels[7] = ((255, 0, 0))
                        cp.play_tone(262, 1)
                        q = 1
                    if (game[k] == 1):                   # second quadrant
                        cp.pixels.fill((0, 0, 0))
                        cp.pixels[7] = ((0, 255, 0))
                        cp.pixels[8] = ((0, 255, 0))
                        cp.pixels[9] = ((0, 255, 0))
                        cp.play_tone(270, 1)
                        q = 2
                    if (game[k] == 2):                   # third quadrant
                        cp.pixels.fill((0, 0, 0))
                        cp.pixels[0] = ((0, 0, 255))
                        cp.pixels[1] = ((0, 0, 255))
                        cp.pixels[2] = ((0, 0, 255))
                        cp.play_tone(278, 1)
                        q = 3
                    if (game[k] == 3):                   # fourth quadrant
                        cp.pixels.fill((0, 0, 0))
                        cp.pixels[2] = ((255, 255, 0))
                        cp.pixels[3] = ((255, 255, 0))
                        cp.pixels[4] = ((255, 255, 0))
                        cp.play_tone(288, 1)
                        q = 4

                    time.sleep(1)
                    b = 0
                    if cp.touch_A1:
                        print("Touched A1!")
                        cp.pixels.fill((0, 0, 0))
                        cp.pixels[5] = ((255, 0, 0))
                        cp.pixels[6] = ((255, 0, 0))
                        cp.pixels[7] = ((255, 0, 0))
                        cp.play_tone(262, 1)
                        b = 1
                    if cp.touch_A2 or cp.touch_A3:
                        print("Touched A2/A3!")
                        cp.pixels.fill((0, 0, 0))
                        cp.pixels[7] = ((0, 255, 0))
                        cp.pixels[8] = ((0, 255, 0))
                        cp.pixels[9] = ((0, 255, 0))
                        cp.play_tone(270, 1)
                        b = 2
                    if cp.touch_A4 or cp.touch_A5:
                        print("Touched A4/A5!")
                        cp.pixels.fill((0, 0, 0))
                        cp.pixels[0] = ((0, 0, 255))
                        cp.pixels[1] = ((0, 0, 255))
                        cp.pixels[2] = ((0, 0, 255))
                        cp.play_tone(278, 1)
                        b = 3
                    if cp.touch_A6 or cp.touch_TX:
                        print("Touched A6/TX!")
                        cp.pixels.fill((0, 0, 0))
                        cp.pixels[2] = ((255, 255, 0))
                        cp.pixels[3] = ((255, 255, 0))
                        cp.pixels[4] = ((255, 255, 0))
                        cp.play_tone(288, 1)
                        b = 4

                    if (b == q):
                        print("true")
                        cp.play_tone(400, 1)
                        cp.play_tone(350, 1)

    else:
        while True:
            if cp.button_b:
                C = C * 2
                D = D * 2
                E = E * 2
                F = F * 2
                G = G * 2
                A = A * 2
                B = B * 2
                time.sleep(0.5)
            if cp.button_a:
                C = C / 2
                D = D / 2
                E = E / 2
                F = F / 2
                G = G / 2
                A = A / 2
                B = B / 2
                time.sleep(0.5)
                
            if cp.touch_A1:
                cp.play_tone(C, 0.2)
            if cp.touch_A2:
                cp.play_tone(D, 0.2)
            if cp.touch_A3:
                cp.play_tone(E, 0.2)
            if cp.touch_A4:
                cp.play_tone(F, 0.2)
            if cp.touch_A5:
                cp.play_tone(G, 0.2)
            if cp.touch_A6:
                cp.play_tone(A, 0.2)
            if cp.touch_A7:
                cp.play_tone(B, 0.2)
