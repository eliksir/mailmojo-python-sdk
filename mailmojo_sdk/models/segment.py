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


class Segment(object):
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
        'created': 'datetime',
        'id': 'int',
        'label': 'str',
        'name': 'str',
        'num_contacts': 'int',
        'type': 'object'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'label': 'label',
        'name': 'name',
        'num_contacts': 'num_contacts',
        'type': 'type'
    }

    def __init__(self, created=None, id=None, label=None, name=None, num_contacts=None, type=None):  # noqa: E501
        """Segment - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._id = None
        self._label = None
        self._name = None
        self._num_contacts = None
        self._type = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        self.name = name
        if num_contacts is not None:
            self.num_contacts = num_contacts
        if type is not None:
            self.type = type

    @property
    def created(self):
        """Gets the created of this Segment.  # noqa: E501


        :return: The created of this Segment.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Segment.


        :param created: The created of this Segment.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this Segment.  # noqa: E501


        :return: The id of this Segment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Segment.


        :param id: The id of this Segment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Segment.  # noqa: E501


        :return: The label of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Segment.


        :param label: The label of this Segment.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this Segment.  # noqa: E501


        :return: The name of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Segment.


        :param name: The name of this Segment.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def num_contacts(self):
        """Gets the num_contacts of this Segment.  # noqa: E501


        :return: The num_contacts of this Segment.  # noqa: E501
        :rtype: int
        """
        return self._num_contacts

    @num_contacts.setter
    def num_contacts(self, num_contacts):
        """Sets the num_contacts of this Segment.


        :param num_contacts: The num_contacts of this Segment.  # noqa: E501
        :type: int
        """

        self._num_contacts = num_contacts

    @property
    def type(self):
        """Gets the type of this Segment.  # noqa: E501


        :return: The type of this Segment.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Segment.


        :param type: The type of this Segment.  # noqa: E501
        :type: object
        """

        self._type = type

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
        if issubclass(Segment, dict):
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
        if not isinstance(other, Segment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
