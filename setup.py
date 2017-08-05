#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    setup.py
    ~~~~~~~~

    Installs the restexample package.

    :copyright: (c) 2017 by tscott.
    :license: see LICENSE for more details.
"""

import codecs
import os
import re
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """Taken from pypa pip setup.py:
    intentionally *not* adding an encoding option to open, See:
       https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    """
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='restexample',
    entry_points = {
        'console_scripts': ['restexample=restexample.main:main'],
    },
    version=find_version("restexample", "__init__.py"),
    description='An REST API example using Flask and MongoDB',
    long_description=read('README.md'),
    author='Tim Scott',
    author_email='tim@developerautomation.com',
    url='http://developerautomation.com/',
    packages=['restexample'],
    platforms='any',
    license='LICENSE',
    install_requires=[]
)
