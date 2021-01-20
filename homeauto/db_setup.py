#!/usr/bin/python3

import os, sqlite3
from db_config import DB_NAME, TABLES

# setting up paths
MOD_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(MOD_PATH)
DB_PATH = os.path.join(DIR_PATH, DB_NAME)

TEMPLATE = """
CREATE TABLE {} (
    state {},
    timestamp REAL
);
"""

CREATE_TABLE_COMMANDS = [TEMPLATE.format(table, "TEXT") for table in TABLES]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    for command in CREATE_TABLE_COMMANDS:
        try:
            conn.execute(command)
        except:
            pass
    conn.commit()
    conn.close()
