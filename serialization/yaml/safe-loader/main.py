import yaml
from config import Config, DbConn


def load_yaml(data, loader=yaml.Loader):
    # Define a custom loader so that we leave the global yaml.Loader.
    class Loader(loader):
        def config_constructor(self, node) -> Config:
            dct = self.construct_mapping(node)
            return Config(**dct)

    Loader.add_constructor('!Config', loader.config_constructor)

    return yaml.load(data, Loader=Loader)


def yaml_to_obj():
    # In yaml, we can tag a node using the ! notation. And through theis tagging, we can associate
    # the tag with a custom class.
    yaml_data = """
    !Config
    debug: true
    db_connections:
      - !DbConn
        db_type: postgres
        username: pguser
        password: password
        host: pg
        db: db
      - !DbConn
        db_type: mysql
        username: dbuser
        password: pwd
        host: localhost
        db: users
    """

    # A constructor is a handler that is used to convert a yaml node that's tagged with an associated tag
    # into a python custom object.
    # yaml.SafeLoader.add_constructor('!Config', constructor=config_constructor)
    # cfg = yaml.load(yaml_data, Loader=yaml.SafeLoader)
    cfg = load_yaml(yaml, yaml.SafeLoader)
    print(cfg)


def obj_to_yaml():
    cfg = Config(True, [
        DbConn('postgres', 'pguser', 'password', 'pg', 'db'),
    ])
    json_data = yaml.dump(cfg)
    print(json_data)


def main():
    yaml_to_obj()
    obj_to_yaml()


if __name__ == '__main__':
    main()
