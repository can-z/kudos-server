#!/usr/bin/env python

from distutils.core import setup

setup(
    name='kudos-server',
    version='1.0',
    description='Kudos server',
    author='Can Zhang',
    author_email='raitorm@gmail.com',
    install_requires=['six', 'flask'],
    packages=['kudos', 'tests'],
)
