#!/usr/bin/env python

import os
from dotenv import load_dotenv


def environ():
    # os.environ raises KeyError if PR_DB_URL isn't found.
    try:
        db_url = os.environ['PR_DB_URL']
        print(f'PR_DB_URL {db_url}')
    except KeyError:
        print('PR_DB_URL not found')


def environ_get():
    # os.environ.get() returns None if PR_DB_URL isn't found.
    db_url = os.environ.get('PR_DB_URL')
    if db_url is None:
        print('PR_DB_URL not found')
        return
    print(f'PR_DB_URL {db_url}')


def environ_get_default():
    # os.environ.get() can assign a default value if PR_DB_URL isn't found.
    db_url = os.environ.get('PR_DB_URL', 'postgres://user:passwd@pg/db')
    print(f'PR_DB_URL = {db_url}')


def getenv():
    # os.getenv() == os.environ.get().
    db_url = os.getenv('PR_DB_URL', 'postgres://user:passwd@pg/db')
    print(f'PR_DB_URL = {db_url}')


def dotenv():
    load_dotenv('.env.production')

    db_url = os.getenv('PR_DB_URL', 'postgres://user:passwd@pg/db')
    print(f'PR_DB_URL = {db_url}')


def main():
    environ()
    environ_get()
    environ_get_default()
    getenv()
    dotenv()


if __name__ == '__main__':
    main()
