#!/usr/bin/env python3

import time
from colorsys import hsv_to_rgb
from unicornhatmini import UnicornHATMini
from gpiozero import Button
from signal import pause

print("""Busy Light Test

Press Ctrl+C to exit!

""")

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.1)



def pressed(button):

    if button.pin.number == 5:
        unicornhatmini.set_all(255, 0, 0)
    elif button.pin.number == 6:
        unicornhatmini.set_all(0,255,0)
    
    unicornhatmini.show()

button_a = Button(5)
button_b = Button(6)
button_x = Button(16)
button_y = Button(24)

try:
    button_a.when_pressed = pressed
    button_b.when_pressed = pressed
    button_x.when_pressed = pressed
    button_y.when_pressed = pressed

    pause()

except KeyboardInterrupt:
    button_a.close()
    button_b.close()
    button_x.close()
    button_y.close()
