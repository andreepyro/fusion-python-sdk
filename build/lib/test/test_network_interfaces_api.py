# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.network_interfaces_api import NetworkInterfacesApi  # noqa: E501
from fusion.rest import ApiException


class TestNetworkInterfacesApi(unittest.TestCase):
    """NetworkInterfacesApi unit test stubs"""

    def setUp(self):
        self.api = NetworkInterfacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_network_interface(self):
        """Test case for get_network_interface

        (Provider) Gets a specific Network Interface.  # noqa: E501
        """
        pass

    def test_get_network_interface_by_id(self):
        """Test case for get_network_interface_by_id

        (Provider) Gets a specific Network Interface.  # noqa: E501
        """
        pass

    def test_list_network_interfaces(self):
        """Test case for list_network_interfaces

        (Provider) Gets a list of all Network Interfaces.  # noqa: E501
        """
        pass

    def test_update_network_interface(self):
        """Test case for update_network_interface

        (Provider) Updates a Network Interface.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
