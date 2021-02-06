#!/usr/bin/python3

import argparse, subprocess
import path, homeauto_control, homeauto_state

pushover_exec = path.PUSHOVER
pushover_msg = "something has gone wrong while running homeauto.py"
pushover_comm = [
    pushover_exec,
    pushover_msg,
]

def args() -> argparse.Namespace:
    desc = "homeauto main script"
    parser = argparse.ArgumentParser(
        description=desc,
    )
    parser.add_argument(
        "sensor",
        help="name of the last logged sensor",
        type=str,
        action='store',
    )
    args = parser.parse_args()
    return args

def sensor_living_room():
    """
    Control living room light when triggered by living room sensor.
    """
    group = "living_room"
    if homeauto_state.light_power_long(group):
        homeauto_control.light_power(group, False)
    elif (
        not homeauto_state.light_power(group)
        and homeauto_state.mode() != "auto"
    ):
        homeauto_control.mode("auto")
    else:
        homeauto_control.light_color(group)
    return

def sensor_kitchen():
    """
    Control kitchen light when triggered by kitchen sensor.
    """
    group = "kitchen"
    if homeauto_state.light_power_long(group):
        homeauto_control.light_power(group, False)
    else:
        homeauto_control.light_color(group)
    return

def sensor_mode():
    """
    Control living room light when triggered by mode change.
    """
    group = "living_room"
    homeauto_control.light_color(group)
    return

def sensor_temp():
    """
    Control ac when triggered by temp sensor.
    """
    # ac control should only be triggered by temperature change
    # only if wifi is connected
    if homeauto_state.wifi_connected():
        if (
            homeauto_state.summer_month()
            and homeauto_state.temp_hot()
            and not homeauto_state.ac_power()
        ):
            homeauto_control.ac_power(True)
        elif (
            homeauto_state.temp_cold()
            and homeauto_state.ac_power()
        ):
            homeauto_control.ac_power(False)
    return

def sensor_wifi():
    """
    Control appliances when triggered by wifi sensor.
    """
    if homeauto_state.wifi_connected():
        homeauto_control.light_power("living_room", True)
        homeauto_control.light_color("living_room")
        if (
            homeauto_state.summer_month()
            and homeauto_state.temp_hot()
            and not homeauto_state.ac_power()
        ):
            homeauto_control.ac_power(True)
    # turn off everything if wifi drops
    else:
        homeauto_control.light_power("living_room", False)
        homeauto_control.light_power("kitchen", False)
        homeauto_control.ac_power(False)
    return

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
        elif options.sensor == "sensor_mode":
            sensor_mode()
        else:
            pass
    except:
        subprocess.run([
            path.PUSHOVER,
            "something has gone wrong while running homeauto.py",
        ])
