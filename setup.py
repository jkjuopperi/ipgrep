#!/usr/bin/env python
from setuptools import setup, find_packages
import os.path

# Read README for long description
#BASE = os.path.dirname(__file__)
#README = os.path.join(BASE, 'README.rst')
#with open(README) as f:
#    long_description = f.read()
long_description="IP grepping tool"  # fixme

setup(name='ipgrep',
      version='0.1.0',
      description="IPv4 netmask aware grep for firewall scripts etc.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: Public Domain',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Internet',
          'Topic :: System :: Networking',
          'Topic :: Utilities',
      ],
      keywords='',
      author='Juho Juopperi',
      # author_email='XXX',
      url='https://github.com/jkjuopperi/ipgrep',
      license='Public Domain',
      packages=find_packages(exclude=['tests']),
      test_suite="tests",
      zip_safe=False,
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      ipgrep=ipgrep.ipgrep:main
      """
      )
