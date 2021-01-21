HUE_URL: str # <hue_url>
USER: str # <url>

LIVING_ROOM = "living_room"
KITCHEN = "kitchen"
ROOMS = [LIVING_ROOM, KITCHEN]
ROOM_URL = {
    LIVING_ROOM: f"{HUE_URL}/api/{USER}/groups/1",
    KITCHEN: f"{HUE_URL}/api/{USER}/groups/2",
}
ROOM_BRIGHTNESS = {
    LIVING_ROOM: 0.8,
    KITCHEN: 1.0,
}
TRANSITION_TIME = 4

TEMP_URL = f"{HUE_URL}/api/{USER}/sensors/35"
