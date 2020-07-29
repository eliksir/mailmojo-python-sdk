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


class Form(object):
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
        'config': 'object',
        'confirmation_html': 'str',
        'created_at': 'datetime',
        'editor_confirmation_html': 'str',
        'editor_html': 'str',
        'expired_at': 'datetime',
        'fields': 'object',
        'final_confirmation_html': 'str',
        'final_html': 'str',
        'html': 'str',
        'id': 'int',
        'lid': 'int',
        'name': 'str',
        'published_at': 'datetime',
        'template_id': 'int',
        'type': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'config': 'config',
        'confirmation_html': 'confirmation_html',
        'created_at': 'created_at',
        'editor_confirmation_html': 'editor_confirmation_html',
        'editor_html': 'editor_html',
        'expired_at': 'expired_at',
        'fields': 'fields',
        'final_confirmation_html': 'final_confirmation_html',
        'final_html': 'final_html',
        'html': 'html',
        'id': 'id',
        'lid': 'lid',
        'name': 'name',
        'published_at': 'published_at',
        'template_id': 'template_id',
        'type': 'type',
        'updated_at': 'updated_at'
    }

    def __init__(self, config=None, confirmation_html=None, created_at=None, editor_confirmation_html=None, editor_html=None, expired_at=None, fields=None, final_confirmation_html=None, final_html=None, html=None, id=None, lid=None, name=None, published_at=None, template_id=None, type=None, updated_at=None):  # noqa: E501
        """Form - a model defined in Swagger"""  # noqa: E501

        self._config = None
        self._confirmation_html = None
        self._created_at = None
        self._editor_confirmation_html = None
        self._editor_html = None
        self._expired_at = None
        self._fields = None
        self._final_confirmation_html = None
        self._final_html = None
        self._html = None
        self._id = None
        self._lid = None
        self._name = None
        self._published_at = None
        self._template_id = None
        self._type = None
        self._updated_at = None
        self.discriminator = None

        self.config = config
        self.confirmation_html = confirmation_html
        if created_at is not None:
            self.created_at = created_at
        if editor_confirmation_html is not None:
            self.editor_confirmation_html = editor_confirmation_html
        if editor_html is not None:
            self.editor_html = editor_html
        if expired_at is not None:
            self.expired_at = expired_at
        self.fields = fields
        if final_confirmation_html is not None:
            self.final_confirmation_html = final_confirmation_html
        if final_html is not None:
            self.final_html = final_html
        self.html = html
        if id is not None:
            self.id = id
        self.lid = lid
        self.name = name
        if published_at is not None:
            self.published_at = published_at
        if template_id is not None:
            self.template_id = template_id
        self.type = type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def config(self):
        """Gets the config of this Form.  # noqa: E501


        :return: The config of this Form.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Form.


        :param config: The config of this Form.  # noqa: E501
        :type: object
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def confirmation_html(self):
        """Gets the confirmation_html of this Form.  # noqa: E501


        :return: The confirmation_html of this Form.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_html

    @confirmation_html.setter
    def confirmation_html(self, confirmation_html):
        """Sets the confirmation_html of this Form.


        :param confirmation_html: The confirmation_html of this Form.  # noqa: E501
        :type: str
        """
        if confirmation_html is None:
            raise ValueError("Invalid value for `confirmation_html`, must not be `None`")  # noqa: E501

        self._confirmation_html = confirmation_html

    @property
    def created_at(self):
        """Gets the created_at of this Form.  # noqa: E501


        :return: The created_at of this Form.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Form.


        :param created_at: The created_at of this Form.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def editor_confirmation_html(self):
        """Gets the editor_confirmation_html of this Form.  # noqa: E501


        :return: The editor_confirmation_html of this Form.  # noqa: E501
        :rtype: str
        """
        return self._editor_confirmation_html

    @editor_confirmation_html.setter
    def editor_confirmation_html(self, editor_confirmation_html):
        """Sets the editor_confirmation_html of this Form.


        :param editor_confirmation_html: The editor_confirmation_html of this Form.  # noqa: E501
        :type: str
        """

        self._editor_confirmation_html = editor_confirmation_html

    @property
    def editor_html(self):
        """Gets the editor_html of this Form.  # noqa: E501


        :return: The editor_html of this Form.  # noqa: E501
        :rtype: str
        """
        return self._editor_html

    @editor_html.setter
    def editor_html(self, editor_html):
        """Sets the editor_html of this Form.


        :param editor_html: The editor_html of this Form.  # noqa: E501
        :type: str
        """

        self._editor_html = editor_html

    @property
    def expired_at(self):
        """Gets the expired_at of this Form.  # noqa: E501


        :return: The expired_at of this Form.  # noqa: E501
        :rtype: datetime
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        """Sets the expired_at of this Form.


        :param expired_at: The expired_at of this Form.  # noqa: E501
        :type: datetime
        """

        self._expired_at = expired_at

    @property
    def fields(self):
        """Gets the fields of this Form.  # noqa: E501


        :return: The fields of this Form.  # noqa: E501
        :rtype: object
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Form.


        :param fields: The fields of this Form.  # noqa: E501
        :type: object
        """
        if fields is None:
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def final_confirmation_html(self):
        """Gets the final_confirmation_html of this Form.  # noqa: E501


        :return: The final_confirmation_html of this Form.  # noqa: E501
        :rtype: str
        """
        return self._final_confirmation_html

    @final_confirmation_html.setter
    def final_confirmation_html(self, final_confirmation_html):
        """Sets the final_confirmation_html of this Form.


        :param final_confirmation_html: The final_confirmation_html of this Form.  # noqa: E501
        :type: str
        """

        self._final_confirmation_html = final_confirmation_html

    @property
    def final_html(self):
        """Gets the final_html of this Form.  # noqa: E501


        :return: The final_html of this Form.  # noqa: E501
        :rtype: str
        """
        return self._final_html

    @final_html.setter
    def final_html(self, final_html):
        """Sets the final_html of this Form.


        :param final_html: The final_html of this Form.  # noqa: E501
        :type: str
        """

        self._final_html = final_html

    @property
    def html(self):
        """Gets the html of this Form.  # noqa: E501


        :return: The html of this Form.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this Form.


        :param html: The html of this Form.  # noqa: E501
        :type: str
        """
        if html is None:
            raise ValueError("Invalid value for `html`, must not be `None`")  # noqa: E501

        self._html = html

    @property
    def id(self):
        """Gets the id of this Form.  # noqa: E501


        :return: The id of this Form.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Form.


        :param id: The id of this Form.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lid(self):
        """Gets the lid of this Form.  # noqa: E501


        :return: The lid of this Form.  # noqa: E501
        :rtype: int
        """
        return self._lid

    @lid.setter
    def lid(self, lid):
        """Sets the lid of this Form.


        :param lid: The lid of this Form.  # noqa: E501
        :type: int
        """
        if lid is None:
            raise ValueError("Invalid value for `lid`, must not be `None`")  # noqa: E501

        self._lid = lid

    @property
    def name(self):
        """Gets the name of this Form.  # noqa: E501


        :return: The name of this Form.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Form.


        :param name: The name of this Form.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def published_at(self):
        """Gets the published_at of this Form.  # noqa: E501


        :return: The published_at of this Form.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this Form.


        :param published_at: The published_at of this Form.  # noqa: E501
        :type: datetime
        """

        self._published_at = published_at

    @property
    def template_id(self):
        """Gets the template_id of this Form.  # noqa: E501


        :return: The template_id of this Form.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this Form.


        :param template_id: The template_id of this Form.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def type(self):
        """Gets the type of this Form.  # noqa: E501


        :return: The type of this Form.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Form.


        :param type: The type of this Form.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["embedded", "subscribe", "subscribe_popup", "unsubscribe", "profile", "forward"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Form.  # noqa: E501


        :return: The updated_at of this Form.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Form.


        :param updated_at: The updated_at of this Form.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(Form, dict):
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
        if not isinstance(other, Form):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other