#!/usr/bin/env python3

u"""
distutils/setuptools install script.

Form of this file borrowed from Kenneth Reitz' requests package
"""

from __future__ import absolute_import
import os
import sys
from io import open

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup

import d2lvalence

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit

packages = ['d2lvalence', ]

# We depend on Kenneth Reitz' requests package to handle the actual HTTP traffic
requires = ['requests >= 1.2.0', ]

setup(
    name='D2LValence',
    version=d2lvalence.__version__,
    description='D2LValence client library for Python.',
    long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    author='Desire2Learn Inc.',
    author_email='Valence@Desire2Learn.com',
    url='http://www.desire2learn.com/r/valencehome',
    packages=packages,
    package_data={'d2lvalence': ['LICENSE', ], },
    include_package_data=True,
    install_requires=[
        'requests >= 1.2.0',
    ],
    license=open(u'LICENSE').read(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
