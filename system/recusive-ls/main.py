#!/usr/bin/env python3

import os.path
import pathlib


def ls(path: str):
    path = '.' if path == '' or path is None else path

    local_path = pathlib.Path(path)
    for f in local_path.iterdir():
        if f.is_dir() and f.name != '.':
            ls(os.path.join(local_path.name, f.name))

        cwd = f'.{os.sep}{f.name}' if local_path.name == '' else f'.{os.sep}{local_path.name}{os.sep}{f.name}'
        print(cwd)


def main():
    ls('.')


if __name__ == '__main__':
    main()
