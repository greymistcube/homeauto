# Pushover

A simple script to push a message to a [Pushover][pushover] service.

## Description

A simple way to send a notification to a phone if anything goes wrong.
Simply sends a string message given as an argument to the script.

## Usage

Files are deployed to

```sh
$HOME/bin/pushover/
```

directory of `pushover` user on `local_server` with a symbolic link

```sh
$HOME/bin/pushover.py -> $HOME/bin/pushover/pushover.py
```

for easy access.

To enable global usage, an additional symbolic link

```sh
/usr/local/bin/pushover.py -> $HOME/bin/pushover.py
```

is also created.

[pushover]: https://pushover.net/
