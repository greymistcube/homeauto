import json

with open("hue_cred.json", "r") as file:
    cred = json.load(file)

URL = cred["url"]
USER = cred["user"]

LIVING_ROOM = "living_room"
KITCHEN = "kitchen"
ROOMS = [LIVING_ROOM, KITCHEN]
ROOM_URL = {
    LIVING_ROOM: f"{URL}/api/{USER}/groups/1",
    KITCHEN: f"{URL}/api/{USER}/groups/2",
}
ROOM_BRIGHTNESS = {
    LIVING_ROOM: 0.8,
    KITCHEN: 1.0,
}
TRANSITION_TIME = 4

TEMP_URL = f"{URL}/api/{USER}/sensors/35"
