import requests, json
import db_io, hue_config

# sensor functions
def get_light_state(room: str) -> bool:
    response = requests.get(url=hue_config.ROOM_URL[room])
    return json.loads(response.content)['state']['any_on']

def get_temp_state() -> float:
    response = requests.get(url=hue_config.TEMP_URL)
    return json.loads(response.content)['state']['temperature'] / 100

# control functions
def set_light_power(room: str, on: bool) -> requests.Response:
    data = {
        "table": f"controller_{room}",
        "state": on,
    }
    db_io.insert_record(record=data)
    url = hue_config.ROOM_URL[room]
    state = light_power_state(on, hue_config.ROOM_BRIGHTNESS[room])
    return action(url=url, state=state)

def set_light_color(
    room: str,
    hue: float,
    sat: float,
) -> requests.Response:
    data = {
        "table": f"controller_{room}",
        "state": [hue, sat],
    }
    db_io.insert_record(record=data)
    url = hue_config.ROOM_URL[room]
    state = light_color_state(hue, sat, hue_config.ROOM_BRIGHTNESS[room])
    return action(url=url, state=state)

# helper functions
def action(url: str, state: dict) -> requests.Response:
    return requests.put(
        url=f"{url}/action",
        json=state,
    )

def light_power_state(on: bool, bri: float) -> dict:
    return {
        "on": on,
        "bri": int(255 * bri),
        "transitiontime": hue_config.TRANSITION_TIME * 10,
    }

def light_color_state(hue: float, sat: float, bri: float) -> dict:
    return {
        "hue": int(65535 * hue),
        "sat": int(255 * sat),
        "bri": int(255 * bri),
        "transitiontime": hue_config.TRANSITION_TIME * 10,
    }
