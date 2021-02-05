import subprocess, datetime
import path, homeauto_config, homeauto_state
import hue_io

def light_power(room: str, power: bool) -> None:
    """
    Turns light on and off.
    """
    hue_io.set_light_power(room, power)
    return

def light_color(room: str) -> None:
    """
    Adjust light color.
    """
    color = get_light_color(room)
    hue_io.set_light_color(room, color["hue"], color["sat"])
    return

def ac_power(power: bool) -> None:
    if power:
        subprocess.Popen([path.AC_IO, "on"])
    else:
        subprocess.Popen([path.AC_IO, "off"])
    return

def get_light_color(room: str) -> dict:
    if room == "living_room":
        hour = datetime.datetime.now().hour
        color = get_hour_to_light_color(hour)
        return color
    else:
        return homeauto_config.COLOR["pure"]

def get_hour_to_light_color(hour: int):
    if 2 <= hour and hour < 10:
        return homeauto_config.COLOR["warm"]
    elif 10 <= hour and hour < 20:
        return homeauto_config.COLOR["ghost"]
    else:
        return homeauto_config.COLOR["candle"]
