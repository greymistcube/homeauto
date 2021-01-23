# Tunnel

A simple script to automatically establish an `ssh` tunnel connection
to `cloud_server`.

## Description

This script is used to establish a persistant `ssh` tunnel connection
to `cloud_server`.

The script is run on boot, which issues an `ssh` command,
binding a remote port to a local port. The script runs indefinitely.
If the connection is dropped, a notification is pushed through `pushover.py`
script, and repeated attempts are made to reestablish a connection henceforth.

## Usage

Files `tunnel.py` and `config.py` are deployed to

```sh
$HOME/bin/tunnel/
```

directory of `tunnel` user on `local_server` with a symbolic link

```sh
$HOME/bin/tunnel.py -> $HOME/bin/tunnel/tunnel.py
```

for easy access.

Finally, in order to run at boot time, the following is added to the `crontab`
of the user. Additionally, to have access to other global custom scripts,
`/usr/local/bin` is also set to path.


```
PATH=/usr/bin:/bin:/usr/local/bin
@reboot $HOME/bin/tunnel.py
```
