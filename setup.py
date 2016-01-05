# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

from pushall import __version__

setup(
   name='python-pushall',
   version=__version__,
   description='API Wrapper',
   long_description=open('README.md', 'r').read(),
   keywords='api, push, push notification, pushall, wrapper',
   author='Alexander Sapronov',
   author_email='a@sapronov.me',
   url='https://github.com/WarmongeR1/python-pushall/',
   license='MIT',
   package_dir={'pushall': 'pushall'},
   include_package_data=True,
   packages=find_packages(),
   classifiers=[
       "Programming Language :: Python",
   ],
   zip_safe=False,
)
