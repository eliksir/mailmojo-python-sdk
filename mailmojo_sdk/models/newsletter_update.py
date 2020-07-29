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


class NewsletterUpdate(object):
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
        'html': 'object',
        'html_url': 'str',
        'list_id': 'int',
        'segment_ids': 'list[object]',
        'subject': 'str',
        'template_id': 'int',
        'utm_campaign': 'str'
    }

    attribute_map = {
        'html': 'html',
        'html_url': 'html_url',
        'list_id': 'list_id',
        'segment_ids': 'segment_ids',
        'subject': 'subject',
        'template_id': 'template_id',
        'utm_campaign': 'utm_campaign'
    }

    def __init__(self, html=None, html_url=None, list_id=None, segment_ids=None, subject=None, template_id=None, utm_campaign=None):  # noqa: E501
        """NewsletterUpdate - a model defined in Swagger"""  # noqa: E501

        self._html = None
        self._html_url = None
        self._list_id = None
        self._segment_ids = None
        self._subject = None
        self._template_id = None
        self._utm_campaign = None
        self.discriminator = None

        if html is not None:
            self.html = html
        if html_url is not None:
            self.html_url = html_url
        self.list_id = list_id
        if segment_ids is not None:
            self.segment_ids = segment_ids
        if subject is not None:
            self.subject = subject
        if template_id is not None:
            self.template_id = template_id
        if utm_campaign is not None:
            self.utm_campaign = utm_campaign

    @property
    def html(self):
        """Gets the html of this NewsletterUpdate.  # noqa: E501


        :return: The html of this NewsletterUpdate.  # noqa: E501
        :rtype: object
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this NewsletterUpdate.


        :param html: The html of this NewsletterUpdate.  # noqa: E501
        :type: object
        """

        self._html = html

    @property
    def html_url(self):
        """Gets the html_url of this NewsletterUpdate.  # noqa: E501


        :return: The html_url of this NewsletterUpdate.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this NewsletterUpdate.


        :param html_url: The html_url of this NewsletterUpdate.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def list_id(self):
        """Gets the list_id of this NewsletterUpdate.  # noqa: E501


        :return: The list_id of this NewsletterUpdate.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this NewsletterUpdate.


        :param list_id: The list_id of this NewsletterUpdate.  # noqa: E501
        :type: int
        """
        if list_id is None:
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501

        self._list_id = list_id

    @property
    def segment_ids(self):
        """Gets the segment_ids of this NewsletterUpdate.  # noqa: E501


        :return: The segment_ids of this NewsletterUpdate.  # noqa: E501
        :rtype: list[object]
        """
        return self._segment_ids

    @segment_ids.setter
    def segment_ids(self, segment_ids):
        """Sets the segment_ids of this NewsletterUpdate.


        :param segment_ids: The segment_ids of this NewsletterUpdate.  # noqa: E501
        :type: list[object]
        """

        self._segment_ids = segment_ids

    @property
    def subject(self):
        """Gets the subject of this NewsletterUpdate.  # noqa: E501


        :return: The subject of this NewsletterUpdate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this NewsletterUpdate.


        :param subject: The subject of this NewsletterUpdate.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def template_id(self):
        """Gets the template_id of this NewsletterUpdate.  # noqa: E501


        :return: The template_id of this NewsletterUpdate.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this NewsletterUpdate.


        :param template_id: The template_id of this NewsletterUpdate.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def utm_campaign(self):
        """Gets the utm_campaign of this NewsletterUpdate.  # noqa: E501


        :return: The utm_campaign of this NewsletterUpdate.  # noqa: E501
        :rtype: str
        """
        return self._utm_campaign

    @utm_campaign.setter
    def utm_campaign(self, utm_campaign):
        """Sets the utm_campaign of this NewsletterUpdate.


        :param utm_campaign: The utm_campaign of this NewsletterUpdate.  # noqa: E501
        :type: str
        """

        self._utm_campaign = utm_campaign

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
        if issubclass(NewsletterUpdate, dict):
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
        if not isinstance(other, NewsletterUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
