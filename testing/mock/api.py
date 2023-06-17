# Basically the logic is:
# get_product calls 2 functions: fetch_token, fetch_product

import utils


def get_product_depends_on_class(key: str, product_id: str) -> dict:
    helper = utils.Helper(key)

    token = helper.fetch_token()
    product = helper.fetch_product(product_id)

    return {'product': product, 'token': f'token-{token}'}


def get_product_depends_on_func(key: str, product_id: str) -> dict:
    token = utils.fetch_token(key)
    product = utils.fetch_product(product_id)

    return {'product': product, 'token': f'token-{token}'}
