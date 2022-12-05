import yaml


class Config(object):
    def __init__(self, debug, db_connections):
        self.debug = debug
        self.db_connections = db_connections

    def __repr__(self):
        return "%s(debug=%r, db_connections=%r)" % (self.__class__.__name__, self.debug, self.db_connections)


# Instead of using yaml.SafeLoader.add_constructor() to register a constructor and a tag to pyyaml, we can
# define a custom class that inherits yaml.YAMLObject. Pyyaml handles the construction of the custom object
# during deserialization using the associated tag and loader `yaml_tag` and `yaml_loader` respectively.
class DbConn(yaml.YAMLObject):
    yaml_tag = '!DbConn'
    yaml_loader = yaml.SafeLoader

    def __init__(self, db_type, username, password, host, db):
        self.db_type = db_type
        self.username = username
        self.password = password
        self.host = host
        self.db = db
