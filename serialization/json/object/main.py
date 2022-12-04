import json
from config import Config


def decoder(dct):
    return Config(**dct)


def json_to_obj():
    json_data = '{"debug": true, "connection_string": "postgres://user:password@pg/db"}'
    # object_hook is a handler that can be used to convert a dict of parsed json values
    # into a python custom object.
    cfg = json.loads(json_data, object_hook=decoder)
    print(cfg.debug, cfg.connection_string)


def obj_to_json():
    cfg = Config(True, 'postgres://user:password@pg/db')
    json_data = json.dumps(cfg.__dict__)
    print(json_data)


def main():
    json_to_obj()
    obj_to_json()


if __name__ == '__main__':
    main()
