import os

# setting up paths
MOD_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(MOD_PATH)

PUSHOVER = "pushover.py"
FLIRC = "flirc_util"

HOMEAUTO = os.path.join(DIR_PATH, "homeauto.py")
AC_IO = os.path.join(DIR_PATH, "ac_io.py")
POLL = os.path.join(DIR_PATH, "poll.py")
MODE = os.path.join(DIR_PATH, "mode.py")
WIFI = os.path.join(DIR_PATH, "wifi.py")
