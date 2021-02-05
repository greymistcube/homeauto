import subprocess, datetime
import path, homeauto_config, homeauto_state
import hue_io

def light_power(room: str, power: bool) -> None:
    """
    Turns light on and off.
    """
    hue_io.set_group_power(room, power)
    return

def light_color(room: str) -> None:
    """
    Adjust light color.
    """
    if room == "living_room":
        color = _get_group_color(room)
        hue_io.set_group_color(room, color["hue"], color["sat"])
    elif room == "kitchen":
        color = _get_group_color(room)
        hue_io.set_group_color(room, color["hue"], color["sat"])
    else:
        raise ValueError(f"invalid value for room: {room}")
    return

def ac_power(power: bool) -> None:
    """
    Turns ac on and off.
    """
    if power:
        subprocess.Popen([path.AC_IO, "on"])
    else:
        subprocess.Popen([path.AC_IO, "off"])
    return

def _get_group_color(room: str) -> dict:
    if room == "living_room":
        hour = datetime.datetime.now().hour
        color = _get_hour_to_group_color(hour)
        return color
    elif room == "kitchen":
        return homeauto_config.GROUP_COLOR["pure"]
    else:
        raise ValueError(f"invalid value for room: {room}")

def _get_hour_to_group_color(hour: int) -> dict:
    if 2 <= hour and hour < 10:
        return homeauto_config.GROUP_COLOR["warm"]
    elif 10 <= hour and hour < 20:
        return homeauto_config.GROUP_COLOR["ghost"]
    else:
        return homeauto_config.GROUP_COLOR["candle"]
