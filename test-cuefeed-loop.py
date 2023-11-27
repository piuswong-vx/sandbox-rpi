# Use this code to help test if the paper feeder is set up correctly.
# This is meant to send out a stack of sheets of paper, one by one.
# Hardware setup info here: https://github.com/piuswong-vx/sandbox-rpi

import RPi.GPIO as GPIO
import time
import sys

print("Running test-cuefeed-loop.py...")

# Set up output signal
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT) #LED
GPIO.setup(23,GPIO.OUT) #STOP
GPIO.setup(24,GPIO.OUT) #START

time.sleep(0.02)
timeSignal = 0.1
timeRunning = 2.5

def startFeeder():
    print("START momentary signal...")
    GPIO.output(24, GPIO.HIGH)
    time.sleep(timeSignal)
    GPIO.output(24, GPIO.LOW)
    time.sleep(timeRunning)

def stopFeeder():
    print("STOP momentary signal...")
    GPIO.output(23, GPIO.HIGH)
    time.sleep(timeSignal)
    GPIO.output(23, GPIO.LOW)

try:
    print("set LED high")
    GPIO.output(18, GPIO.HIGH)
    start = time.time()
    
    while True:
        print("** START for a few seconds. **")
        startFeeder()
        stopFeeder()
        time.sleep(1)
        end = time.time()
        print("Time elapsed: ", end - start)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")
    print("STOP momentary signal...")
    stopFeeder()

except:
    print("error!") 
    stopFeeder()

finally:
    print("Ending GPIO control.") 
    GPIO.cleanup() # change all GPIO to input mode.
