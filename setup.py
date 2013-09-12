##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.testbrowser package
"""
import os
from setuptools import setup, find_packages

long_description = (
    '.. contents::\n\n'
    + open('README.rst').read()
    + '\n\n'
    + open(os.path.join('src', 'zope', 'testbrowser', 'README.txt')).read()
    + '\n\n'
    + open('CHANGES.rst').read()
)

tests_require = ['zope.testing']

setup(
    name='zope.testbrowser',
    version='5.0.0.dev0',
    url='http://pypi.python.org/pypi/zope.testbrowser',
    license='ZPL 2.1',
    description='Programmable browser for functional black-box tests',
    author='Zope Corporation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Testing',
        'Topic :: Internet :: WWW/HTTP',
    ],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope'],
    test_suite='zope.testbrowser.tests',
    tests_require=tests_require,
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.schema',
        'zope.cachedescriptors',
        'pytz > dev',
        'WebTest >= 2.0.6',
        'WSGIProxy2',
        'six',
    ],
    extras_require={
        'test': tests_require,
        'test_bbb': [
            'zope.testbrowser [test]',
        ],
        'wsgi': [
            # BBB
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
