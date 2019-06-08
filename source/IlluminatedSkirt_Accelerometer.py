"""
    IlluminatedSkirt_Accelerometer.py

    Displays LED Illumination on the Skirt.
    If motion is detected, the LEDs shine brighter.

"""
from microbit import *
import neopixel

# Setup the Neopixel
np = neopixel.NeoPixel(pin0, 240)

r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

last_x = accelerometer.get_x() / 64
last_y = accelerometer.get_y() / 64
last_z = accelerometer.get_z() / 64

coeff = 1

while True:

    for itr in range(0, 45):
        for nop in range(0, 3):

            accele_x = accelerometer.get_x() / 64
            accele_y = accelerometer.get_y() / 64
            accele_z = accelerometer.get_z() / 64

            var_x = accele_x - last_x
            var_y = accele_y - last_y
            var_z = accele_z - last_z

            var = var_x * var_x + var_y * var_y + var_z * var_z

            last_x = accele_x
            last_y = accele_y
            last_z = accele_z

            if 255 < var:
                coeff = 4
            elif 127 < var:
                coeff = 3
            elif (63 < var) and (coeff < 2):
                coeff = 2
            elif 1 < coeff:
                coeff -= 1

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
            elif (itr ==  9): r[14] = 28
            elif (itr == 10): r[14] = 32
            elif (itr == 11): r[14] = 28
            elif (itr == 12): r[14] = 24
            elif (itr == 13): r[14] = 16
            elif (itr == 14): r[14] = 12
            elif (itr == 15): r[14] = 8
            elif (itr == 16): r[14] = 6
            elif (itr == 17): r[14] = 4
            elif (itr == 18): r[14] = 3
            elif (itr == 19): r[14] = 2
            elif (itr == 20): r[14] = 1
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
            elif (itr == 24): g[14] = 28
            elif (itr == 25): g[14] = 32
            elif (itr == 26): g[14] = 28
            elif (itr == 27): g[14] = 24
            elif (itr == 28): g[14] = 16
            elif (itr == 29): g[14] = 12
            elif (itr == 30): g[14] = 8
            elif (itr == 31): g[14] = 6
            elif (itr == 32): g[14] = 4
            elif (itr == 33): g[14] = 3
            elif (itr == 34): g[14] = 2
            elif (itr == 35): g[14] = 1
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
            elif (itr == 39): b[14] = 28
            elif (itr == 40): b[14] = 32
            elif (itr == 41): b[14] = 28
            elif (itr == 42): b[14] = 24
            elif (itr == 43): b[14] = 16
            elif (itr == 44): b[14] = 12
            elif (itr ==  0): b[14] = 8
            elif (itr ==  1): b[14] = 6
            elif (itr ==  2): b[14] = 4
            elif (itr ==  3): b[14] = 3
            elif (itr ==  4): b[14] = 2
            elif (itr ==  5): b[14] = 1
            else: b[14] = 0

            for y in range(0, 15):
                for x in range(0, 8):
                    np[30*x +    y    ] = (r[y]*coeff, g[y]*coeff, b[y]*coeff)
                    np[30*x + 14-y +15] = (r[y]*coeff, g[y]*coeff, b[y]*coeff)

            np.show()
