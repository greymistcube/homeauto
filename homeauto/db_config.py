DB_DIR = "db/"
DB_FILE = "homeauto.db"
TABLES = [
    "sensor_temp", "sensor_wifi", "sensor_living_room", "sensor_kitchen",
    "sensor_mode", "control_living_room", "control_kitchen", "control_ac",
]
TRIGGERS = [
    "sensor_temp", "sensor_wifi", "sensor_living_room", "sensor_kitchen",
]
# one week in seconds
TIMEFRAME = 3600 * 24 * 7
