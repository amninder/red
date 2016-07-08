#!/usr/bin/env python
# -*- coding: utf-8 -*-
# :vi ft=python

import unittest
import mock
from ..gitconfig import GitConfig


class GitConfigTest(unittest.TestCase):

    """Test cases for GitConfig class"""

    def setUp(self):
        """Basic setup"""
        self.config = GitConfig()

    def test_init_with_invalid_valid_level_value(self):
        """Test case to catch invalid level in .gitconfig file."""
        with self.assertRaises(ValueError):
            GitConfig('sample')

    @mock.patch('subprocess.check_output')
    def test_get_level_mapping_for_alias_only_as_true(self, mock_check_output):
        """Test case to get aliases as list."""
        mock_check_output.return_value = 'alias.br\nbranch\x00alias.ci\ncommit'
        config = GitConfig()
        alias = config.get_level_mapping()
        self.assertEqual(alias, ['br', 'ci'])

    @mock.patch('subprocess.check_output')
    def test_get_level_mapping_for_alias_only_as_false(self,
                                                       mock_check_output):
        """Test case to get aliases as dictionary."""
        mock_check_output.return_value = 'alias.br\nbranch\x00alias.ci\ncommit'
        config = GitConfig()
        alias = config.get_level_mapping(alias_only=False)
        self.assertEqual(alias, {'alias': ['br', 'ci']})

    def test_has_number_in_string(self):
        """Test case to find if string contains number."""
        self.assertTrue(self.config._has_number_in_string("this is 3"))

    def test_has_no_number_in_string(self):
        """Test case to find if string doesnt contains number."""
        self.assertFalse(self.config._has_number_in_string("sample sentence."))
