#!/usr/bin/python3

import subprocess
import db_io, hue_io, hue_config

pushover_exec = "pushover.py"
pushover_msg = f"polling failed"
pushover_comm = [
    pushover_exec,
    pushover_msg,
]

if __name__ == "__main__":
    try:
        # gather sensor data
        light_data = {
            room: {
                "table": f"sensor_{room}",
                "state": hue_io.get_light_state(room),
            } for room in hue_config.ROOMS
        }
        temp_data = {
            "table": "sensor_temp",
            "state": hue_io.get_temp_state(),
        }

        # record data
        for room in hue_config.ROOMS:
            db_io.insert_record(light_data[room])
        db_io.insert_record(temp_data)
    except:
        subprocess.run(pushover_comm)
