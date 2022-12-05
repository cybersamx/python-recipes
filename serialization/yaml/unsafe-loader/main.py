import yaml
from config import Config, DbConn


def yaml_to_obj():
    # In yaml, we can tag a node using the ! notation. And through theis tagging, we can associate
    # the tag with a custom class. The !!python/object:* are specific yaml tags associated with python.
    # The postgres connection being tagged, will be deserialized to a DbConn object.
    # The mysql connection not being tagged, will be deserialized to a dict.
    yaml_data = """
    !!python/object:config.Config
    debug: true
    db_connections:
      - !!python/object:config.DbConn
        db_type: postgres
        username: pguser
        password: password
        host: pg
        db: db
      - db_type: mysql
        username: dbuser
        password: pwd
        host: localhost
        db: users
    """

    # UnsafeLoader allows us to deserialize to a custom object just with a special python tag.
    cfg = yaml.load(yaml_data, Loader=yaml.UnsafeLoader)
    print(cfg)


def main():
    yaml_to_obj()


if __name__ == '__main__':
    main()
