# Write your code here :-)
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    # print("Hello, CircuitPython!")
    sos = [0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5]

    # for i in sos:
    #    led.value = True
    #    time.sleep(i)
    #    led.value = False
    #    time.sleep(i)

    for i in range(1, 2):
        for j in range(1, 3):
            led.value = True
            time.sleep(i)
            led.value = False
            time.sleep(i)
