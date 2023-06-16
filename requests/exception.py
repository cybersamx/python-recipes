#!/usr/bin/env python

from requests import get
from requests.exceptions import (
    ConnectionError,
    ConnectTimeout,
    HTTPError,
    Timeout,
)

status_codes = [200, 400, 404, 502, 503]

for code in status_codes:
    try:
        res = get(f'https://httpstat.us/{code}')
        res.raise_for_status()
    except HTTPError as err:
        print(f'{type(err)}: {err=}')
        print(f'Status code: {err.response.status_code}')
    except (ConnectionError, ConnectTimeout, Timeout) as err:
        print('Retry')
    except Exception as err:
        raise SystemExit() from err
    finally:
        print('Done')
