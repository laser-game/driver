#!/usr/bin/env python3
# coding=utf-8

import sys
from distutils import core

from setuptools import find_packages

import lgba

__author__ = "Jan Vykydal"
__license__ = "GNU GPL Version 3"

if sys.version_info < (3, 5):
    print('Run in python >= 3.5 please.', file=sys.stderr)
    exit(1)


def setup():
    core.setup(
        name='laser-game-driver',
        version=lgd.__version__,
        license='GNU GENERAL PUBLIC LICENSE Version 3',
        author='Jan Vykydal',
        author_email='john.vykydal@gmail.com',
        packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    )


if __name__ == '__main__':
    setup()
