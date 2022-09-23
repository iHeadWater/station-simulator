#!/usr/bin/env python
# coding=utf-8

import os
import sys
import random
import string

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='dijkstra_conda',
    version=''.join(random.sample(string.digits, 8)),
    description='A test project',
    entry_points={'console_scripts': ['calcstream = dijkstra_conda.cli:main']},
    long_description='https://readthedocs.org/projects/calctest/',
    author='dijkstra_conda-test',
    url='https://github.com/iHeadWater/dijkstra-conda',
    packages=[
        'dijkstra_conda',
    ],
    package_dir={'dijkstra_conda': 'dijkstra_conda'},
    include_package_data=True,
    install_requires=['pytest>=7.1.3', 'setuptools>=63.4.1', 'click>=8.1.3', 'bidict>=0.21.2', 'multidict>=6.0.2',
                      'networkx>=2.8.6', 'pandas>=1.4.3', 'shapely>=1.8.4', 'pyshp>=2.3.1'],
    license='MIT',
    zip_safe=False,
    keywords='dijkstra_conda',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
