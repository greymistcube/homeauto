#!/usr/bin/python3

import os, subprocess, time
from config import REMOTE, USER, KEY_PATH, REMOTE_PORT, LOCAL_PORT

# wait times
BOOT_WAIT_TIME = 60
RECONNECT_WAIT_TIME = 60

ssh_bin = "/usr/bin/ssh"
ssh_args = [
    ssh_bin,
    "-i", f"{KEY_PATH}",
    "-N",
    "-R", f"{REMOTE_PORT}:localhost:{LOCAL_PORT}",
    f"{USER}@{REMOTE}",
]

pushover_bin = "/usr/bin/pushover.py"
pushover_msg = f"ssh connection to {REMOTE} has been dropped"
pushover_args = [
    pushover_bin,
    pushover_msg,
]

if __name__ == "__main__":
    # since this is a boot script
    # wait for other services to load just in case
    time.sleep(BOOT_WAIT_TIME)

    while True:
        # make an attempt to connect
        start = time.time()
        subprocess.run(ssh_args)
        end = time.time()

        # if an attempt lasted longer than 10 minutes
        # we assume there was a successful session
        # and then the connection dropped for whatever reason
        if end - start > 600:
            subprocess.run(pushover_args)

        # wait before making another attempt
        time.sleep(RECONNECT_WAIT_TIME)
