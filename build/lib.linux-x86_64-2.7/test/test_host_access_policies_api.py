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
from fusion.api.host_access_policies_api import HostAccessPoliciesApi  # noqa: E501
from fusion.rest import ApiException


class TestHostAccessPoliciesApi(unittest.TestCase):
    """HostAccessPoliciesApi unit test stubs"""

    def setUp(self):
        self.api = HostAccessPoliciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_host_access_policy(self):
        """Test case for create_host_access_policy

        Creates a Host Access Policy.  # noqa: E501
        """
        pass

    def test_delete_host_access_policy(self):
        """Test case for delete_host_access_policy

        Deletes a specific host access policy.  # noqa: E501
        """
        pass

    def test_get_host_access_policy(self):
        """Test case for get_host_access_policy

        Gets a specific Host Access Policy.  # noqa: E501
        """
        pass

    def test_get_host_access_policy_by_id(self):
        """Test case for get_host_access_policy_by_id

        Gets a specific Host Access Policy.  # noqa: E501
        """
        pass

    def test_list_host_access_policies(self):
        """Test case for list_host_access_policies

        Gets a list of all Host Access Policies.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
