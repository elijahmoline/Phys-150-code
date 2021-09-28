# Write your code here :-)
from adafruit_circuitplayground import cp
import time
import math

cp.pixels.brightness = .05
on = (127, 127, 127)
off = (0, 0, 0)
while True:
    x, y, z = cp.acceleration
    theta = math.asin(x/(math.sqrt(x ** 2 + y ** 2 + z**2)))
    degree = theta*180/math.pi
    # print(degree)
    data = 0
    for i in range(1000):
        data += degree
    d = round(data / 1000,1)
    print(d)

    cp.pixels.fill(off)
    if (d > 85):

        cp.pixels[0] = on
    if (d > 85.5):

        cp.pixels[1] = on
    if (d > 86):

        cp.pixels[2] = on
    if (d > 86.5):

        cp.pixels[3] = on
    if (d > 87):

        cp.pixels[4] = on
    if (d > 87.5):

        cp.pixels[5] = on
    if (d > 88):

        cp.pixels[6] = on
    if (d > 88.5):

        cp.pixels[7] = on
    if (d > 89):

        cp.pixels[8] = on
    if (d > 89.5):

        cp.pixels[9] = on

    time.sleep(.1)
