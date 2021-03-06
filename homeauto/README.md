# Homeauto

The main module for the project. Implements logic, database handling,
and appliance controls.

## Description

Sensor logs and and control logs are automatically gathered and
put into a database. Whenever the database is updated, this triggers
the main logic script `homeauto.py` which determines the actions to follow.

There are two types of "sensors", passive and active.
Information from passive sensors are polled by a script named `poll.py`,
which runs every `5` minutes. Information from active sensors are logged by
the sensors triggering a script, one of which is `wifi.py`.

The rest are either wrapper libraries or config files.

## Usage

All files are deployed to

```sh
$HOME/bin/homeauto/
```

directory of `homeauto` user on `local_server` with symbolic links
for executables inside

```sh
$HOME/bin/
```

pointing to appropriate files.

Note that `db_setup.py` must be run once to initialize the database
before usage.

Finally, for automated script executions, the following
is added to the `crontab` of the user. Additionally, to have access
to other global custom scripts, `/usr/local/bin` is also set to path.

```
PATH=/usr/bin:/bin:/usr/local/bin
*/5 * * * * $HOME/bin/poll.py
0 0 * * * $HOME/bin/db_prune.py
```
