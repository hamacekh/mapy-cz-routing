# coding: utf-8

"""
    REST API Mapy.cz routing methods

    Service for finding/planning a route between two or more points.   Api is based on common principles described in the document [Common principles of REST API Mapy.cz](/v1/docs/commons/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from mapy_cz_routing.models.routing_error_response import RoutingErrorResponse

class TestRoutingErrorResponse(unittest.TestCase):
    """RoutingErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoutingErrorResponse:
        """Test RoutingErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingErrorResponse`
        """
        model = RoutingErrorResponse()
        if include_optional:
            return RoutingErrorResponse(
                detail = None
            )
        else:
            return RoutingErrorResponse(
        )
        """

    def testRoutingErrorResponse(self):
        """Test RoutingErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
