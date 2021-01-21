#!/usr/bin/python3

import os, shutil, sqlite3
import db_config, db_io

# setting up paths
MOD_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(MOD_PATH)
DB_DIR = os.path.join(DIR_PATH, db_config.DB_DIR)
DB_PATH = os.path.join(DB_DIR, db_config.DB_FILE)

TEMPLATE = """
CREATE TABLE {} (
    state {},
    timestamp REAL
);
"""

CREATE_TABLE_COMMANDS = [
    TEMPLATE.format(table, "TEXT") for table in db_config.TABLES
]

if __name__ == "__main__":
    # remove old db
    try:
        shutil.rmtree(DB_DIR)
    except:
        pass

    # create a new db with right permissions
    os.mkdir(DB_DIR)

    conn = sqlite3.connect(DB_PATH)
    for command in CREATE_TABLE_COMMANDS:
        try:
            conn.execute(command)
        except:
            pass
    conn.commit()
    conn.close()

    # initialize records
    db_io.insert_record({
        "table": "control_ac",
        "state": False,
    })
    db_io.insert_record({
        "table": "sensor_wifi",
        "state": False,
    })

    os.chmod(DB_DIR, 0o0777)
    os.chmod(DB_PATH, 0o0666)
