# Use this code to feed paper automatically into a device for testing.
# Timing parameters here are general and not customized for a system.
# This is meant to send out a stack of sheets of paper, one by one.
# Hardware setup info here: https://github.com/piuswong-vx/sandbox-rpi
# For more info, contact pius@voting.works

# Initialize program
import qwiic_bme280
import qwiic_vl53l1x
import RPi.GPIO as GPIO
import time
import sys

print("Running paper feeder test system...")

# Define these paper feed parameters according to desired system setup
time.sleep(0.02)
timeSignal = 0.1    # length of momentary signal trigger
timeRunning = 2.5   # default length of time after start signal to stop 
pinStop = 23
pinStart = 24
pinLed = 18

# Set up output signal
GPIO.setmode(GPIO.BCM)

# Initialize paper feeder; can be started for a set time or stopped.
class Feeder:
    def __init__(self, pinStop, pinStart, pinLed, timeSignal):
        self.timeSignal = timeSignal
        self.timeRunning = timeRunning
        self.pinStop = pinStop
        self.pinStart = pinStart
        self.pinLed = pinLed
        GPIO.setup(pinStop,GPIO.OUT) #STOP
        GPIO.setup(pinStart,GPIO.OUT) #START
        GPIO.setup(pinLed,GPIO.OUT) #LED

    def start(self,timeRunning):
        GPIO.output(self.pinStart, GPIO.HIGH)
        time.sleep(timeSignal)
        GPIO.output(self.pinStart, GPIO.LOW)
        GPIO.output(self.pinLed, GPIO.HIGH)
        time.sleep(timeRunning)

    def stop(self):
        GPIO.output(self.pinStop, GPIO.HIGH)
        time.sleep(timeSignal)
        GPIO.output(self.pinStop, GPIO.LOW)
        GPIO.output(self.pinLed, GPIO.LOW)

feeder = Feeder(pinStop, pinStart, pinLed, timeSignal)

# Start the whole system
cycles = 0

try:
    # Initialize sensors
    print("\nInitializing sensors...\n")
    sensorAtmospheric = qwiic_bme280.QwiicBme280()
    sensorDist1 = qwiic_vl53l1x.QwiicVL53L1X()
    if sensorAtmospheric.is_connected() == False:
        print("The Qwiic BME280 (atmospheric) device isn't connected to the system.", 
            file=sys.stderr)
        raise Exception("Atmospheric sensor not connected.")
    else:
        print("The Qwiic BME280 (atmospheric) device is online!")
    sensorAtmospheric.begin()
    distance1 = 999
    distance1past = 999
    sensorDist1.sensor_init() 
    if (sensorDist1.sensor_init() == None):
        print("The Qwiic LV531X (IR distance) is online!")
    else:
        print("The Qwiic LV531X (IR distance) device isn't connected to the system.", 
            file=sys.stderr)
        raise Exception("Distance sensor not connected.")
    print("\nSensors initialized.\n")
    
    # Initialize paper feeder parameters
    start = time.time()
    oldTime = 0
    
    # Run paper feeder in cycles
    while True:
        cycles += 1
        print("Paper feed cycle:\t%3d" % cycles)
        feeder.start(timeRunning)
        feeder.stop()
        totalTime = time.time() - start
        print("Time elapsed, total test time:\t%.3f" % totalTime)
        print("\n")
        time.sleep(0.02)
        
        # Show sensor data
        print("Humidity (RH):\t%.3f" % sensorAtmospheric.humidity)
        print("Pressure (kPa):\t%.3f" % sensorAtmospheric.pressure)    
        print("Altitude (ft):\t%.3f" % sensorAtmospheric.altitude_feet)
        print("Temp (F):\t%.2f" % sensorAtmospheric.temperature_fahrenheit)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")
    print("STOP momentary signal...")
    feeder.stop()

except Exception as e:
    print("error!", e) 
    feeder.stop()

finally:
    print("Ending GPIO control.") 
    GPIO.cleanup() # change all GPIO to input mode.
