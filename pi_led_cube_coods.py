#! /usr/bin/python
import RPi.GPIO as GPIO
import time

#define a 3d list of pins to light up for that x,y,x coordinate
pins=[[[[40,7],[40,11],[40,35],[40,37]],[[40,12],[40,13],[40,31],[40,33]],[[40,15],[40,16],[40,23],[40,29]],[[40,18],[40,19],[40,21],[40,22]]],
      [[[38,7],[38,11],[38,35],[38,37]],[[38,12],[38,13],[38,31],[38,33]],[[38,15],[38,16],[38,23],[38,29]],[[38,18],[38,19],[38,21],[38,22]]],
      [[[36,7],[36,11],[36,35],[36,37]],[[36,12],[36,13],[36,31],[36,33]],[[36,15],[36,16],[36,23],[36,29]],[[36,18],[36,19],[36,21],[36,22]]],
      [[[32,7],[32,11],[32,35],[32,37]],[[32,12],[32,13],[32,31],[32,33]],[[32,15],[32,16],[32,23],[32,29]],[[32,18],[32,19],[32,21],[32,22]]]]

#GPIO Pins that control a layer
LAYERS = [40,38,36,32]

#GPIO Pins that control the LEDS on a layer
GRID = [7,11,35,37,12,13,31,33,15,16,23,29,18,19,21,22]


def initialize_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # Layers
    GPIO.setup(32, GPIO.OUT)
    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(38, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)

    # Individual LED
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)

def reset_grid():
    for led in GRID:
        GPIO.output(led,False)

def reset_layers():
    for layer in LAYERS:
        GPIO.output(layer,False)

def set(x,y,z):
    print(pins[x][y][z])
    GPIO.output(pins[x][y][z][0],True)
    GPIO.output(pins[x][y][z][1],True)

def reset(x,y,z):
    GPIO.output(pins[x][y][z][0],False)
    GPIO.output(pins[x][y][z][1],False)


if __name__ == '__main__':
    initialize_gpio()
    reset_grid()
    reset_layers()

    set(0,0,0)
    time.sleep(1)
    reset(0,0,0)

    set(1,1,1)
    time.sleep(1)
    reset(1,1,1)

    set(2,2,2)
    time.sleep(1)
    reset(2,2,2)

    set(3,3,3)
    time.sleep(1)
    reset(3,3,3)
