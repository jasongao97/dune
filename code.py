# Dune
# By Jason & Marcel

import time
import board
import pwmio
import neopixel

STEPS_PER_REVOLUTION = 800
NUMPIXELS = 45

# LED setup
led = pwmio.PWMOut(board.CLK, frequency=20000, duty_cycle=0)

pixels = neopixel.NeoPixel(board.DATA, NUMPIXELS, auto_write=False, pixel_order=(1, 0, 2, 3))

lastTimeChange = 0
currentStep = 0

def calculateBrightness(index):
    pos = index / NUMPIXELS
    center = (currentStep % STEPS_PER_REVOLUTION) / STEPS_PER_REVOLUTION

    x = abs(pos - center)

    if x > 0.5:
        x = 1 - x

    result = (-6 * x + 1) * 255
    return int(min(max(result, 0), 255))

while True:
    now = time.monotonic()

    if (now - lastTimeChange) > 0.02:
        currentStep += 1
        lastTimeChange = now

    for i in range(NUMPIXELS):
        brightness = calculateBrightness(i)
        pixels[i] = (0, 0, 0, brightness)

    pixels.show()
    led.duty_cycle = 20000
