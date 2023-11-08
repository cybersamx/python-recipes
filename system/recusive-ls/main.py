#!/usr/bin/env python3

import os.path
import pathlib


def ls(path: str):
    path = '.' if path == '' or path is None else path

    local_path = pathlib.Path(path)
    for f in local_path.iterdir():
        if f.is_dir():
            ls(os.path.join(path, f.name))

        cwd = f'.{os.sep}{f}'
        print(cwd)


def main():
    ls('folder-a')


if __name__ == '__main__':
    main()
