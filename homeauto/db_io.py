import sys, os, sqlite3, datetime, subprocess
import db_config

# setting up paths
MOD_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(MOD_PATH)
DB_DIR = os.path.join(DIR_PATH, db_config.DB_DIR)
DB_PATH = os.path.join(DB_DIR, db_config.DB_FILE)

def tables() -> list:
    conn = sqlite3.connect(DB_PATH)
    tables = conn.execute(f"""
    SELECT name FROM sqlite_master;
    """).fetchall()
    conn.commit()
    conn.close()

    tables = [table[0] for table in tables]
    return tables

def latest_records(table: str) -> list:
    conn = sqlite3.connect(DB_PATH)
    limit = timestamp() - db_config.TIMEFRAME
    records = conn.execute(f"""
    SELECT * FROM {table}
    WHERE timestamp > {limit}
    ORDER BY timestamp DESC;
    """).fetchall()
    conn.commit()
    conn.close()

    return records

def insert_record(record: dict) -> None:
    conn = sqlite3.connect(DB_PATH)
    table = record["table"]
    values = (str(record["state"]), timestamp())
    conn.execute(f"""
    INSERT INTO {table} VALUES (?, ?);
    """, values)
    conn.commit()
    conn.close()

    homeauto_exec = os.path.join(DIR_PATH, "homeauto.py")
    homeauto_comm = [homeauto_exec, table]
    subprocess.run(homeauto_comm)
    return

def timestamp() -> float:
    return datetime.datetime.now().timestamp()
