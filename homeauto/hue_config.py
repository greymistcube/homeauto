import os, json

# setting up paths
MOD_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(MOD_PATH)
CRED_PATH = os.path.join(DIR_PATH, "hue_cred.json")

with open(CRED_PATH, "r") as file:
    cred = json.load(file)

URL = cred["url"]
USER = cred["user"]

LIVING_ROOM = "living_room"
KITCHEN = "kitchen"
GROUPS = [LIVING_ROOM, KITCHEN]
GROUP_URL = {
    LIVING_ROOM: f"{URL}/api/{USER}/groups/1",
    KITCHEN: f"{URL}/api/{USER}/groups/2",
}
GROUP_BRIGHTNESS = {
    LIVING_ROOM: 0.8,
    KITCHEN: 1.0,
}
TRANSITION_TIME = 4

TEMP_URL = f"{URL}/api/{USER}/sensors/35"
