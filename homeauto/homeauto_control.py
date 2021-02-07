import subprocess, datetime, random
import path, homeauto_config, homeauto_state
import db_io, hue_io

def light_power(group: str, power: bool) -> None:
    """
    Turns light on and off.
    """
    data = {
        "table": f"control_{group}",
        "state": power,
    }
    db_io.insert_record(data)
    hue_io.set_group_power(group, power)

    # when turning off, set mode to auto
    if group == "living_room" and not power:
        subprocess.run([path.MODE, "auto"])
    return

def light_color(group: str) -> None:
    """
    Update light color.
    """
    if group == "living_room":
        mode = homeauto_state.mode()
        if mode == "auto":
            color = _get_group_color(group)
            data = {
                "table": f"control_{group}",
                "state": [color["hue"], color["sat"]],
            }
            db_io.insert_record(data)
            hue_io.set_group_color(group, color["hue"], color["sat"])
        else:
            lights = hue_io.get_group_lights(group)
            colors = homeauto_config.MODE_COLORS[mode]
            for light in lights:
                color = random.choice(colors)
                hue_io.set_light_color(light, color["hue"], color["sat"])
    elif group == "kitchen":
        color = _get_group_color(group)
        data = {
            "table": f"control_{group}",
            "state": [color["hue"], color["sat"]],
        }
        db_io.insert_record(data)
        hue_io.set_group_color(group, color["hue"], color["sat"])
    else:
        raise ValueError(f"invalid value for group: {group}")
    return

def ac_power(power: bool) -> None:
    """
    Turns ac on and off.
    """
    data = {
        "table": "control_ac",
        "state": power,
    }
    db_io.insert_record(data)
    if power:
        subprocess.Popen([path.AC_IO, "on"])
    else:
        subprocess.Popen([path.AC_IO, "off"])
    return

def _get_group_color(group: str) -> dict:
    if group == "living_room":
        hour = datetime.datetime.now().hour
        color = _get_hour_to_group_color(hour)
        return color
    elif group == "kitchen":
        return homeauto_config.GROUP_COLOR["pure"]
    else:
        raise ValueError(f"invalid value for group: {group}")

def _get_hour_to_group_color(hour: int) -> dict:
    if 2 <= hour and hour < 10:
        return homeauto_config.GROUP_COLOR["warm"]
    elif 10 <= hour and hour < 20:
        return homeauto_config.GROUP_COLOR["ghost"]
    else:
        return homeauto_config.GROUP_COLOR["candle"]
