#!/usr/bin/python3

import subprocess
import path, db_io, hue_io, hue_config

if __name__ == "__main__":
    try:
        # gather sensor data
        group_data = {
            group: {
                "table": f"sensor_{group}",
                "state": hue_io.get_group_power(group),
            } for group in hue_config.GROUPS
        }
        temp_data = {
            "table": "sensor_temp",
            "state": hue_io.get_temp_state(),
        }

        # record data
        for group in hue_config.GROUPS:
            db_io.insert_record(group_data[group])
        db_io.insert_record(temp_data)
    except:
        subprocess.run([path.PUSHOVER, "polling failed"])
