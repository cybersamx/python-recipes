from dataclasses import dataclass


@dataclass
class DbConfig(object):
    username: str
    password: str
    host:     str = None  # Marks the host attribute as optional
    db:       str = None  # Marks the db attribute as optional


@dataclass
class Config(object):
    debug: bool
    db_config: DbConfig
