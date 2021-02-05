import json

with open("ac_cred.json", "r") as file:
    cred = json.load(file)

ON_PATTERN = cred["on_pattern"]
OFF_PATTERN = cred["off_pattern"]

WAIT_TIME = 5
