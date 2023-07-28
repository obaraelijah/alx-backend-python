#!/usr/bin/env python3
"""Unit testing.
"""

import unittest
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
from parameterized import parameterized
from unittest.mock import Mock, patch

class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function."""
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
         """Tests access_nested_map's output"""
         return self.assertEqual(access_nested_map(nested_map, path), expected_output)
    
    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """Tests access_nested_map's exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
            
class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """Tests get_json's output."""
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value = mock_response):
            self.assertEqual(get_json(), expected_output)
        
         
        