#!/usr/bin/env python3

import sqlite3
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta


def create_table(con):
    create_table_stmt = '''
    CREATE TABLE IF NOT EXISTS calendar (
        id      INTEGER PRIMARY KEY,
        date    DATETIME NOT NULL,
        weekday TINYINT,
        month   SMALLINT,
        week    SMALLINT,
        day     SMALLINT
    )
    '''
    cursor = con.cursor()
    cursor.execute(create_table_stmt)
    con.commit()
    cursor.close()


def populate_table(con, year):
    insert_stmt = '''
    INSERT INTO calendar (
        date,
        weekday,
        month,
        week,
        day
    ) VALUES (
        ?, ?, ?, ?, ?
    )
    '''

    # Start the year from 1/1.
    date = datetime(year, 1, 1, tzinfo=timezone.utc)
    week = 1
    month = 1
    day = 1
    cursor = con.cursor()
    for i in range(0, 365):
        if date.month > month:
            month += 1
        if day > 1 and date.weekday() == 6:
            # Increment week if it's a Sunday (6).
            week += 1
        weekday = date.weekday()
        cursor.execute(insert_stmt, (date, weekday, month, week, day))
        con.commit()
        # print(date.astimezone(timezone.utc), weekday, month, week, day)
        date += relativedelta(days=1)
        day += 1
    cursor.close()


def query_table(con):
    select_stmt = '''
    SELECT id, date, weekday, month, week, day
    FROM calendar
    '''

    cursor = con.cursor()
    cursor.execute(select_stmt)
    for row in cursor.fetchall():
        print(row)
    cursor.close()


def main():
    try:
        con = sqlite3.connect('test.sqlite')
        create_table(con)
        populate_table(con, 2022)
        query_table(con)
    except sqlite3.Error as error:
        print(error)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    main()
