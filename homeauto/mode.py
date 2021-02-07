#!/usr/bin/python3

import argparse
import db_io, homeauto_config

def args() -> argparse.Namespace:
    desc = "mode sensor logging script"
    parser = argparse.ArgumentParser(
        description=desc,
    )
    parser.add_argument(
        "mode",
        help="state of mode to log",
        type=str,
        action='store',
    )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    options = args()
    if (
        options.mode != "auto"
        and options.mode not in homeauto_config.MODE_COLORS
    ):
        raise ValueError(f"invalid value for mode: {options.mode}")
    data = {
        "table": "sensor_mode",
        "state": options.mode,
    }
    db_io.insert_record(data)
