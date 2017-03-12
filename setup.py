# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


testpkgs = [
]
install_requires = [
    'django==1.6',
    'pyws',
]

setup(
    name='zarinpakl_mock',
    version='0.1',
    description='',
    author='Amin Etesamian',
    author_email='aminetesamian1371@gmail.com',
    url='https://github.com/eteamin/zarinpal_mock',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    tests_require=testpkgs,
    include_package_data=True,
)