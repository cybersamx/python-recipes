# Creating Calendar in SQLite

One of the most common data operations is the generation of a calendar in organization's database for grouping dates in analytics that are used in different application contexts from calculating daily revenue to determining shipments made per week.

## Fiscal Calendar

This example shows how we populate a SQLite table with the relevant calendar data. We are calculating the date range for the regular calendar in this example, but we can modify the logic to calculate a custom fiscal calendar.

Also, there's a package called `fiscalyear` that you can use for the generation of a fiscal calendar.

## Setup

1. Install the packages.

   ```bash
   $ pip install -r requirements.txt
   ```

1. Run the program, which will create a sqlite file.

   ```bash
   $ rm test.sqlite
   $ ./main.py
   ```

