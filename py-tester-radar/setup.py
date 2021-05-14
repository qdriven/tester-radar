# coding: utf-8

"""
 {{project_description}}
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "{{project_name}}"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
# project template reference:https://github.com/brettcannon/python-project-template.git
#


REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="<Desc>",
    author="<Author>",
    author_email="<AuthorEmail>",
    url="",
    keywords=["Any"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    <Detail>
    """
)
