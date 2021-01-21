#!/usr/bin/python3

import sys, argparse
import requests
import config

def args():
    desc = "homeauto script"
    parser = argparse.ArgumentParser(
        description=desc,
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
        "token": config.TOKEN,
        "user": config.USER,
        "message": message,
    }

    # send data
    response = requests.post(
        url=config.URL,
        json=data,
    )
