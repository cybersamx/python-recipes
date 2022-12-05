class Config(object):
    def __init__(self, debug, db_connections):
        self.debug = debug
        self.db_connections = db_connections

    def __repr__(self):
        return "%s(debug=%r, db_connections=%r)" % (self.__class__.__name__, self.debug, self.db_connections)


class DbConn(object):
    def __init__(self, db_type, username, password, host, db):
        self.db_type = db_type
        self.username = username
        self.password = password
        self.host = host
        self.db = db
