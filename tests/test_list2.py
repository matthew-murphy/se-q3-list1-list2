#!/usr/bin/env python3
"""
Unit tests for list2

Students should not modify this file.
"""

__author__ = 'madarp'

import sys
import unittest
import importlib
import subprocess


# Kenzie devs: change this to 'soln.list2' to test solution
PKG_NAME = 'list2'


class TestList2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)

    def test_remove_adjacent(self):
        """Check if remove_adjacent function is working"""
        remove_adjacent = self.module.remove_adjacent
        self.assertEqual(
            remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(
            remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        self.assertEqual(
            remove_adjacent([]), [])
        self.assertEqual(
            remove_adjacent([2, 2, 3, 3, 3, 4, 5, 2, 3]), [2, 3, 4, 5, 2, 3])

    def test_linear_merge(self):
        """Check if linear_merge function is working"""
        linear_merge = self.module.linear_merge
        self.assertEqual(
            linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
            ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(
            linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
            ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(
            linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
            ['aa', 'aa', 'aa', 'bb', 'bb'])

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
