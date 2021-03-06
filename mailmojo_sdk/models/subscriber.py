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


class Subscriber(object):
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
        'email': 'str',
        'first_name': 'str',
        'force_subscribe': 'bool',
        'last_name': 'str',
        'name': 'str',
        'subscribed': 'datetime',
        'tags': 'list[str]'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'first_name',
        'force_subscribe': 'force_subscribe',
        'last_name': 'last_name',
        'name': 'name',
        'subscribed': 'subscribed',
        'tags': 'tags'
    }

    def __init__(self, email=None, first_name=None, force_subscribe=True, last_name=None, name=None, subscribed=None, tags=None):  # noqa: E501
        """Subscriber - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._force_subscribe = None
        self._last_name = None
        self._name = None
        self._subscribed = None
        self._tags = None
        self.discriminator = None

        self.email = email
        if first_name is not None:
            self.first_name = first_name
        if force_subscribe is not None:
            self.force_subscribe = force_subscribe
        if last_name is not None:
            self.last_name = last_name
        if name is not None:
            self.name = name
        if subscribed is not None:
            self.subscribed = subscribed
        if tags is not None:
            self.tags = tags

    @property
    def email(self):
        """Gets the email of this Subscriber.  # noqa: E501


        :return: The email of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Subscriber.


        :param email: The email of this Subscriber.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this Subscriber.  # noqa: E501


        :return: The first_name of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Subscriber.


        :param first_name: The first_name of this Subscriber.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def force_subscribe(self):
        """Gets the force_subscribe of this Subscriber.  # noqa: E501


        :return: The force_subscribe of this Subscriber.  # noqa: E501
        :rtype: bool
        """
        return self._force_subscribe

    @force_subscribe.setter
    def force_subscribe(self, force_subscribe):
        """Sets the force_subscribe of this Subscriber.


        :param force_subscribe: The force_subscribe of this Subscriber.  # noqa: E501
        :type: bool
        """

        self._force_subscribe = force_subscribe

    @property
    def last_name(self):
        """Gets the last_name of this Subscriber.  # noqa: E501


        :return: The last_name of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Subscriber.


        :param last_name: The last_name of this Subscriber.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def name(self):
        """Gets the name of this Subscriber.  # noqa: E501

        Full name of the contact. Will, if present, take precedence over first_name and last_name.  # noqa: E501

        :return: The name of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Subscriber.

        Full name of the contact. Will, if present, take precedence over first_name and last_name.  # noqa: E501

        :param name: The name of this Subscriber.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def subscribed(self):
        """Gets the subscribed of this Subscriber.  # noqa: E501


        :return: The subscribed of this Subscriber.  # noqa: E501
        :rtype: datetime
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """Sets the subscribed of this Subscriber.


        :param subscribed: The subscribed of this Subscriber.  # noqa: E501
        :type: datetime
        """

        self._subscribed = subscribed

    @property
    def tags(self):
        """Gets the tags of this Subscriber.  # noqa: E501


        :return: The tags of this Subscriber.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Subscriber.


        :param tags: The tags of this Subscriber.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(Subscriber, dict):
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
        if not isinstance(other, Subscriber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
