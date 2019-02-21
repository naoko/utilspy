#!/usr/bin/env python

import os
import sys
import shlex

from setuptools import setup, find_packages
from setuptools.command.test import test


class RunTest(test):
    pytest_args = ''
    mypy_args = list()

    def initialize_options(self):
        test.initialize_options(self)
        self.mypy_args = ['utilspy']

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        import mypy.api

        color_red = '\x1b[31;1m'
        color_green = '\x1b[32;1m'
        color_default = '\x1b[0m'
        exit_ok = 0

        err_no = pytest.main(shlex.split(self.pytest_args))
        if err_no != exit_ok:
            sys.exit(err_no)

        print(">>> Running mypy")
        stdout, _, status = mypy.api.run(args=self.mypy_args)
        if status:
            raise SystemExit("{color_red}ERROR!\n {color_default}{msg}".format(
                color_red=color_red, color_default=color_default, msg=stdout))

        print("{color}All good{default}".format(color=color_green, default=color_default))
        sys.exit(exit_ok)


here = os.path.realpath(os.path.dirname(__file__))
req_dir = os.path.join(here, 'requirements')


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith(("#", "--"))]


requirements = parse_requirements(os.path.join(req_dir, 'main.txt'))
test_requirements = parse_requirements(os.path.join(req_dir, 'test.txt'))

version_file = open(os.path.join(here, 'VERSION'))
version = version_file.read().strip()

setup(
    name='utilspy',
    version=version,
    description='Generic code for python',
    long_description='',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],
    author='Naoko Reeves',
    author_email='',
    
    url='https://github.com/naoko/utilspy.git',
    packages=find_packages(exclude=('tests*',)),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    tests_require=test_requirements,
    cmdclass={
        'test': RunTest,
    },
)
