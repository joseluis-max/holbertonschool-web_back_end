#!/usr/bin/env python3
"""This module contais the test for the utils class
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from utils import (access_nested_map, get_json, memoize)
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """test class for utils.access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping, path: Sequence,
        expected: Any
    ):
        """test for utils.access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test to exeption of utils.access_nested_map method"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test class for utils.get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test that utils.get_json returns the expected result.
        """
        requests_json = unittest.mock.Mock()
        requests_json.json.return_value = test_payload

        with patch('requests.get', return_value=requests_json) as mocked:
            self.assertEqual(get_json(test_url), test_payload)
            mocked.assert_called_once()


class TestMemoize(unittest.TestCase):
    """test class for utils.memoize decorator
    """

    def test_memoize(self):
        """test for utils.memoize decorator
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_class = TestClass()

        with patch.object(test_class, 'a_method') as mocked:
            self.assertEqual(test_class.a_property(), test_class.a_property())
            mocked.assert_called_once()
