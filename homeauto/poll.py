#!/usr/bin/python3

import db_io, hue_io, hue_config

if __name__ == "__main__":
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

    for room in hue_config.ROOMS:
        db_io.insert_record(light_data[room])
    db_io.insert_record(temp_data)
