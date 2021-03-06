#!/usr/bin/python3

import argparse, subprocess, time
import path, ac_config

def args() -> argparse.Namespace:
    desc = "ac control script"
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

def set_ac_state(power: bool) -> None:
    if power:
        pattern = ac_config.ON_PATTERN
    else:
        pattern = ac_config.OFF_PATTERN

    # requires flirc_util
    flirc_command = [
        path.FLIRC,
        "sendir",
        f"--pattern={pattern}",
    ]

    # run twice for robustness
    subprocess.run(flirc_command)
    time.sleep(ac_config.WAIT_TIME)
    subprocess.run(flirc_command)
    return

if __name__ == "__main__":
    options = args()
    set_ac_state(options.power == "on")
