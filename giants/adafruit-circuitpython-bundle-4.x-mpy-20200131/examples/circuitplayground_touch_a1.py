"""This example prints to the serial console when you touch capacitive touch pad A1."""
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print('Touched pad A1')
