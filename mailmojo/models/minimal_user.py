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


class MinimalUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email=None, logo_url=None, name=None, trial_days=None, username=None):
        """
        MinimalUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email': 'str',
            'logo_url': 'str',
            'name': 'str',
            'trial_days': 'int',
            'username': 'str'
        }

        self.attribute_map = {
            'email': 'email',
            'logo_url': 'logo_url',
            'name': 'name',
            'trial_days': 'trial_days',
            'username': 'username'
        }

        self._email = email
        self._logo_url = logo_url
        self._name = name
        self._trial_days = trial_days
        self._username = username

    @property
    def email(self):
        """
        Gets the email of this MinimalUser.

        :return: The email of this MinimalUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this MinimalUser.

        :param email: The email of this MinimalUser.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def logo_url(self):
        """
        Gets the logo_url of this MinimalUser.

        :return: The logo_url of this MinimalUser.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this MinimalUser.

        :param logo_url: The logo_url of this MinimalUser.
        :type: str
        """

        self._logo_url = logo_url

    @property
    def name(self):
        """
        Gets the name of this MinimalUser.

        :return: The name of this MinimalUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MinimalUser.

        :param name: The name of this MinimalUser.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def trial_days(self):
        """
        Gets the trial_days of this MinimalUser.

        :return: The trial_days of this MinimalUser.
        :rtype: int
        """
        return self._trial_days

    @trial_days.setter
    def trial_days(self, trial_days):
        """
        Sets the trial_days of this MinimalUser.

        :param trial_days: The trial_days of this MinimalUser.
        :type: int
        """

        self._trial_days = trial_days

    @property
    def username(self):
        """
        Gets the username of this MinimalUser.

        :return: The username of this MinimalUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this MinimalUser.

        :param username: The username of this MinimalUser.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")
        if username is not None and len(username) > 32:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `32`")
        if username is not None and len(username) < 4:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `4`")

        self._username = username

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
        if not isinstance(other, MinimalUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
