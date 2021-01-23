#!/usr/bin/python3

import os, subprocess, time
import config

ssh_exec = "ssh"
ssh_comm = [
    ssh_exec,
    "-i", f"{config.KEY_PATH}",
    "-N",
    "-R", f"{config.REMOTE_PORT}:localhost:{config.LOCAL_PORT}",
    f"{config.USER}@{config.REMOTE}",
]

pushover_exec = "pushover.py"
pushover_msg = f"ssh connection to {config.REMOTE} has been dropped"
pushover_comm = [
    pushover_exec,
    pushover_msg,
]

if __name__ == "__main__":
    # since this is a boot script
    # wait for other services to load just in case
    time.sleep(config.BOOT_WAIT_TIME)

    while True:
        # make an attempt to connect
        start = time.time()
        subprocess.run(ssh_comm)
        end = time.time()

        # if an attempt lasted longer than 10 minutes
        # we assume there was a successful session
        # and then the connection dropped for whatever reason
        if end - start > config.MIN_SESSION_LENGTH:
            subprocess.run(pushover_comm)

        # wait before making another attempt
        time.sleep(config.RECONNECT_WAIT_TIME)
