#!/usr/bin/env python3

import calendar
from datetime import *
from dateutil.relativedelta import *
from dateutil.tz import *
import time

# Today's datetime
now = datetime.now(UTC)
print("Today's datetime")
print(now)
print(now.tzname())

# Defined datetime
# MST = UTC -7.0 hrs = UTC -7*3600 secs
mst = tzoffset("MST", -7*3600)
mountain = datetime(2006, 1, 2, 15, 4, 5, tzinfo=mst)
print("Timezone")
print(mountain)

# Converting to another timezone
pst = tzoffset("PST", -8*3600)
pacific = mountain.astimezone(pst)
print(pacific)

# Custom date format
# RFC822 - 02 Jan 06 15:04 -0700
print("Date formats")
print(mountain.strftime("%Y %b %d %H:%M %z"))
print(mountain.strftime("%Y%m%dT%H%M%SZ"))
date_str = "05/31/2023 22:59:40"
fmt = "%m/%d/%Y %H:%M:%S"
print(datetime.strptime(date_str, fmt))

# UNIX time to datetime
now_unix = time.time()
print("Epoch unix time")
print(now_unix)
now = datetime.fromtimestamp(now_unix, UTC)
print(now)
# Datetime to UNIX time
date_unix = time.mktime(mountain.timetuple())
print(date_unix)

# Arithmetic: datetime = datetime + delta
print("Date arithmetic")
tomorrow = now + relativedelta(days=1)
future = now + relativedelta(months=1, weeks=3)
print(tomorrow)
print(future)
# Arithmetic: delta = datetime - datetime
delta = relativedelta(datetime(2010, 12, 25, 10, 45), datetime(2010, 11, 30, 7, 15))
print(delta)
# Arithmetic: delta = delta + delta
delta = delta + relativedelta(months=2)
print(delta)

# Advanced setting
# Next Thursday
print("Advanced")
next_thu = now + relativedelta(weekday=calendar.FRIDAY)
print(next_thu)
# The last Saturday of the current month. Note: it's day=, not days=
last_sat = now + relativedelta(day=31, weekday=calendar.SATURDAY)
print(last_sat)
