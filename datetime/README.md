# Datetime

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
