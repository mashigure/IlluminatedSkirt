"""
    IlluminatedSkirtDemo.py

    Displays LED Illumination on the Skirt.
    On nico-video, You can watch how to work this program:
    https://www.nicovideo.jp/watch/sm35141886

"""
from microbit import *
import neopixel

# Setup the Neopixel
np = neopixel.NeoPixel(pin0, 240)

r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:

    for itr in range(0, 45):
        for nop in range(0, 3):

            # value of brightness shifts upside to under
            for pixel_id in range(0, 14):
                r[pixel_id] = r[pixel_id+1]
                g[pixel_id] = g[pixel_id+1]
                b[pixel_id] = b[pixel_id+1]

            # set brightness value (Red) of top LEDs
            if (itr ==  0): r[14] = 1
            elif (itr ==  1): r[14] = 2
            elif (itr ==  2): r[14] = 3
            elif (itr ==  3): r[14] = 4
            elif (itr ==  4): r[14] = 6
            elif (itr ==  5): r[14] = 8
            elif (itr ==  6): r[14] = 12
            elif (itr ==  7): r[14] = 16
            elif (itr ==  8): r[14] = 24
            elif (itr ==  9): r[14] = 32
            elif (itr == 10): r[14] = 48
            elif (itr == 11): r[14] = 56
            elif (itr == 12): r[14] = 64
            elif (itr == 13): r[14] = 56
            elif (itr == 14): r[14] = 48
            elif (itr == 15): r[14] = 32
            elif (itr == 16): r[14] = 24
            elif (itr == 17): r[14] = 16
            elif (itr == 18): r[14] = 12
            elif (itr == 19): r[14] = 8
            elif (itr == 20): r[14] = 6
            elif (itr == 21): r[14] = 4
            elif (itr == 22): r[14] = 3
            elif (itr == 23): r[14] = 2
            elif (itr == 24): r[14] = 1
            else: r[14] = 0

            # set brightness value (Green) of top LEDs
            if (itr == 15): g[14] = 1
            elif (itr == 16): g[14] = 2
            elif (itr == 17): g[14] = 3
            elif (itr == 18): g[14] = 4
            elif (itr == 19): g[14] = 6
            elif (itr == 20): g[14] = 8
            elif (itr == 21): g[14] = 12
            elif (itr == 22): g[14] = 16
            elif (itr == 23): g[14] = 24
            elif (itr == 24): g[14] = 32
            elif (itr == 25): g[14] = 48
            elif (itr == 26): g[14] = 56
            elif (itr == 27): g[14] = 64
            elif (itr == 28): g[14] = 56
            elif (itr == 29): g[14] = 48
            elif (itr == 30): g[14] = 32
            elif (itr == 31): g[14] = 24
            elif (itr == 32): g[14] = 16
            elif (itr == 33): g[14] = 12
            elif (itr == 34): g[14] = 8
            elif (itr == 35): g[14] = 6
            elif (itr == 36): g[14] = 4
            elif (itr == 37): g[14] = 3
            elif (itr == 38): g[14] = 2
            elif (itr == 39): g[14] = 1
            else: g[14] = 0

            # set brightness value (Blue) of top LEDs
            if (itr == 30): b[14] = 1
            elif (itr == 31): b[14] = 2
            elif (itr == 32): b[14] = 3
            elif (itr == 33): b[14] = 4
            elif (itr == 34): b[14] = 6
            elif (itr == 35): b[14] = 8
            elif (itr == 36): b[14] = 12
            elif (itr == 37): b[14] = 16
            elif (itr == 38): b[14] = 24
            elif (itr == 39): b[14] = 32
            elif (itr == 40): b[14] = 48
            elif (itr == 41): b[14] = 56
            elif (itr == 42): b[14] = 64
            elif (itr == 43): b[14] = 56
            elif (itr == 44): b[14] = 48
            elif (itr ==  0): b[14] = 32
            elif (itr ==  1): b[14] = 24
            elif (itr ==  2): b[14] = 16
            elif (itr ==  3): b[14] = 12
            elif (itr ==  4): b[14] = 8
            elif (itr ==  5): b[14] = 6
            elif (itr ==  6): b[14] = 4
            elif (itr ==  7): b[14] = 3
            elif (itr ==  8): b[14] = 2
            elif (itr ==  9): b[14] = 1
            else: b[14] = 0

            for y in range(0, 15):
                for x in range(0, 8):
                    np[30*x +    y    ] = (r[y], g[y], b[y])
                    np[30*x + 14-y +15] = (r[y], g[y], b[y])

            np.show()
