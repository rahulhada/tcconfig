# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import os.path
import sys

import setuptools

import tcconfig


REQUIREMENT_DIR = "requirements"


with open("README.rst") as fp:
    long_description = fp.read()

with open(os.path.join("docs", "pages", "introduction", "summary.txt")) as f:
    summary = f.read()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "build_requirements.txt")) as f:
    build_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "docs_requirements.txt")) as f:
    docs_requires = [line.strip() for line in f if line.strip()]

setuptools_require = ["setuptools>=20.2.2"]
needs_pytest = set(["pytest", "test", "ptr"]).intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

setuptools.setup(
    name="tcconfig",
    version=tcconfig.VERSION,
    url="https://github.com/thombashi/tcconfig",

    author="Tsuyoshi Hombashi",
    author_email="tsuyoshi.hombashi@gmail.com",
    description=summary,
    keywords=[
        "traffic control", "tc", "traffic shaping", "bandwidth",
        "latency", "packet loss",
    ],
    long_description=long_description,
    license="MIT License",
    include_package_data=True,
    packages=setuptools.find_packages(exclude=['test*']),

    install_requires=setuptools_require + install_requires,
    setup_requires=setuptools_require + pytest_runner,
    tests_require=tests_requires,
    extras_require={
        "build": build_requires,
        "docs": docs_requires,
        "test": tests_requires,
    },
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*',

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
    ],
    entry_points={
        "console_scripts": [
            "tcset=tcconfig.tcset:main",
            "tcdel=tcconfig.tcdel:main",
            "tcshow=tcconfig.tcshow:main",
        ],
    })
