#!/usr/bin/env python3

import os


def environ():
    # os.environ raises KeyError if PR_DB_URL isn't found.
    try:
        db_url = os.environ['PR_DB_URL']
        print('PR_DB_URL = %s', db_url)
    except KeyError:
        print('PR_DB_URL not found')


def environ_get():
    # os.environ.get() returns None if PR_DB_URL isn't found.
    db_url = os.environ.get('PR_DB_URL')
    if db_url is None:
        print('PR_DB_URL not found')
        return
    print('PR_DB_URL = %s', db_url)


def environ_get_default():
    # os.environ.get() can assign a default value if PR_DB_URL isn't found.
    db_url = os.environ.get('PR_DB_URL', 'postgres://user:passwd@pg/db')
    print('PR_DB_URL = %s', db_url)


def getenv():
    # os.getenv() == os.environ.get().
    db_url = os.getenv('PR_DB_URL', 'postgres://user:passwd@pg/db')
    print('PR_DB_URL = %s', db_url)


def main():
    environ()
    environ_get()
    environ_get_default()
    getenv()


if __name__ == '__main__':
    main()
