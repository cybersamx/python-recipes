class DbConfig(object):
    def __init__(self, username, password, host, db):
        self.username = username
        self.password = password
        self.host = host
        self.db = db


class Config(object):
    def __init__(self, debug, db_config):
        self.debug = debug
        self.db_config = db_config
