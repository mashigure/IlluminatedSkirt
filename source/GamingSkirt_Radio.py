"""
    GamingSkirt_Radio.py

    Displays LED Illumination on the Skirt and communicates using Radio module of micro:bit.

"""
import radio
import neopixel
from microbit import *

# Setup the Neopixel
np = neopixel.NeoPixel(pin0, 15)

r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

radio.config(group=0x03)
radio.on()


def Illuminate():
    first = True

    # Full Coloured Illumination
    while True:
        for itr in range(0, 45):
            for nop in range(0, 3):
    
                # value of brightness shifts upside to under
                for pixel_id in range(0, 14):
                    r[14 - pixel_id] = r[13 - pixel_id]
                    g[14 - pixel_id] = g[13 - pixel_id]
                    b[14 - pixel_id] = b[13 - pixel_id]
    
                # set brightness value (Red) of top LEDs
                if (itr ==  0): r[0] = 1
                elif (itr ==  1): r[0] = 2
                elif (itr ==  2): r[0] = 3
                elif (itr ==  3): r[0] = 4
                elif (itr ==  4): r[0] = 6
                elif (itr ==  5): r[0] = 8
                elif (itr ==  6): r[0] = 12
                elif (itr ==  7): r[0] = 16
                elif (itr ==  8): r[0] = 24
                elif (itr ==  9): r[0] = 32
                elif (itr == 10): r[0] = 48
                elif (itr == 11): r[0] = 56
                elif (itr == 12): r[0] = 64
                elif (itr == 13): r[0] = 56
                elif (itr == 14): r[0] = 48
                elif (itr == 15): r[0] = 32
                elif (itr == 16): r[0] = 24
                elif (itr == 17): r[0] = 16
                elif (itr == 18): r[0] = 12
                elif (itr == 19): r[0] = 8
                elif (itr == 20): r[0] = 6
                elif (itr == 21): r[0] = 4
                elif (itr == 22): r[0] = 3
                elif (itr == 23): r[0] = 2
                elif (itr == 24): r[0] = 1
                else: r[0] = 0

                # set brightness value (Green) of top LEDs
                if (itr == 15): g[0] = 1
                elif (itr == 16): g[0] = 2
                elif (itr == 17): g[0] = 3
                elif (itr == 18): g[0] = 4
                elif (itr == 19): g[0] = 6
                elif (itr == 20): g[0] = 8
                elif (itr == 21): g[0] = 12
                elif (itr == 22): g[0] = 16
                elif (itr == 23): g[0] = 24
                elif (itr == 24): g[0] = 32
                elif (itr == 25): g[0] = 48
                elif (itr == 26): g[0] = 56
                elif (itr == 27): g[0] = 64
                elif (itr == 28): g[0] = 56
                elif (itr == 29): g[0] = 48
                elif (itr == 30): g[0] = 32
                elif (itr == 31): g[0] = 24
                elif (itr == 32): g[0] = 16
                elif (itr == 33): g[0] = 12
                elif (itr == 34): g[0] = 8
                elif (itr == 35): g[0] = 6
                elif (itr == 36): g[0] = 4
                elif (itr == 37): g[0] = 3
                elif (itr == 38): g[0] = 2
                elif (itr == 39): g[0] = 1
                else: g[0] = 0
    
                # set brightness value (Blue) of top LEDs
                if (itr == 30): b[0] = 1
                elif (itr == 31): b[0] = 2
                elif (itr == 32): b[0] = 3
                elif (itr == 33): b[0] = 4
                elif (itr == 34): b[0] = 6
                elif (itr == 35): b[0] = 8
                elif (itr == 36): b[0] = 12
                elif (itr == 37): b[0] = 16
                elif (itr == 38): b[0] = 24
                elif (itr == 39): b[0] = 32
                elif (itr == 40): b[0] = 48
                elif (itr == 41): b[0] = 56
                elif (itr == 42): b[0] = 64
                elif (itr == 43): b[0] = 56
                elif (itr == 44): b[0] = 48
                elif first == False:
                    if (itr ==  0): b[0] = 32
                    elif (itr ==  1): b[0] = 24
                    elif (itr ==  2): b[0] = 16
                    elif (itr ==  3): b[0] = 12
                    elif (itr ==  4): b[0] = 8
                    elif (itr ==  5): b[0] = 6
                    elif (itr ==  6): b[0] = 4
                    elif (itr ==  7): b[0] = 3
                    elif (itr ==  8): b[0] = 2
                    elif (itr ==  9): b[0] = 1
                    else: b[0] = 0
                else: b[0] = 0

                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (r[pixel_id], g[pixel_id], b[pixel_id])
    
                np.show()

                for receiving in range(0, 100):
                    recv = radio.receive()
                    if (recv != None) and (recv != 'Reset'):
                        return recv
                    sleep(1)

        first = False



def Effect(colour):
    while True:
        # value of brightness shifts upside to under
        for pixel_id in range(0, 14):
            r[14 - pixel_id] = r[13 - pixel_id]
            g[14 - pixel_id] = g[13 - pixel_id]
            b[14 - pixel_id] = b[13 - pixel_id]

        if colour == 'Red':
            r[0] = 64
            g[0] = 0
            b[0] = 0

        elif colour == 'Green':
            r[0] = 0
            g[0] = 64
            b[0] = 0

        elif colour == 'Blue':
            r[0] = 0
            g[0] = 0
            b[0] = 64

        elif colour == 'Yellow':
            r[0] = 64
            g[0] = 64
            b[0] = 0

        elif colour == 'Orange':
            r[0] = 64
            g[0] = 16
            b[0] = 0

        elif colour == 'Purple':
            r[0] = 16
            g[0] = 0
            b[0] = 64

        elif colour == 'Cyan':
            r[0] = 0
            g[0] = 64
            b[0] = 64

        elif colour == 'Reset':
            break

        #Iterate over each LED in the strip
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (r[pixel_id], g[pixel_id], b[pixel_id])

        # Display the current pixel data on the Neopixel strip
        np.show()

        for receiving in range(0, 100):
            recv = radio.receive()
            if recv != None:
                colour = recv
                continue


    for loop in range(0, 100):

        # value of brightness shifts upside to under
        for pixel_id in range(0, 14):
            r[14 - pixel_id] = r[13 - pixel_id]
            g[14 - pixel_id] = g[13 - pixel_id]
            b[14 - pixel_id] = b[13 - pixel_id]
   
        r[0] = int(r[0] / 2)
        g[0] = int(g[0] / 2)
        b[0] = int(b[0] / 2)

        #Iterate over each LED in the strip
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (r[pixel_id], g[pixel_id], b[pixel_id])

        # Display the current pixel data on the Neopixel strip
        np.show()

        for receiving in range(0, 100):
            recv = radio.receive()
            if (recv != None) and (recv != 'Reset'):
                return recv

    return 'Reset'


command = 'Reset'

while True:
    if command == 'Reset':
        command = Illuminate()
    else:
        command = Effect(command)
