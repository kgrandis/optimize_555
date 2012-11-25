import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

VERSION = '0.1.0'

setup(
    name = "optimize_555",
    version = VERSION,
    author = "Kurt Grandis",
    author_email = "kgrandis@gmail.com",
    description = "Optimize the selection of electronic components for a 555 circuit.",
    long_description = read('README.rst'),
    license = 'Apache License 2.0',
    url = "http://github.com/kgrandis/optimize_555",
    packages = find_packages(),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Topic :: Other/Nonlisted Topic",
        "Programming Language :: Python :: 2",
        ],

    py_modules = ['numpy>=1.6', 'scipy>=0.10'],
    zip_safe = False,
    test_suite = 'tests',
)
