# SPDX-FileCopyrightText: 2022 Alec Delaney
#
# SPDX-License-Identifier: MIT

"""

lib_funcs.py
============

Library-specific functionalities to aid in developing patches

* Author(s): Alec Delaney

"""

import os
import functools
from collections.abc import Sequence
from typing import Protocol, Any, Union
from typing_extensions import TypeAlias
from github.Repository import Repository

# Helpful type annotation for path-like strings
StrPath: TypeAlias = Union[str, os.PathLike[str]]
"""Path or path-like strings"""


# pylint: disable=too-few-public-methods
class LocalLibFunc(Protocol):
    """Typing protocol for methods (or callables) that take the following
    parameters:

    - (StrPath) The path to a specific Adafruit library
    - (Sequence[Any]) A list of any positional arguments
    - (Dict[str, Any]) A dict of any keyword arguments
    """

    def __call__(
        self, lib_path: StrPath, *args: Sequence[Any], **kwargs: dict[str, Any]
    ) -> Any:
        ...


# pylint: disable=too-few-public-methods
class RemoteLibFunc(Protocol):
    """Typing protocol for methods (or callables) that take the following
    parameters:

    - (Repository) The repo as a github.Repository.Repository object
    - (Sequence[Any]) A list of any positional arguments
    - (Dict[str, Any]) A dict of any keyword arguments
    """

    def __call__(
        self, lib_repo: Repository, *args: Sequence[Any], **kwargs: dict[str, Any]
    ) -> Any:
        ...


def in_lib_path(func: LocalLibFunc) -> LocalLibFunc:
    """Decorator for automating temporarily entering a function's
    library directory

    :param LibraryFunc func: The library function to decorate
    """

    @functools.wraps(func)
    def wrapper_use_lib_path(lib_path: StrPath, *args, **kwargs) -> Any:
        # Get the current directory
        current_path = os.getcwd()

        # Enter the library directory for the duration of executing the function
        os.chdir(lib_path)
        result = func(lib_path, *args, **kwargs)
        os.chdir(current_path)

        # Return the result of the function
        return result

    return wrapper_use_lib_path
