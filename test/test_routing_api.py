# coding: utf-8

"""
    REST API Mapy.cz routing methods

    Service for finding/planning a route between two or more points.   Api is based on common principles described in the document [Common principles of REST API Mapy.cz](/v1/docs/commons/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mapy_cz_routing.api.routing_api import RoutingApi


class TestRoutingApi(unittest.TestCase):
    """RoutingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RoutingApi()

    def tearDown(self) -> None:
        pass

    def test_basic_route_v1_routing_route_get(self) -> None:
        """Test case for basic_route_v1_routing_route_get

        Basic Route
        """
        pass


if __name__ == '__main__':
    unittest.main()