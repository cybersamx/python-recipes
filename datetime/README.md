# Datetime

## Datetime

Common string directives for `strftime()` and `strptime()`.

| Directive | Meaning                | Example             |
|-----------|------------------------|---------------------|
| %a        | Abbreviated weekday    | Sun, Mon,...        |
| %d        | Day of month           | 01, 02,... , 31     |
| %m        | Month number           | 01, 02,... , 12     |
| %b        | Abbreviated month name | Jan, Feb,... , Dec  |
| %y        | 2-digit year           | 00, 01,... , 99     |
| %Y        | 4-digit year           | ..., 2000, 2001,... |
| %H        | 24-hr Hour             | 00, 01,... , 23     |
| %I        | 12-hr Hour             | 01, 02,... , 12     |
| %M        | Minute                 | 00, 01,... , 59     |
| %S        | Second                 | 00, 01,... , 59     |
| %z        | UTC offset             | +0000, +0400,...    |

## Dateutil

Datetime arithmetic can be accomplished by using the standard `timedelta` class.

```python
from datetime import datetime, timedelta, timezone
date = datetime.now(timezone.utc)
tomorrow = date + timedelta(days=1)
```

But `dateutil` provides some useful datetime utilities. If you need support for more complex arithmetic and timezone conversion, use `dateutil`.

```python
from datetime import *
from dateutil.relativedelta import *
from dateutil.tz import *
date = datetime.now(UTC)
tomorrow = date + relativedelta(days=1)
```

## Setup

1. Install packages and run.

   ```bash
   $ pip install -r requirements.txt
   $ ./main.py
   ```

## Reference

* [Python strftime format specifiers](https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior)
* [Github: dateutil](https://github.com/dateutil/dateutil)
