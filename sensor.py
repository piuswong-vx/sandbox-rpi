import qwiic_bme280
import time
import sys

print("Running sensor.py...")

def runExample():

    print("\nSparkFun BME280 Sensor + Raspberry Pi Example \n")
    mySensor = qwiic_bme280.QwiicBme280()

    if mySensor.is_connected() == False:
        print("The Qwiic BME280 device isn't connected to the system.", 
            file=sys.stderr)
        return

    mySensor.begin()

    while True:
        print("Humidity:\t%.3f" % mySensor.humidity)

        print("Pressure:\t%.3f" % mySensor.pressure)    

        print("Altitude:\t%.3f" % mySensor.altitude_feet)

        print("Temperature:\t%.2f" % mySensor.temperature_fahrenheit)       

        print("")

        time.sleep(1)


runExample()