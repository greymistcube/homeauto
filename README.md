# Home Automation

[![python][python_img]][python_url]
[![requests][requests_img]][requests_url]

Just a small personal project for home automation.

## Description

Other than actually producing something useful, the intent of the project
was to build something from scratch. This is not really a long term solution,
and once the system complexity starts to grow, migrating to
an open source third party solution such as [Home Assistant](home_assistant)
may be needed in the near future.

## Features

The main goal is to implement the following features:

* automatic lighting
* automatic air conditioning

To support the main features listed above, the following supporting
features must also be implemented:

* detect user presence
* monitor temperature

## Overview

![homeauto_system][homeauto_system]

## Components

See each accompanied component document for more details.

* [tunnel](./tunnel/README.md)
* [pushover](./pushover/README.md)
* [homeauto](./homeauto/README.md)

All sensative pieces of information, mostly stored in config files,
are removed from the repository.

### Tunnel

This is used to funnel traffic to `cloud_server` to `home_server`.
As `home_server` is without a fixed address, this is so that
`cloud_server` can be used as an api gateway to `home_server`

### Pushover

This is used to push a notification to a phone if something goes wrong.
As there are many moving parts, this is used as a crude monitering
on system health.

### Homeauto

Collection of executable scripts for the entire system.
Handles database management, core logic, and control of appliances.

[homeauto_system]: ./docs/static/homeauto_system.png
[python_img]: https://img.shields.io/badge/python-3.7-blue.svg
[python_url]: https://www.python.org/
[requests_img]: https://img.shields.io/badge/requests-2.21-brightgreen.svg
[requests_url]: https://requests.readthedocs.io/en/master/
[home_assistant]: https://www.home-assistant.io/
