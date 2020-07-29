# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Domain(object):
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
        'created_at': 'datetime',
        'domain': 'str',
        'has_authentication': 'bool',
        'is_authentication_valid': 'bool',
        'is_dmarc_passed': 'bool',
        'is_free_domain': 'bool',
        'is_verified': 'bool',
        'spf_status': 'object'
    }

    attribute_map = {
        'created_at': 'created_at',
        'domain': 'domain',
        'has_authentication': 'has_authentication',
        'is_authentication_valid': 'is_authentication_valid',
        'is_dmarc_passed': 'is_dmarc_passed',
        'is_free_domain': 'is_free_domain',
        'is_verified': 'is_verified',
        'spf_status': 'spf_status'
    }

    def __init__(self, created_at=None, domain=None, has_authentication=None, is_authentication_valid=None, is_dmarc_passed=None, is_free_domain=None, is_verified=None, spf_status=None):  # noqa: E501
        """Domain - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._domain = None
        self._has_authentication = None
        self._is_authentication_valid = None
        self._is_dmarc_passed = None
        self._is_free_domain = None
        self._is_verified = None
        self._spf_status = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        self.domain = domain
        if has_authentication is not None:
            self.has_authentication = has_authentication
        if is_authentication_valid is not None:
            self.is_authentication_valid = is_authentication_valid
        if is_dmarc_passed is not None:
            self.is_dmarc_passed = is_dmarc_passed
        if is_free_domain is not None:
            self.is_free_domain = is_free_domain
        if is_verified is not None:
            self.is_verified = is_verified
        if spf_status is not None:
            self.spf_status = spf_status

    @property
    def created_at(self):
        """Gets the created_at of this Domain.  # noqa: E501


        :return: The created_at of this Domain.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Domain.


        :param created_at: The created_at of this Domain.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def domain(self):
        """Gets the domain of this Domain.  # noqa: E501


        :return: The domain of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Domain.


        :param domain: The domain of this Domain.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def has_authentication(self):
        """Gets the has_authentication of this Domain.  # noqa: E501


        :return: The has_authentication of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._has_authentication

    @has_authentication.setter
    def has_authentication(self, has_authentication):
        """Sets the has_authentication of this Domain.


        :param has_authentication: The has_authentication of this Domain.  # noqa: E501
        :type: bool
        """

        self._has_authentication = has_authentication

    @property
    def is_authentication_valid(self):
        """Gets the is_authentication_valid of this Domain.  # noqa: E501


        :return: The is_authentication_valid of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._is_authentication_valid

    @is_authentication_valid.setter
    def is_authentication_valid(self, is_authentication_valid):
        """Sets the is_authentication_valid of this Domain.


        :param is_authentication_valid: The is_authentication_valid of this Domain.  # noqa: E501
        :type: bool
        """

        self._is_authentication_valid = is_authentication_valid

    @property
    def is_dmarc_passed(self):
        """Gets the is_dmarc_passed of this Domain.  # noqa: E501


        :return: The is_dmarc_passed of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._is_dmarc_passed

    @is_dmarc_passed.setter
    def is_dmarc_passed(self, is_dmarc_passed):
        """Sets the is_dmarc_passed of this Domain.


        :param is_dmarc_passed: The is_dmarc_passed of this Domain.  # noqa: E501
        :type: bool
        """

        self._is_dmarc_passed = is_dmarc_passed

    @property
    def is_free_domain(self):
        """Gets the is_free_domain of this Domain.  # noqa: E501


        :return: The is_free_domain of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._is_free_domain

    @is_free_domain.setter
    def is_free_domain(self, is_free_domain):
        """Sets the is_free_domain of this Domain.


        :param is_free_domain: The is_free_domain of this Domain.  # noqa: E501
        :type: bool
        """

        self._is_free_domain = is_free_domain

    @property
    def is_verified(self):
        """Gets the is_verified of this Domain.  # noqa: E501


        :return: The is_verified of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._is_verified

    @is_verified.setter
    def is_verified(self, is_verified):
        """Sets the is_verified of this Domain.


        :param is_verified: The is_verified of this Domain.  # noqa: E501
        :type: bool
        """

        self._is_verified = is_verified

    @property
    def spf_status(self):
        """Gets the spf_status of this Domain.  # noqa: E501


        :return: The spf_status of this Domain.  # noqa: E501
        :rtype: object
        """
        return self._spf_status

    @spf_status.setter
    def spf_status(self, spf_status):
        """Sets the spf_status of this Domain.


        :param spf_status: The spf_status of this Domain.  # noqa: E501
        :type: object
        """

        self._spf_status = spf_status

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
        if issubclass(Domain, dict):
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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other