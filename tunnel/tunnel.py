#!/usr/bin/python3

import os, subprocess, time
import config

if __name__ == "__main__":
    ssh_command = [
        "ssh",
        "-i", f"{config.KEY}",
        "-N",
        "-R", f"{config.REMOTE_PORT}:localhost:{config.LOCAL_PORT}",
        f"{config.USER}@{config.REMOTE}",
    ]

    pushover_command = [
        "pushover.py",
        f"ssh connection to {config.REMOTE} has been dropped",
    ]

    # since this is a boot script
    # wait for other services to load just in case
    time.sleep(config.BOOT_WAIT_TIME)

    while True:
        # make an attempt to connect
        start = time.time()
        subprocess.run(ssh_command)
        end = time.time()

        # if an attempt lasted longer than 10 minutes
        # we assume there was a successful session
        # and then the connection dropped for whatever reason
        if end - start > config.MIN_SESSION_LENGTH:
            subprocess.run(pushover_command)

        # wait before making another attempt
        time.sleep(config.RECONNECT_WAIT_TIME)
