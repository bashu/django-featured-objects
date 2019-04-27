#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

from featured import __version__


version = ".".join(map(str, __version__))

setup(
    name='django-featured-objects',
    version=version,
    description='Django app for making any object featured',
    author='Pedro Buron',
    author_email='pedro@witoi.com',
    long_description=open('README.rst', 'r').read(),
    url='http://desarrollo.witoi.com/',
    packages=[
        'featured',
        'featured.migrations',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    install_requires=[
        'swapper',
    ],
    requires=[
        'Django (>=1.4.2)',
    ],
    tests_require=[
        'django-setuptest',
        'mock',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
)
