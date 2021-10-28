# Write your code here :-)
from adafruit_circuitplayground import cp
import math
import time

while (True):
    # using colors from resistors
    zero = (32, 32, 32)  # black
    one = (102, 51, 0)  # brown
    two = (255, 0, 0)  # red
    three = (255, 128, 0)  # orange
    four = (255, 255, 0)  # yellow
    five = (0, 255, 0)  # green
    six = (0, 0, 255)  # blue
    seven = (127, 0, 255)  # violet
    eight = (128, 128, 128)  # grey
    nine = (255, 255, 255)  # white
    
    num = 12345

    ones = math.floor((num) % 10)
    tens = math.floor((num/10) % 10)
    hundreds = math.floor((num/100) % 10)
    thousands = math.floor((num/1000) % 10)
    tenthousands = math.floor((num/10000) % 10)

    i = 0

    if i == 0:
        x = zero
    if i == 1:
        x = (one)
    if i == 2:
        x = (two)
    if i == 3:
        x = (three)
    if i == 4:
        x = (four)
    if i == 5:
        x = (five)
    if i == 6:
        x = (six)
    if i == 7:
        x = (seven)
    if i == 8:
        x = (eight)
    if i == 9:
        x = (nine)

    cp.pixels.brightness = 0.1

    for i in range(10):
        if ones == i:
            cp.pixels[0] = x
    for i in range(10):
        if tens == i:
            cp.pixels[1] = x
    for i in range(10):
        if hundreds == i:
            cp.pixels[2] = x
    for i in range(10):
        if thousands == i:
            cp.pixels[3] = x
    for i in range(10):
        if tenthousands == i:
            cp.pixels[4] = x

    print(ones)
    print(tens)
    print(hundreds)
    print(thousands)
    print(tenthousands)
    
    time.sleep(.05)
