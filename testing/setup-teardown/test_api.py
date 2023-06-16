#!/usr/bin/env python -m unittest

import os
import unittest

from api import connect_api


class TestApi(unittest.TestCase):
    sys_envs: dict[str, str] = {}
    envs: dict[str, str] = {
        'PR_ACCESS_KEY': 'dummy-access-key',
        'PR_SECRET_KEY': 'dummy-secret-key',
    }

    def setUp(self):
        for k, v in self.envs.items():
            # Save an existing env variable.
            # Note: os.environ.get() returns None if key not found.
            self.sys_envs[k] = os.environ.get(k)

            # Inject our value to env variables.
            os.environ[k] = v

    def tearDown(self):
        for k, v in self.envs.items():
            if v is None:
                os.environ.pop(k)
                continue

            # Revert to the previous value
            os.environ[k] = v

    def test_connect_api(self):
        self.assertIsNotNone(connect_api())


