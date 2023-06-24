#!/usr/bin/env python

from config import Config, DbConfig
from datetime import datetime


json_data = '''\
{\
    "debug": true,\
    "scheduledShutdown": "2023-06-17T16:45:00-00:00",\
    "createdAt": "2023-06-15T13:30:00-00:00",\
    "dbConfig": {\
        "username": "pguser",\
        "password": "pass"\
    }\
}\
'''


def json_to_obj():
    cfg = Config.from_json(json_data)
    print(cfg.debug, cfg.db_config, cfg.scheduled_shutdown, cfg.scheduled_boot)


def obj_to_json():
    cfg = Config(
        True,
        DbConfig('pguser', 'pass', 'pg', 'db'),
        scheduled_boot=datetime(2023, 5, 4, 16, 0, 0),
        created_at=datetime(2022, 6, 15, 4, 0, 0),
    )
    json_output = cfg.to_json(indent=4)
    print(json_output)


def main():
    json_to_obj()
    obj_to_json()


if __name__ == '__main__':
    main()
