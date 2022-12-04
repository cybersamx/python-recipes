import json


def json_to_dict():
    json_data = '{"debug": true, "connection_string": "postgres://user:password@pg/db"}'
    dct = json.loads(json_data)
    print(dct)


def dict_to_json():
    dct = {'debug': True, 'connection_string': 'postgres://user:password@pg/db'}
    json_data = json.dumps(dct)
    print(json_data)


def main():
    json_to_dict()
    dict_to_json()


if __name__ == '__main__':
    main()
