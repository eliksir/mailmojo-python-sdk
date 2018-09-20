# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NewsletterStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bounce_rate=None, click_rate=None, num_shares=None, open_rate=None):
        """
        NewsletterStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bounce_rate': 'float',
            'click_rate': 'float',
            'num_shares': 'int',
            'open_rate': 'float'
        }

        self.attribute_map = {
            'bounce_rate': 'bounce_rate',
            'click_rate': 'click_rate',
            'num_shares': 'num_shares',
            'open_rate': 'open_rate'
        }

        self._bounce_rate = bounce_rate
        self._click_rate = click_rate
        self._num_shares = num_shares
        self._open_rate = open_rate

    @property
    def bounce_rate(self):
        """
        Gets the bounce_rate of this NewsletterStatistics.

        :return: The bounce_rate of this NewsletterStatistics.
        :rtype: float
        """
        return self._bounce_rate

    @bounce_rate.setter
    def bounce_rate(self, bounce_rate):
        """
        Sets the bounce_rate of this NewsletterStatistics.

        :param bounce_rate: The bounce_rate of this NewsletterStatistics.
        :type: float
        """

        self._bounce_rate = bounce_rate

    @property
    def click_rate(self):
        """
        Gets the click_rate of this NewsletterStatistics.

        :return: The click_rate of this NewsletterStatistics.
        :rtype: float
        """
        return self._click_rate

    @click_rate.setter
    def click_rate(self, click_rate):
        """
        Sets the click_rate of this NewsletterStatistics.

        :param click_rate: The click_rate of this NewsletterStatistics.
        :type: float
        """

        self._click_rate = click_rate

    @property
    def num_shares(self):
        """
        Gets the num_shares of this NewsletterStatistics.

        :return: The num_shares of this NewsletterStatistics.
        :rtype: int
        """
        return self._num_shares

    @num_shares.setter
    def num_shares(self, num_shares):
        """
        Sets the num_shares of this NewsletterStatistics.

        :param num_shares: The num_shares of this NewsletterStatistics.
        :type: int
        """

        self._num_shares = num_shares

    @property
    def open_rate(self):
        """
        Gets the open_rate of this NewsletterStatistics.

        :return: The open_rate of this NewsletterStatistics.
        :rtype: float
        """
        return self._open_rate

    @open_rate.setter
    def open_rate(self, open_rate):
        """
        Sets the open_rate of this NewsletterStatistics.

        :param open_rate: The open_rate of this NewsletterStatistics.
        :type: float
        """

        self._open_rate = open_rate

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
        if not isinstance(other, NewsletterStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
