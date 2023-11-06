# sandbox-rpi
Prep for Vx Rpi instrumentation

## References
* General setup and BME280 atmospheric sensor setup: https://learn.sparkfun.com/tutorials/introduction-to-the-raspberry-pi-gpio-and-physical-computing?_gl=1*190akoj*_ga*MTUxODQ3NjE5OC4xNjk5MTI2Njc5*_ga_T369JS7J9N*MTY5OTEzNzUwMS4yLjEuMTY5OTEzODI1MS42MC4wLjA.&_ga=2.259974664.362080396.1699126679-1518476198.1699126679
* Qwiic distance sensor library: https://github.com/sparkfun/Qwiic_VL53L1X_Py


## Notes and Troubleshooting

### Installing dependencies and sensor libraries

The `externally-managed-environment` error may come up when installing drivers for the Qwiic sensors.  For example when running: `sudo pip install sparkfun-qwiic-bme280`.  Some [guidance](https://stackoverflow.com/questions/75602063/pip-install-r-requirements-txt-is-failing-this-environment-is-externally-mana/75696359#75696359) led to running a virtual environment:

```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install sparkfun-qwiic-bme280
```
This seems to work as of 11/5/23!  Check `sensor.py` for details.