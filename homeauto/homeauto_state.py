import os, datetime
import db_io, hue_io, path, homeauto_config

def ac_power() -> bool:
    """
    Determines if ac is on.
    """
    try:
        record = db_io.latest_records("contro_ac")[0]
        return record[0] == "True"
    except:
        return False

def wifi_connected() -> bool:
    """
    Determines if wifi is connected
    """
    try:
        record = db_io.latest_records("sensor_wifi")[0]
        return record[0] == "True"
    except:
        return False

def temp_cold() -> bool:
    """
    Determines if temperature is too cold.
    """
    record = db_io.latest_records("sensor_temp")[0]
    return float(record[0]) < homeauto_config.TEMP_LO

def temp_hot() -> bool:
    """
    Determines if temperature is too hot.
    """
    record = db_io.latest_records("sensor_temp")[0]
    return float(record[0]) > homeauto_config.TEMP_HI

def summer_month() -> bool:
    """
    Determines if current time is summer.
    """
    return datetime.datetime.now().month in homeauto_config.SUMMER_MONTHS

def mode() -> str:
    """
    Determines which mode the system is in.
    """
    try:
        record = db_io.latest_records("sensor_mode")[0]
        return record[0]
    except:
        return "auto"

def light_power(room: str) -> bool:
    """
    Determines if light is on.
    """
    return hue_io.get_group_power(room)

def light_power_long(room: str) -> bool:
    """
    Determines if light has been on for too long.
    """
    records = db_io.latest_records(f"sensor_{room}")
    records = [(record[0] == "True", record[1]) for record in records]
    false_index = -1
    for i in range(len(records)):
        if not records[i][0]:
            false_index = i
            break
    records = records[:false_index]
    # either every recorded light state was on
    # or at least the latest recorded light state was on
    if records:
        on_time = datetime.datetime.now().timestamp() - records[-1][1]
        return homeauto_config.TIMEOUT[room] < on_time
    # the latest recorded light state was off
    else:
        return False
