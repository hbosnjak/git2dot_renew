#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-
# pylint: disable=invalid-name
# HB 12.12.2024 Update from imp to importlib libary

import io
import os
from os.path import join as ospj

import importlib.util

from setuptools import find_packages, setup


_dir = os.path.abspath(os.path.dirname(__file__))

SRC = ospj(_dir, "git2dot")
README = ospj(_dir, "README.rst")
DOCS = ospj(_dir, "docs")
TESTS = ospj(_dir, "tests")

# Use importlib.util to load the __pkginfo__.py module
spec = importlib.util.spec_from_file_location("__pkginfo__", ospj(SRC, "__pkginfo__.py"))
PKG = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PKG)


def readFile(fname, m="rt", enc="utf-8", nl=None):
    with io.open(fname, mode=m, encoding=enc, newline=nl) as f:
        return f.read()


setup(
    name=PKG.package,
    version=PKG.version,
    description=PKG.description,
    long_description=readFile(README),
    url=PKG.url,
    author=PKG.authors[0],
    author_email=PKG.emails[0],
    license=PKG.license,
    keywords=PKG.keywords,
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=PKG.install_requires,
    entry_points=PKG.get_entry_points(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=PKG.classifiers,
)
