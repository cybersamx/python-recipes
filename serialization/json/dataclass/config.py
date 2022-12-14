from dataclasses import dataclass


@dataclass
class DbConfig(object):
    username: str
    password: str
    host:     str = None  # Assign a default value to mark the host field in json optional
    db:       str = None  # Assign a default value to mark the host field in json optional


@dataclass
class Config(object):
    debug: bool
    db_config: DbConfig
