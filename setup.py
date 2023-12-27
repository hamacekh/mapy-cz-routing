# coding: utf-8

"""
    REST API Mapy.cz routing methods

    Service for finding/planning a route between two or more points.   Api is based on common principles described in the document [Common principles of REST API Mapy.cz](/v1/docs/commons/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "mapy-cz-routing"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="REST API Mapy.cz routing methods",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "REST API Mapy.cz routing methods"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Service for finding/planning a route between two or more points.   Api is based on common principles described in the document [Common principles of REST API Mapy.cz](/v1/docs/commons/)
    """,  # noqa: E501
    package_data={"mapy_cz_routing": ["py.typed"]},
)