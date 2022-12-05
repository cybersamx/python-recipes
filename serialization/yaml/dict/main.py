import yaml


def yaml_to_dict():
    yaml_data = """
    debug: true
    connection_string: postgres://user:password@pg/db
    """
    dct = yaml.safe_load(yaml_data)  # Same as yaml.load(yaml_data, Loader=yaml.SafeLoader)
    print(dct)


def dict_to_yaml():
    dct = {'debug': True, 'connection_string': 'postgres://user:password@pg/db'}
    yaml_data = yaml.dump(dct)
    print(yaml_data)


def main():
    yaml_to_dict()
    dict_to_yaml()


if __name__ == '__main__':
    main()
