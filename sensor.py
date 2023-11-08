import qwiic
import qwiic_bme280
import qwiic_vl53l1x
import time
import sys

# For checking devices available:
# results = qwiic.list_devices()
# print(results)

print("Running sensor.py...")

def runExample():

    print("\nVxWorks testing \n")
    sensorAtmospheric = qwiic_bme280.QwiicBme280()
    sensorDist1 = qwiic_vl53l1x.QwiicVL53L1X()

    if sensorAtmospheric.is_connected() == False:
        print("The Qwiic BME280 (atmospheric) device isn't connected to the system.", 
            file=sys.stderr)
        return
    else:
        print("The Qwiic BME280 (atmospheric) device is online!")
        
    if (sensorDist1.sensor_init() == None):
        print("The Qwiic LV531X (IR distance) is online!")
    else:
        print("The Qwiic LV531X (IR distance) device isn't connected to the system.", 
            file=sys.stderr)
        return

    print("\n======\n")
    
    sensorAtmospheric.begin()

    while True:
        print("Humidity (RH):\t%.3f" % sensorAtmospheric.humidity)

        print("Pressure (kPa):\t%.3f" % sensorAtmospheric.pressure)    

        print("Altitude (ft):\t%.3f" % sensorAtmospheric.altitude_feet)

        print("Temp (F):\t%.2f" % sensorAtmospheric.temperature_fahrenheit)
        
#       distance code
        sensorDist1.start_ranging()
        distance1 = sensorDist1.get_distance()
        time.sleep(.005)
        sensorDist1.stop_ranging()
        print("Dist 1 (mm):\t%.1f" % distance1)
        

        print("")

        time.sleep(1)

runExample()