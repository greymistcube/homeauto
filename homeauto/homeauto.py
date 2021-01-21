#!/usr/bin/python3

import argparse, datetime
import db_io
import homeauto_config

def args() -> argparse.Namespace:
    desc = "wifi sensor logging script"
    parser = argparse.ArgumentParser(
        description=desc,
    )
    parser.add_argument(
        "sensor",
        help="name of last logged sensor",
        type=str,
        action='store',
    )
    args = parser.parse_args()
    return args

def sensor_living_room():
    """
    Turn off living room light if living room light has been on
    for more than specified amount of time.
    """
    pass

def sensor_kitchen():
    """
    Turn off kitchen light if kitchen light has been on
    for more than specified amount of time.
    """
    pass

def sensor_temp():
    """
    Turn on or off ac depending on temperature and other factors.
    """
    pass

def sensor_wifi():
    """
    Turn on or off appliances depending on wifi connection and other factors.
    """
    pass

def _wifi_connected() -> bool:
    pass

def _temp_cold() -> bool:
    pass

def _temp_warm() -> bool:
    pass

def _valid_month() -> bool:
    pass

def timestamp() -> float:
    return datetime.datetime.now()

if __name__ == "__main__":
    options = args()
    if options.sensor == "sensor_living_room":
        sensor_living_room()
    elif options.sensor == "sensor_kitchen":
        sensor_kitchen()
    elif options.sensor == "sensor_temp":
        sensor_temp()
    elif options.sensor == "sensor_wifi":
        sensor_wifi()
    else:
        pass
