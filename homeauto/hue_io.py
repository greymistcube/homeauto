import requests
import hue_config

# sensor functions
def get_group_power(group: str) -> bool:
    response = requests.get(url=hue_config.GROUP_URL[group])
    return response.json()["state"]["any_on"]

def get_group_lights(group: str) -> list:
    response = requests.get(url=hue_config.GROUP_URL[group])
    return response.json()["lights"]

def get_temp_state() -> float:
    response = requests.get(url=hue_config.TEMP_URL)
    return response.json()["state"]["temperature"] / 100

# control functions
def set_group_power(group: str, power: bool) -> requests.Response:
    group_url = hue_config.GROUP_URL[group]
    state = group_power_state(power, hue_config.GROUP_BRIGHTNESS[group])
    return set_group_state(group_url=group_url, state=state)

def set_group_color(group: str, hue: float, sat: float) -> requests.Response:
    group_url = hue_config.GROUP_URL[group]
    state = group_color_state(hue, sat, hue_config.GROUP_BRIGHTNESS[group])
    return set_group_state(group_url=group_url, state=state)

def set_light_power(light: str, power: bool) -> requests.Response:
    light_url = f"{hue_config.URL}/api/{hue_config.USER}/lights/{light}"
    state = light_power_state(power)
    return set_light_state(light_url=light_url, state=state)

def set_light_color(light: str, hue: float, sat: float) -> requests.Response:
    light_url = f"{hue_config.URL}/api/{hue_config.USER}/lights/{light}"
    state = light_color_state(hue, sat)
    return set_light_state(light_url=light_url, state=state)

# helper functions
def set_group_state(group_url: str, state: dict) -> requests.Response:
    return requests.put(
        url=f"{group_url}/action",
        json=state,
    )

def set_light_state(light_url: str, state: dict) -> requests.Response:
    return requests.put(
        url=f"{light_url}/state",
        json=state,
    )

# state generators
def group_power_state(on: bool, bri: float) -> dict:
    return {
        "on": on,
        "bri": int(255 * bri),
    }

def group_color_state(hue: float, sat: float, bri: float) -> dict:
    return {
        "hue": int(65535 * hue),
        "sat": int(255 * sat),
        "bri": int(255 * bri),
        "transitiontime": hue_config.TRANSITION_TIME * 10,
    }

def light_power_state(on: bool) -> dict:
    return {
        "on": on,
    }

def light_color_state(hue: float, sat: float) -> dict:
    return {
        "hue": int(65535 * hue),
        "sat": int(255 * sat),
        "transitiontime": hue_config.TRANSITION_TIME * 10,
    }
