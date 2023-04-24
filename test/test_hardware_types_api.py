# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.hardware_types_api import HardwareTypesApi  # noqa: E501
from fusion.rest import ApiException


class TestHardwareTypesApi(unittest.TestCase):
    """HardwareTypesApi unit test stubs"""

    def setUp(self):
        self.api = HardwareTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_hardware_type(self):
        """Test case for get_hardware_type

        (Provider) Gets a specific Hardware Type.  # noqa: E501
        """
        pass

    def test_get_hardware_type_by_id(self):
        """Test case for get_hardware_type_by_id

        (Provider) Gets a specific Hardware Type.  # noqa: E501
        """
        pass

    def test_list_hardware_types(self):
        """Test case for list_hardware_types

        (Provider) Gets a list of all hardware types.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
