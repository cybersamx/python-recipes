import os
from dataclasses import dataclass


@dataclass
class Result:
    id: str
    name: str
    quantity: int


def connect_api() -> Result | None:
    # Depends on api key and secret to connect to api.
    access_key = os.getenv('PR_ACCESS_KEY')
    secret_key = os.getenv('PR_SECRET_KEY')

    # Make the call and return a dummy result.
    if access_key == 'dummy-access-key' and secret_key == 'dummy-secret-key':
        return Result(id='1234', name='bag', quantity=3)

    return None
