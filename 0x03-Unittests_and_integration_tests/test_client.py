#!/usr/bin/env python3
""" client testter """

from http import client
import imp
import unittest
from defer import return_value
from parameterized import parameterized
from urllib.error import HTTPError
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class that inherits TestCase from unittest """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """ Test GithubOrgClient.org and return """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once
