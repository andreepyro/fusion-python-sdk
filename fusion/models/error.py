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

class Error(object):
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
        'message': 'str',
        'details': 'dict(str, str)',
        'pure_code': 'str',
        'http_code': 'int'
    }

    attribute_map = {
        'message': 'message',
        'details': 'details',
        'pure_code': 'pure_code',
        'http_code': 'http_code'
    }

    def __init__(self, message=None, details=None, pure_code=None, http_code=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._details = None
        self._pure_code = None
        self._http_code = None
        self.discriminator = None
        self.message = message
        self.details = details
        self.pure_code = pure_code
        self.http_code = http_code

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        The error message, e.g., \"Cannot delete a volume while it is connected to hosts\".  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        The error message, e.g., \"Cannot delete a volume while it is connected to hosts\".  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def details(self):
        """Gets the details of this Error.  # noqa: E501

        Key-value pairs containing details about the error.  # noqa: E501

        :return: The details of this Error.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Error.

        Key-value pairs containing details about the error.  # noqa: E501

        :param details: The details of this Error.  # noqa: E501
        :type: dict(str, str)
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def pure_code(self):
        """Gets the pure_code of this Error.  # noqa: E501

        Pure Code describing the error. May be more specific than the HTTP code. The code may be one of the following. INTERNAL - An internal error occurred. NOT_FOUND - A resource was not found. ALREADY_EXISTS - A resource cannot be created because one already exists by this name. INVALID_ARGUMENT - An argument value is incorrect. NOT_AUTHENTICATED - The client is not authenticated. PERMISSION_DENIED - The client is authenticated, but lacks a specific permission required for this action. NOT_IMPLEMENTED - The functionality has not been implemented yet. FAILED_PRECONDITION - A precondition of the action is not fulfilled. For instance, trying to use a resource that is being deleted. CONFLICT - This action came into conflict with another. FAILED_TRANSACTION - An action could not be performed due to conflict with another transaction. CANCELED - The action was canceled. DEADLINE_EXCEEDED - The action could not be completed in the time allotted. UNAVAILABLE - A required service is unavailable. EXHAUSTED - A required resource is not available. For instance, there is no storage space in the Placement Group.   # noqa: E501

        :return: The pure_code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._pure_code

    @pure_code.setter
    def pure_code(self, pure_code):
        """Sets the pure_code of this Error.

        Pure Code describing the error. May be more specific than the HTTP code. The code may be one of the following. INTERNAL - An internal error occurred. NOT_FOUND - A resource was not found. ALREADY_EXISTS - A resource cannot be created because one already exists by this name. INVALID_ARGUMENT - An argument value is incorrect. NOT_AUTHENTICATED - The client is not authenticated. PERMISSION_DENIED - The client is authenticated, but lacks a specific permission required for this action. NOT_IMPLEMENTED - The functionality has not been implemented yet. FAILED_PRECONDITION - A precondition of the action is not fulfilled. For instance, trying to use a resource that is being deleted. CONFLICT - This action came into conflict with another. FAILED_TRANSACTION - An action could not be performed due to conflict with another transaction. CANCELED - The action was canceled. DEADLINE_EXCEEDED - The action could not be completed in the time allotted. UNAVAILABLE - A required service is unavailable. EXHAUSTED - A required resource is not available. For instance, there is no storage space in the Placement Group.   # noqa: E501

        :param pure_code: The pure_code of this Error.  # noqa: E501
        :type: str
        """
        if pure_code is None:
            raise ValueError("Invalid value for `pure_code`, must not be `None`")  # noqa: E501
        allowed_values = ["INTERNAL", "NOT_FOUND", "ALREADY_EXISTS", "INVALID_ARGUMENT", "NOT_AUTHENTICATED", "PERMISSION_DENIED", "NOT_IMPLEMENTED", "FAILED_PRECONDITION", "CONFLICT", "FAILED_TRANSACTION", "CANCELED", "DEADLINE_EXCEEDED", "UNAVAILABLE", "EXHAUSTED"]  # noqa: E501
        if pure_code not in allowed_values:
            raise ValueError(
                "Invalid value for `pure_code` ({0}), must be one of {1}"  # noqa: E501
                .format(pure_code, allowed_values)
            )

        self._pure_code = pure_code

    @property
    def http_code(self):
        """Gets the http_code of this Error.  # noqa: E501

        The HTTP code returned by the request. It will be the same as the header response status code. The code may be one of the following. 400 Bad Request - The request payload is malformed; e.g. incorrection JSON. 401 Unauthorized - The client is not authenticated. 403 Forbidden - The client is authenticated, but lacks a specific permission required for this action. 404 Not Found - A resource was not found. 408 Request Timeout - The action could not be completed in the time allotted. 409 Conflict - This action came into conflict with another. 412 Precondition Failed - A precondition of the action is not fulfilled. For instance, trying to use a resource that is being deleted. 422 Unprocessable Entity - An argument value is incorrect. The request was well-formed but was unable to be followed due to semantic errors; e.g. an incorrect enum value. 429 Too Many Requests - The user has sent too many requests in a given amount of time (\"rate limiting\"). 500 Internal Server Error - An internal error occurred. 501 Not Implemented - The functionality has not been implemented yet. 503 Service Unavailable - A required service is unavailable.   # noqa: E501

        :return: The http_code of this Error.  # noqa: E501
        :rtype: int
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        """Sets the http_code of this Error.

        The HTTP code returned by the request. It will be the same as the header response status code. The code may be one of the following. 400 Bad Request - The request payload is malformed; e.g. incorrection JSON. 401 Unauthorized - The client is not authenticated. 403 Forbidden - The client is authenticated, but lacks a specific permission required for this action. 404 Not Found - A resource was not found. 408 Request Timeout - The action could not be completed in the time allotted. 409 Conflict - This action came into conflict with another. 412 Precondition Failed - A precondition of the action is not fulfilled. For instance, trying to use a resource that is being deleted. 422 Unprocessable Entity - An argument value is incorrect. The request was well-formed but was unable to be followed due to semantic errors; e.g. an incorrect enum value. 429 Too Many Requests - The user has sent too many requests in a given amount of time (\"rate limiting\"). 500 Internal Server Error - An internal error occurred. 501 Not Implemented - The functionality has not been implemented yet. 503 Service Unavailable - A required service is unavailable.   # noqa: E501

        :param http_code: The http_code of this Error.  # noqa: E501
        :type: int
        """
        if http_code is None:
            raise ValueError("Invalid value for `http_code`, must not be `None`")  # noqa: E501
        allowed_values = [401, 403, 404, 408, 409, 412, 422, 429, 500, 501, 503]  # noqa: E501
        if http_code not in allowed_values:
            raise ValueError(
                "Invalid value for `http_code` ({0}), must be one of {1}"  # noqa: E501
                .format(http_code, allowed_values)
            )

        self._http_code = http_code

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
        if issubclass(Error, dict):
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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
