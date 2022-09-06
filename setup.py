#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys 

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup( 
  name='hexroute',
  version='0.1',
  url='https://github.com/musashiXXX/python-hexroute',
  license='GNU GPLv3',
  author='Charles Hamilton',
  author_email='chamilton@nefaria.com',
  keywords='249 121 dhcp hexroute',
  description='Generate a hex string for use with DHCP options 121/249',
  long_description='',
  classifiers=['Programming Language :: Python :: 3'],
  py_modules=['hexroute']
)

