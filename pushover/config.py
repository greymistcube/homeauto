import json

with open("config.json", "r") as file:
    cred = json.load(file)

URL = cred["url"]
TOKEN = cred["token"]
USER = cred["user"]
