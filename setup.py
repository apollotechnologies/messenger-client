#!/usr/bin/env python

from distutils.core import setup

setup(
    name='messenger_client',
    version='1.0',
    description='Unofficial Python wrapper for the Facebook Messenger API',
    author='Apollo Technologies',
    author_email='contact@apollo.tech',
    url='https://apollo.tech',
    packages=['messenger_client'],
    install_requires=['enum34', 'requests', 'six']
)
