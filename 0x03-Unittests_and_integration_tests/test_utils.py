#!/usr/bin/env python3
""" Parameterize a unit test """

import unittest
from unittest import mock
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test class inherits the TestCase module
    from the unittest super module """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """ method to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test the KeyError is raise some exception """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(err.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ TestCase """
    @parameterized.expand([
        ("http://example.com", {"playload": True}),
        ("http://example.com", {"playload": False}),

    ])
    @mock.patch("test_utils.get_json")
    def test_get_json(self, test_url, test_playload, mock_get):
        """ test if expected json """
        mock_get.return_value = test_playload
        result = get_json(test_url)
        self.assertEqual(result, test_playload)


class TestMemoize(unittest.TestCase):
    """ TESTCASE """

    def test_memoize(self):
        """ some testter """
        class TestClass:
            """ Test class """

            def a_method(self):
                """ user defined method """
                return 42

            @memoize
            def a_property(self):
                """ user defined property """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
