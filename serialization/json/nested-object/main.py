# Let's parse nested json string using object hook.
import json
from config import Config,DbConfig


def decoder(dct: dict) -> Config:
    if dct.get('username') is not None:
        return DbConfig(**dct)
    return Config(**dct)


def json_to_obj():
    json_data = '{"debug": true, "db_config": {"username": "pguser", "password": "pass", "host": "pg", "db": "db"}}'
    cfg = json.loads(json_data, object_hook=decoder)
    db_cfg = cfg.db_config
    print(cfg.debug, db_cfg.username, db_cfg.password, db_cfg.host, db_cfg.db)


def obj_to_json():
    cfg = Config(True, DbConfig('pguser', 'pass', 'pg', 'db'))
    cfg_dict = cfg.__dict__
    cfg_dict['db_config'] = cfg.db_config.__dict__
    json_data = json.dumps(cfg_dict)
    print(json_data)


def main():
    json_to_obj()
    obj_to_json()


if __name__ == '__main__':
    main()
