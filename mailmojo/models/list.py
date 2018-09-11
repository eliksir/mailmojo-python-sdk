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


class List(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, description=None, facebook=None, from_email=None, from_name=None, id=None, instagram=None, linkedin=None, name=None, subscribe_redirect_url=None, subscribe_url=None, twitter=None, unsubscribe_cascades=True, unsubscribe_redirect_url=None, unsubscribe_url=None, website=None):
        """
        List - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'description': 'str',
            'facebook': 'str',
            'from_email': 'str',
            'from_name': 'str',
            'id': 'int',
            'instagram': 'str',
            'linkedin': 'str',
            'name': 'str',
            'subscribe_redirect_url': 'str',
            'subscribe_url': 'str',
            'twitter': 'str',
            'unsubscribe_cascades': 'bool',
            'unsubscribe_redirect_url': 'str',
            'unsubscribe_url': 'str',
            'website': 'str'
        }

        self.attribute_map = {
            'created': 'created',
            'description': 'description',
            'facebook': 'facebook',
            'from_email': 'from_email',
            'from_name': 'from_name',
            'id': 'id',
            'instagram': 'instagram',
            'linkedin': 'linkedin',
            'name': 'name',
            'subscribe_redirect_url': 'subscribe_redirect_url',
            'subscribe_url': 'subscribe_url',
            'twitter': 'twitter',
            'unsubscribe_cascades': 'unsubscribe_cascades',
            'unsubscribe_redirect_url': 'unsubscribe_redirect_url',
            'unsubscribe_url': 'unsubscribe_url',
            'website': 'website'
        }

        self._created = created
        self._description = description
        self._facebook = facebook
        self._from_email = from_email
        self._from_name = from_name
        self._id = id
        self._instagram = instagram
        self._linkedin = linkedin
        self._name = name
        self._subscribe_redirect_url = subscribe_redirect_url
        self._subscribe_url = subscribe_url
        self._twitter = twitter
        self._unsubscribe_cascades = unsubscribe_cascades
        self._unsubscribe_redirect_url = unsubscribe_redirect_url
        self._unsubscribe_url = unsubscribe_url
        self._website = website

    @property
    def created(self):
        """
        Gets the created of this List.

        :return: The created of this List.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this List.

        :param created: The created of this List.
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """
        Gets the description of this List.

        :return: The description of this List.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this List.

        :param description: The description of this List.
        :type: str
        """

        self._description = description

    @property
    def facebook(self):
        """
        Gets the facebook of this List.

        :return: The facebook of this List.
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """
        Sets the facebook of this List.

        :param facebook: The facebook of this List.
        :type: str
        """

        self._facebook = facebook

    @property
    def from_email(self):
        """
        Gets the from_email of this List.

        :return: The from_email of this List.
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """
        Sets the from_email of this List.

        :param from_email: The from_email of this List.
        :type: str
        """
        if from_email is None:
            raise ValueError("Invalid value for `from_email`, must not be `None`")
        if from_email is not None and len(from_email) < 5:
            raise ValueError("Invalid value for `from_email`, length must be greater than or equal to `5`")

        self._from_email = from_email

    @property
    def from_name(self):
        """
        Gets the from_name of this List.

        :return: The from_name of this List.
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """
        Sets the from_name of this List.

        :param from_name: The from_name of this List.
        :type: str
        """
        if from_name is None:
            raise ValueError("Invalid value for `from_name`, must not be `None`")
        if from_name is not None and len(from_name) < 1:
            raise ValueError("Invalid value for `from_name`, length must be greater than or equal to `1`")

        self._from_name = from_name

    @property
    def id(self):
        """
        Gets the id of this List.

        :return: The id of this List.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this List.

        :param id: The id of this List.
        :type: int
        """

        self._id = id

    @property
    def instagram(self):
        """
        Gets the instagram of this List.

        :return: The instagram of this List.
        :rtype: str
        """
        return self._instagram

    @instagram.setter
    def instagram(self, instagram):
        """
        Sets the instagram of this List.

        :param instagram: The instagram of this List.
        :type: str
        """

        self._instagram = instagram

    @property
    def linkedin(self):
        """
        Gets the linkedin of this List.

        :return: The linkedin of this List.
        :rtype: str
        """
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        """
        Sets the linkedin of this List.

        :param linkedin: The linkedin of this List.
        :type: str
        """

        self._linkedin = linkedin

    @property
    def name(self):
        """
        Gets the name of this List.

        :return: The name of this List.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this List.

        :param name: The name of this List.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def subscribe_redirect_url(self):
        """
        Gets the subscribe_redirect_url of this List.

        :return: The subscribe_redirect_url of this List.
        :rtype: str
        """
        return self._subscribe_redirect_url

    @subscribe_redirect_url.setter
    def subscribe_redirect_url(self, subscribe_redirect_url):
        """
        Sets the subscribe_redirect_url of this List.

        :param subscribe_redirect_url: The subscribe_redirect_url of this List.
        :type: str
        """
        if subscribe_redirect_url is None:
            raise ValueError("Invalid value for `subscribe_redirect_url`, must not be `None`")

        self._subscribe_redirect_url = subscribe_redirect_url

    @property
    def subscribe_url(self):
        """
        Gets the subscribe_url of this List.

        :return: The subscribe_url of this List.
        :rtype: str
        """
        return self._subscribe_url

    @subscribe_url.setter
    def subscribe_url(self, subscribe_url):
        """
        Sets the subscribe_url of this List.

        :param subscribe_url: The subscribe_url of this List.
        :type: str
        """

        self._subscribe_url = subscribe_url

    @property
    def twitter(self):
        """
        Gets the twitter of this List.

        :return: The twitter of this List.
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """
        Sets the twitter of this List.

        :param twitter: The twitter of this List.
        :type: str
        """

        self._twitter = twitter

    @property
    def unsubscribe_cascades(self):
        """
        Gets the unsubscribe_cascades of this List.

        :return: The unsubscribe_cascades of this List.
        :rtype: bool
        """
        return self._unsubscribe_cascades

    @unsubscribe_cascades.setter
    def unsubscribe_cascades(self, unsubscribe_cascades):
        """
        Sets the unsubscribe_cascades of this List.

        :param unsubscribe_cascades: The unsubscribe_cascades of this List.
        :type: bool
        """

        self._unsubscribe_cascades = unsubscribe_cascades

    @property
    def unsubscribe_redirect_url(self):
        """
        Gets the unsubscribe_redirect_url of this List.

        :return: The unsubscribe_redirect_url of this List.
        :rtype: str
        """
        return self._unsubscribe_redirect_url

    @unsubscribe_redirect_url.setter
    def unsubscribe_redirect_url(self, unsubscribe_redirect_url):
        """
        Sets the unsubscribe_redirect_url of this List.

        :param unsubscribe_redirect_url: The unsubscribe_redirect_url of this List.
        :type: str
        """
        if unsubscribe_redirect_url is None:
            raise ValueError("Invalid value for `unsubscribe_redirect_url`, must not be `None`")

        self._unsubscribe_redirect_url = unsubscribe_redirect_url

    @property
    def unsubscribe_url(self):
        """
        Gets the unsubscribe_url of this List.

        :return: The unsubscribe_url of this List.
        :rtype: str
        """
        return self._unsubscribe_url

    @unsubscribe_url.setter
    def unsubscribe_url(self, unsubscribe_url):
        """
        Sets the unsubscribe_url of this List.

        :param unsubscribe_url: The unsubscribe_url of this List.
        :type: str
        """

        self._unsubscribe_url = unsubscribe_url

    @property
    def website(self):
        """
        Gets the website of this List.

        :return: The website of this List.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this List.

        :param website: The website of this List.
        :type: str
        """

        self._website = website

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
        if not isinstance(other, List):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
