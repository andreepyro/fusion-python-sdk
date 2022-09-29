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
from fusion.api.tenant_spaces_api import TenantSpacesApi  # noqa: E501
from fusion.rest import ApiException


class TestTenantSpacesApi(unittest.TestCase):
    """TenantSpacesApi unit test stubs"""

    def setUp(self):
        self.api = TenantSpacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tenant_space(self):
        """Test case for create_tenant_space

        Creates a Tenant Space.  # noqa: E501
        """
        pass

    def test_delete_tenant_space(self):
        """Test case for delete_tenant_space

        Deletes a specific Tenant Space.  # noqa: E501
        """
        pass

    def test_get_tenant_space(self):
        """Test case for get_tenant_space

        Gets a specific Tenant Space.  # noqa: E501
        """
        pass

    def test_get_tenant_space_by_id(self):
        """Test case for get_tenant_space_by_id

        Gets a specific Tenant Space.  # noqa: E501
        """
        pass

    def test_get_tenant_space_performance(self):
        """Test case for get_tenant_space_performance

        Gets performance metrics of a specific Tenant Space.  # noqa: E501
        """
        pass

    def test_get_tenant_space_space(self):
        """Test case for get_tenant_space_space

        Gets space metrics of a specific Tenant Space.  # noqa: E501
        """
        pass

    def test_list_tenant_spaces(self):
        """Test case for list_tenant_spaces

        Gets a list of all Tenant Spaces.  # noqa: E501
        """
        pass

    def test_update_tenant_space(self):
        """Test case for update_tenant_space

        Updates a Tenant Space.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
