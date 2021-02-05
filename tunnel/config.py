import json

with open("cred.json", "r") as file:
    cred = json.load(file)

REMOTE = cred["remote"]
USER = cred["user"]
KEY = cred["key"]
REMOTE_PORT = cred["remote_port"]
LOCAL_PORT = cred["local_port"]

# wait times
BOOT_WAIT_TIME = 60
RECONNECT_WAIT_TIME = 60
MIN_SESSION_LENGTH = 600
