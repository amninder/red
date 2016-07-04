#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import MutableMapping
import subprocess


class GitConfig(MutableMapping):

    """
    Simple wrapper around git config
    """
    CMD = ['git', 'config']

    def __init__(self, level='alias'):
        """
        :param level: where to store the configuration keys. Can be global,
        local or system see "man git config
        """

        if level not in ['global', 'local', 'system', 'alias']:
            raise ValueError('Level has to be alias, local, global or system')
        self.level = level

    def __iter__(self):
        """
        Iterate over git config keys
        """

        try:
            cmd = self.CMD + ['--list', '-z']
            lines = subprocess.check_output(
                cmd, universal_newlines=True).split('\0')
            keys = (line.split()[0] for line in lines if line)
            return keys
        except subprocess.CalledProcessError:
            return []

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __delitem__(self, key):
        """
        Equivalent to 'git config --unset key'
        """

        try:
            cmd = self.CMD + ['--list', '--unset', key]
            return subprocess.check_call(cmd, universal_newlines=True)
        except subprocess.CalledProcessError:
            raise KeyError

    def __getitem__(self, key):
        """
        Equivalent to 'git config --get key'
        """

        try:
            cmd = self.CMD + ['--get', key]
            return subprocess.check_output(cmd,
                                           universal_newlines=True).strip()
        except subprocess.CalledProcessError:
            raise KeyError

    def __len__(self):
        """
        Counts number git config keys
        """

        try:
            cmd = self.CMD + ['--list', '-z']
            lines = subprocess.check_output(
                cmd, universal_newlines=True).split('\0')
            # the last line is empty so doesn't count
            return len(lines) - 1
        except subprocess.CalledProcessError:
            return 0

    def __setitem__(self, key, value):
        """
        Equivalent to git config --LEVEL key value
        """

        level = '--' + self.level
        try:
            cmd = ['git', 'config', level, key, str(value)]
            subprocess.check_output(cmd, universal_newlines=True).strip()
        except subprocess.CalledProcessError as e:
            if e.returncode == 1:
                raise ValueError
            elif e.returncode == 2:
                print(cmd)
                raise KeyError
            else:
                # I don't know what happened to get here, so just raise
                # the error
                raise

    def keys(self):
        """Get all the key headers from the config file"""
        levels = super(GitConfig, self).keys()
        return list(set([a[0]
                         for a in filter(lambda x: x, [level.split('.')
                                                       for level in levels])]))

    def get_level_mapping(self, alias_only=True):
        """This method return alias or all the level options from .gitconfig file.

        Args:
            only_alias(bool): level to fetch mappin from
        Returns:
            List of alias mapping
            or
            conf_mapping(dict): Level mapping in list from the gitconfig

        Example:
            ['co', 'br']
            or
            {'alias': ['co', 'br'], 'push': ['default']}
        """
        levels = super(GitConfig, self).keys()
        if alias_only:
            return [a.split('.')[1] for a in levels
                    if a.split('.')[0] == self.level]
        else:
            conf_mapping = {}
            for level in self.keys():
                conf_mapping[level] = [a.split('.')[1] for a in levels
                                       if a.split('.')[0] == level]
            print('this')
            return conf_mapping
