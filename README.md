# sandbox-rpi
Prep for Vx Rpi instrumentation

## References
* [General setup and BME280 atmospheric sensor setup](https://learn.sparkfun.com/tutorials/introduction-to-the-raspberry-pi-gpio-and-physical-computing?_gl=1*190akoj*_ga*MTUxODQ3NjE5OC4xNjk5MTI2Njc5*_ga_T369JS7J9N*MTY5OTEzNzUwMS4yLjEuMTY5OTEzODI1MS42MC4wLjA.&_ga=2.259974664.362080396.1699126679-1518476198.1699126679)
* [Qwiic distance sensor library](https://github.com/sparkfun/Qwiic_VL53L1X_Py)
* [Qwiic atmospheric sensor library](https://github.com/sparkfun/Qwiic_BME280_Py)


## Notes and Troubleshooting

### Hardware notes

1. Connect Qwiic shim through [Pins 1-6 on RPi 4](https://pinout.xyz/).  Connect the Qwiic connect cable to the shim, and then attach the heatsink (if necessary) over that, since it will block access to the shim.  
2. Connect the sensors.
	* Connect the BME280 atmospheric sensor via the Qwiic cable.  Insert cable on left side.  
	* Connect the VL53L4CD distance sensor via another Qwiic cable, daisy-chaining it from the atmospheric sensor.
	* Connect other sensors as needed in a similar way, if they are different types of sensors.  If you need to connect more sensors of the same type, use an appropriate breakout board.
3. Connect indicator LED through Pin 12 (GPIO 18) and Pin 6 (GND); Pin 12 &rarr; LED+ (long leg) &rarr; 330 ohm resistor &rarr; Pin 6 / ground
4. Connect the relay that will send momentary start/stop signals.  
	* For Relay 1 (STOP signal), connect Pin 17 on the RPi (3.3V) &rarr; VCC on the relay, Pin 16 (GPIO 23) &rarr; IN, and Pin 20 (GND) to GND.
	* For Relay 2 (START signal), connect Pin 17 on the RPi (3.3V) &rarr; VCC on the relay, Pin 18 (GPIO 24) &rarr; IN, and Pin 20 (GND) to GND.
	* In the default setup as of 11/2023, the relays connect to an M12 cable, where the black ground wire connects to the relay COM outputs, the yellow wire connects to the STOP relay NO output (normally open), and the red wire connects to the START relay NO output (normally open).   


### Installing dependencies and sensor libraries

* Check connections with `i2cdetect -y 1`.

* The `externally-managed-environment` error may come up when installing drivers for the Qwiic sensors.  For example when running: `sudo pip install sparkfun-qwiic-bme280`.  Some [guidance](https://stackoverflow.com/questions/75602063/pip-install-r-requirements-txt-is-failing-this-environment-is-externally-mana/75696359#75696359) led to running a virtual environment:

    ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        python3 -m pip install sparkfun-qwiic RPi.GPIO
    ```

    ...or install a specific library, like `python3 -m pip install sparkfun-qwiic-bme280`

* To exit the virtual environment, use the command `deactivate`.

This might work as of 11/5/23... Check `sensor.py` for details.

### Running

* The libraries have to have been installed first as described above.
* Start the virtual environment: `source .venv/bin/activate`
* Run with:

    ```shell
        python sensor.py
    ```


### Remote dev

* You can use [VSCode's remote SSH extension](https://www.raspberrypi.com/news/coding-on-raspberry-pi-remotely-with-visual-studio-code/) to program remotely, if needed.
* Make sure to enable SSH from the RPi settings, and to find the IP address of the RPi, possibly through the router adminstrator.
* You can log into the RPi via the terminal with `ssh [username]@[ipaddress]`