#!/usr/bin/python3

import argparse
import db_io

def args() -> argparse.Namespace:
    desc = "wifi sensor logging script"
    parser = argparse.ArgumentParser(
        description=desc,
    )
    parser.add_argument(
        "state",
        help="state of wifi connection",
        type=str,
        choices=["on", "off"],
        action='store',
    )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    options = args()
    data = {
        "table": "sensor_wifi",
        "state": options.state == "on"
    }
    db_io.insert_record(data)
