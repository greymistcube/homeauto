import json

with open("cred.json", "r") as file:
    cred = json.load(file)

URL = cred["url"]
TOKEN = cred["token"]
USER = cred["user"]
