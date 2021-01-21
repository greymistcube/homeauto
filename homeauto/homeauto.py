#!/usr/bin/python3

import argparse, datetime, os, subprocess
import homeauto_config
import db_io, ac_io, hue_io

# setting up paths
MOD_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(MOD_PATH)

pushover_exec = "pushover.py"
pushover_msg = "something has gone wrong while running homeauto.py"
pushover_comm = [
    pushover_exec,
    pushover_msg,
]

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
    room = "living_room"
    if homeauto_config.TIMEOUT[room] < _light_stopwatch(room):
        hue_io.set_light_power(room, False)
    else:
        color = _light_color("living_room")
        hue_io.set_light_color("living_room", color["hue"], color["sat"])
    return

def sensor_kitchen():
    """
    Turn off kitchen light if kitchen light has been on
    for more than specified amount of time.
    """
    room = "kitchen"
    if homeauto_config.TIMEOUT[room] < _light_stopwatch(room):
        hue_io.set_light_power(room, False)
    else:
        color = _light_color("kitchen")
        hue_io.set_light_color("kitchen", color["hue"], color["sat"])
    return

def sensor_temp():
    """
    Turn on or off ac depending on temperature and other factors.
    """
    if _wifi_connected():
        # summer month is not checked as power off may be needed
        # after month changes
        if _temp_cold() and _get_ac_state():
            _set_ac_state(False)
        elif _summer() and _temp_hot() and not _get_ac_state():
            _set_ac_state(True)
    return

def sensor_wifi():
    """
    Turn on or off appliances depending on wifi connection and other factors.
    """
    if _wifi_connected():
        hue_io.set_light_power("living_room", True)
        color = _light_color("living_room")
        hue_io.set_light_color("living_room", color["hue"], color["sat"])
        if _summer() and _temp_hot() and not _get_ac_state():
            _set_ac_state(True)
    # just turn off everything when leaving the house
    else:
        hue_io.set_light_power("living_room", False)
        hue_io.set_light_power("kitchen", False)
        _set_ac_state(False)
    return

# helper functions
def _get_ac_state() -> bool:
    record = db_io.latest_records("contro_ac")[0]
    return record[0] == "True"

def _set_ac_state(power: bool) -> None:
    # run ac_io as async process
    if power:
        arg = "on"
    else:
        arg = "off"
    ac_io_exec = os.path.join(DIR_PATH, "ac_io.py")
    ac_io_comm = [ac_io_exec, arg]
    subprocess.Popen(ac_io_comm)
    return

def _wifi_connected() -> bool:
    record = db_io.latest_records("sensor_wifi")[0]
    return record[0] == "True"

def _temp_cold() -> bool:
    record = db_io.latest_records("sensor_temp")[0]
    return float(record[0]) < homeauto_config.TEMP_LO

def _temp_hot() -> bool:
    record = db_io.latest_records("sensor_temp")[0]
    return float(record[0]) > homeauto_config.TEMP_HI

def _light_stopwatch(room: str) -> float:
    """
    Roughly estimates how long light has been on.
    """
    records = db_io.latest_records(f"sensor_{room}")
    records = [(record[0] == "True", record[1]) for record in records]
    false_index = -1
    for i in range(len(records)):
        if not records[i][0]:
            false_index = i
            break
    records = records[:false_index]
    if records:
        return timestamp() - records[-1][1]
    else:
        return 0

def _light_color(room: str) -> dict:
    if room == "living_room":
        hour = datetime.datetime.now().hour
        color = _hour_to_light_color(hour)
        return color
    else:
        return homeauto_config.COLOR["pure"]

def _hour_to_light_color(hour: int):
    if 2 <= hour and hour < 10:
        return homeauto_config.COLOR["warm"]
    elif 10 <= hour and hour < 20:
        return homeauto_config.COLOR["ghost"]
    else:
        return homeauto_config.COLOR["candle"]

def _summer() -> bool:
    date = datetime.datetime.now()
    return date.month in homeauto_config.SUMMER_MONTHS

def timestamp() -> float:
    return datetime.datetime.now().timestamp()

if __name__ == "__main__":
    options = args()
    try:
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
    except:
        subprocess.run(pushover_comm)
