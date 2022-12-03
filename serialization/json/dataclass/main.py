from config import Config, DbConfig
from dataclasses import asdict
import jsons


def json_to_obj():
    # Note that fields host and db are deliberately missing from the db_config field.
    json_data = '{"debug": true, "db_config": {"username": "pguser", "password": "pass"}}'
    cfg = jsons.loads(json_data, Config)
    print(cfg.debug, cfg.db_config)


def obj_to_json():
    cfg = Config(True, DbConfig('pguser', 'pass', 'pg', 'db'))
    json_data = jsons.dumps(asdict(cfg))
    print(json_data)


def main():
    json_to_obj()
    obj_to_json()


if __name__ == '__main__':
    main()
