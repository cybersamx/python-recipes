from config import Config, DbConfig


def json_to_obj():
    # Note that fields host and db are deliberately missing from the db_config field.
    json_data = '{"debug": true, "db_config": {"username": "pguser", "password": "pass"}}'
    cfg = Config.from_json(json_data)
    print(cfg.debug, cfg.db_config)


def obj_to_json():
    # Note that the fields host and db are deliberately missing from DbConfig. With skip_defaults = True,
    # fields in DbConfig with default values will be omitted from the dictionary return from `to_dict()`.
    cfg = Config(True, DbConfig('pguser', 'pass'))
    json_data = cfg.to_json()
    print(json_data)


def main():
    json_to_obj()
    obj_to_json()


if __name__ == '__main__':
    main()
