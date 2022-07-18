#!/usr/bin/env python3
""" client testter """

from cgi import test
import unittest
from unittest import mock
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
        test_return = GithubOrgClient(org_name).org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once

    @patch('GithubOrgClient', return_value={'payload': True})
    def test_public_repos_url(self):
        """ Test if _public_repos_url result
        is as expected """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock,
                          return_value={'repos_url': 'Belayneh'}) as mock_get:
            test_json = {"repos_url": "Belayneh"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(test_return,
                             mock_get.return_value.get('repos_url'))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """ to unit-test GithubOrgClient.public_repos """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once
