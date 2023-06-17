#!/usr/bin/env python -m unittest

import unittest
from unittest.mock import patch, Mock, MagicMock

import api
import utils


class TestApi(unittest.TestCase):
    @patch.object(utils.Helper, 'fetch_token')
    @patch.object(utils.Helper, 'fetch_product')
    # Note the inverse order of the mock variables from the order of patch decorators.
    def test_get_product(self, mock_fetch_product: MagicMock, mock_fetch_token: MagicMock):
        mock_fetch_token.return_value = 'abc-567'
        mock_fetch_product.return_value = 'product book-35'

        d = api.get_product_depends_on_class('abc', 'book')
        self.assertEqual('token-abc-567', d['token'])
        self.assertEqual('product book-35', d['product'])

    @patch('utils.fetch_token')
    @patch('utils.fetch_product')
    # Note the inverse order of the mock variables from the order of patch decorators.
    def test_get_product(self, mock_fetch_product: MagicMock, mock_fetch_token: MagicMock):
        mock_fetch_product.return_value = 'product book-35'
        mock_fetch_token.return_value = 'abc-567'

        d = api.get_product_depends_on_func('abc', 'book')
        self.assertEqual('token-abc-567', d['token'])
        self.assertEqual('product book-35', d['product'])
