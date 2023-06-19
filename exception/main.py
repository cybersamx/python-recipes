#!/usr/bin/env python


class WarningException(Exception):
    pass


class ErrorException(Exception):
    def __init__(self, status_code: int):
        self.status_code = status_code

    def __str__(self):
        return f'status_code={str(self.status_code)}'


class FatalException(Exception):
    pass


class PanicException(Exception):
    pass


class AppError(Exception):
    pass


for ex in [WarningException, ErrorException, FatalException, PanicException]:
    try:
        if ex is ErrorException:
            raise ex(status_code=500)

        raise ex()
    except WarningException as err:
        pass  # This exception is the exception :-)
    except ErrorException as err:
        print(f'Caught {err=}')
        raise AppError from err
    except (FatalException, PanicException) as err:  # To catch more than 1 exception.
        raise SystemExit(err)
    finally:
        # Final task to perform before closing out the try block.
        print('Done')
