# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Space(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resource': 'ResourceReference',
        'total_physical_space': 'int',
        'unique_space': 'int',
        'snapshot_space': 'int'
    }

    attribute_map = {
        'resource': 'resource',
        'total_physical_space': 'total_physical_space',
        'unique_space': 'unique_space',
        'snapshot_space': 'snapshot_space'
    }

    def __init__(self, resource=None, total_physical_space=None, unique_space=None, snapshot_space=None):  # noqa: E501
        """Space - a model defined in Swagger"""  # noqa: E501
        self._resource = None
        self._total_physical_space = None
        self._unique_space = None
        self._snapshot_space = None
        self.discriminator = None
        if resource is not None:
            self.resource = resource
        if total_physical_space is not None:
            self.total_physical_space = total_physical_space
        if unique_space is not None:
            self.unique_space = unique_space
        if snapshot_space is not None:
            self.snapshot_space = snapshot_space

    @property
    def resource(self):
        """Gets the resource of this Space.  # noqa: E501


        :return: The resource of this Space.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Space.


        :param resource: The resource of this Space.  # noqa: E501
        :type: ResourceReference
        """

        self._resource = resource

    @property
    def total_physical_space(self):
        """Gets the total_physical_space of this Space.  # noqa: E501

        Total physical space occupied by system, shared space, volume, and snapshot data. Measured in bytes.  # noqa: E501

        :return: The total_physical_space of this Space.  # noqa: E501
        :rtype: int
        """
        return self._total_physical_space

    @total_physical_space.setter
    def total_physical_space(self, total_physical_space):
        """Sets the total_physical_space of this Space.

        Total physical space occupied by system, shared space, volume, and snapshot data. Measured in bytes.  # noqa: E501

        :param total_physical_space: The total_physical_space of this Space.  # noqa: E501
        :type: int
        """

        self._total_physical_space = total_physical_space

    @property
    def unique_space(self):
        """Gets the unique_space of this Space.  # noqa: E501

        The unique physical space occupied by customer data. Unique physical space does not include shared space, snapshots, and internal array metadata. Measured in bytes.  # noqa: E501

        :return: The unique_space of this Space.  # noqa: E501
        :rtype: int
        """
        return self._unique_space

    @unique_space.setter
    def unique_space(self, unique_space):
        """Sets the unique_space of this Space.

        The unique physical space occupied by customer data. Unique physical space does not include shared space, snapshots, and internal array metadata. Measured in bytes.  # noqa: E501

        :param unique_space: The unique_space of this Space.  # noqa: E501
        :type: int
        """

        self._unique_space = unique_space

    @property
    def snapshot_space(self):
        """Gets the snapshot_space of this Space.  # noqa: E501

        The physical space occupied by data unique to one or more snapshots. Measured in bytes.  # noqa: E501

        :return: The snapshot_space of this Space.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_space

    @snapshot_space.setter
    def snapshot_space(self, snapshot_space):
        """Sets the snapshot_space of this Space.

        The physical space occupied by data unique to one or more snapshots. Measured in bytes.  # noqa: E501

        :param snapshot_space: The snapshot_space of this Space.  # noqa: E501
        :type: int
        """

        self._snapshot_space = snapshot_space

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Space, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Space):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
