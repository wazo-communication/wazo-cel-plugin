#!/usr/bin/env python3
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_cel',
    version='1.0.0',
    description='Wazo CEL API',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo-platform.org',

    packages=find_packages(),
    include_package_data=True,
    package_data={
        'wazo_cel': ['*/api.yml'],
    },
    entry_points={
        'wazo_call_logd.plugins': [
            'cel = wazo_cel.call_logd.plugin:Plugin',
        ]
    }
)
