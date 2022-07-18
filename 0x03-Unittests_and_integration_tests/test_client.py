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

    @patch("client.get_json", return_value=[{"name": "Belayneh"}])
    def test_public_repos(self, mock_get):
        """ to unit-test GithubOrgClient.public_repos """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("Belayneh")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["Belayneh"])
            mock_get.assert_called_once
            mock_pub.assert_called_once


@parameterized.expand([
    ({"license": {"key": "my_license"}}, "my_license", True),
    ({"license": {"key": "other_license"}}, "my_license", False),
])
def test_has_license(self, repo, license_key, expected_return):
    """ to unit-test GithubOrgClient.has_license """
    test_client = GithubOrgClient("holberton")
    test_return = test_client.has_license(repo, license_key)
    self.assertEqual(expected_return, test_return)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TESTCASE """
    @classmethod
    def setUpClass(cls):
        """ It is part of the unittest.TestCase API
        method to return example payloads found in the fixtures """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ It is part of the unittest.TestCase API
        method to stop the patcher """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ method to test GithubOrgClient.public_repos """
        test_class = GithubOrgClient("holberton")
        assert True

    def test_public_repos_with_license(self):
        """ method to test the public_repos with the argument license """
        test_class = GithubOrgClient("holberton")
        assert True
