# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API

    OpenAPI spec version: 1.0.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ContactListAssociations(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, added=None, email=None, list_id=None, status=None, status_changed=None):
        """
        ContactListAssociations - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'added': 'datetime',
            'email': 'str',
            'list_id': 'int',
            'status': 'str',
            'status_changed': 'datetime'
        }

        self.attribute_map = {
            'added': 'added',
            'email': 'email',
            'list_id': 'list_id',
            'status': 'status',
            'status_changed': 'status_changed'
        }

        self._added = added
        self._email = email
        self._list_id = list_id
        self._status = status
        self._status_changed = status_changed

    @property
    def added(self):
        """
        Gets the added of this ContactListAssociations.


        :return: The added of this ContactListAssociations.
        :rtype: datetime
        """
        return self._added

    @added.setter
    def added(self, added):
        """
        Sets the added of this ContactListAssociations.


        :param added: The added of this ContactListAssociations.
        :type: datetime
        """

        self._added = added

    @property
    def email(self):
        """
        Gets the email of this ContactListAssociations.


        :return: The email of this ContactListAssociations.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ContactListAssociations.


        :param email: The email of this ContactListAssociations.
        :type: str
        """

        self._email = email

    @property
    def list_id(self):
        """
        Gets the list_id of this ContactListAssociations.


        :return: The list_id of this ContactListAssociations.
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """
        Sets the list_id of this ContactListAssociations.


        :param list_id: The list_id of this ContactListAssociations.
        :type: int
        """

        self._list_id = list_id

    @property
    def status(self):
        """
        Gets the status of this ContactListAssociations.


        :return: The status of this ContactListAssociations.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ContactListAssociations.


        :param status: The status of this ContactListAssociations.
        :type: str
        """
        allowed_values = ["b", "d", "a", "u"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_changed(self):
        """
        Gets the status_changed of this ContactListAssociations.


        :return: The status_changed of this ContactListAssociations.
        :rtype: datetime
        """
        return self._status_changed

    @status_changed.setter
    def status_changed(self, status_changed):
        """
        Sets the status_changed of this ContactListAssociations.


        :param status_changed: The status_changed of this ContactListAssociations.
        :type: datetime
        """

        self._status_changed = status_changed

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
