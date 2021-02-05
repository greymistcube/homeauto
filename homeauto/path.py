import os

# setting up paths
MOD_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(MOD_PATH)

PUSHOVER = os.path.join("pushover.py")
AC_IO = os.path.join(DIR_PATH, "ac_io.py")
