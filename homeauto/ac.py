#!/usr/bin/python3

import argparse, subprocess, time
import ac_config, db_io

# requires flirc_util
flirc_exec = "flirc_util"

def args() -> argparse.Namespace:
    desc = "ac controller script"
    parser = argparse.ArgumentParser(
        description=desc,
    )
    parser.add_argument(
        "power",
        help="power state to send to ac",
        type=str,
        choices=["on", "off"],
        action='store',
    )
    args = parser.parse_args()
    return args

def ac_control(power: bool) -> None:
    # record to db
    data = {
        "table": "controller_ac",
        "state": power,
    }
    db_io.insert_record(data)

    if power:
        pattern = ac_config.ON_SIGNAL
    else:
        pattern = ac_config.OFF_SIGNAL
    flirc_comm = [
        flirc_exec,
        "sendir",
        f"--pattern={pattern}",
    ]
    # run twice for robustness
    subprocess.run(flirc_comm)
    time.sleep(ac_config.WAIT_TIME)
    subprocess.run(flirc_comm)
    return

if __name__ == "__main__":
    options = args()
    ac_control(options.power == "on")
