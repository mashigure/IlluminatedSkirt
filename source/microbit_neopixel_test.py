"""
    microbit_neopixel_test.py

    Turns on an LED in order of connected.
    This example requires a strip of 240 Neopixels (WS2812) connected to pin0.

"""
from microbit import *
import neopixel

# Setup the Neopixel
np = neopixel.NeoPixel(pin0, 240)

while True:
    #Iterate over each LED in the strip
    for itr in range(0, len(np)):

        for pixel_id in range(0, len(np)):
            brightness = 0
            
            if itr == pixel_id:
                brightness = 30

            np[pixel_id] = (brightness, brightness, brightness)

        # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(50)
