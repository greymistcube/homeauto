#!/usr/bin/python3

import sys, argparse
import requests
from config import TOKEN, USER, URL

def args():
    desc = "homeauto script"
    parser = argparse.ArgumentParser(
        description=desc,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "message",
        help="message to push",
        type=str,
        action='store',
    )
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    options = args()
    message = options.message

    # prepare data
    data = {
        "token": TOKEN,
        "user": USER,
        "message": message,
    }

    # send data
    response = requests.post(
        url=URL,
        json=data,
    )
