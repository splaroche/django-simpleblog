#!/usr/bin/env python
from setuptools import setup, find_packages

required = []
setup(
    name='django-simpleblog',
    version='0.1.0',
    description="A simple blog built for Django 1.7",
    packages=find_packages(),
    author="Steven Laroche",
    author_email="stevenplaroche@gmail.com",
    include_package_data=True,
    zip_safe=False,
    install_requires=required,
)