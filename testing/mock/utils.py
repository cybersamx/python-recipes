# Dependencies implemented as a class

from random import randint


class Helper:
    def __init__(self, key: str):
        self.key = key

    def fetch_token(self) -> str:
        return f'{self.key}-{randint(0, 999):03d}'

    def fetch_product(self, product_id: str) -> str:
        return f'product {product_id}-{randint(0, 99):02d}'


# Dependencies implemented as functions
def fetch_token(key) -> str:
    return f'{key}-{randint(0, 999):03d}'


def fetch_product(product_id: str) -> str:
    return f'product {product_id}'
