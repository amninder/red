# vi: ft=python
from gitconfig import GitConfig


def get_alias():
    """This method reads from .gitconfig and returns all the alias mapping.

    Returns:
        alias(list): list of all the alias from .gitconfig
    """
    config = GitConfig()
    return config.get_level_mapping()
