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

if sys.argv[-1] == u'publish':
    os.system(u'python setup.py sdist upload')
    sys.exit

packages = [u'd2lvalence', ]

# We depend on Kenneth Reitz' requests package to handle the actual HTTP traffic
requires = [u'requests >= 1.2.0', ]

setup(
    name=u'D2LValence',
    version=d2lvalence.__version__,
    description=u'D2LValence client library for Python.',
    long_description=open(u'README.rst').read() + u'\n\n' +
                     open(u'HISTORY.rst').read(),
    author=u'Desire2Learn Inc.',
    author_email=u'Valence@Desire2Learn.com',
    url=u'http://www.desire2learn.com/r/valencehome',
    packages=packages,
    package_data={u'': [u'LICENSE', ] },
    include_package_data=True,
    install_requires=[
        u'requests >= 1.2.0',
        ],
    license=open(u'LICENSE').read(),
    classifiers=(
        u'Development Status :: 4 - Beta',
        u'Intended Audience :: Developers',
        u'Natural Language :: English',
        u'License :: OSI Approved :: Apache Software License',
        u'Programming Language :: Python',
        u'Programming Language :: Python :: 3',
        u'Programming Language :: Python :: 3.0',
        u'Programming Language :: Python :: 3.1',
        u'Programming Language :: Python :: 3.2',
        u'Programming Language :: Python :: 3.3',
        u'Programming Language :: Python :: 3.4'
        ),
    )
