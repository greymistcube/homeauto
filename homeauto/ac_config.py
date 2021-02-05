import os, json

# setting up paths
MOD_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(MOD_PATH)
CRED_PATH = os.path.join(DIR_PATH, "ac_cred.json")

with open(CRED_PATH, "r") as file:
    cred = json.load(file)

ON_PATTERN = cred["on_pattern"]
OFF_PATTERN = cred["off_pattern"]

WAIT_TIME = 5
