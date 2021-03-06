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


class Template(object):
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
        'campaign_expires_at': 'datetime',
        'campaign_price': 'float',
        'categories': 'list[Category]',
        'current_price': 'float',
        'data': 'object',
        'description': 'str',
        'id': 'int',
        'is_buyable': 'bool',
        'is_editable': 'bool',
        'is_on_sale': 'bool',
        'name': 'str',
        'preview_url': 'object',
        'price': 'float',
        'product_category': 'str',
        'product_description': 'str',
        'product_id': 'list[object]',
        'product_type': 'str',
        'screenshot_url': 'object',
        'settings': 'object',
        'total_price': 'float',
        'vat_amount': 'float'
    }

    attribute_map = {
        'campaign_expires_at': 'campaign_expires_at',
        'campaign_price': 'campaign_price',
        'categories': 'categories',
        'current_price': 'current_price',
        'data': 'data',
        'description': 'description',
        'id': 'id',
        'is_buyable': 'is_buyable',
        'is_editable': 'is_editable',
        'is_on_sale': 'is_on_sale',
        'name': 'name',
        'preview_url': 'preview_url',
        'price': 'price',
        'product_category': 'product_category',
        'product_description': 'product_description',
        'product_id': 'product_id',
        'product_type': 'product_type',
        'screenshot_url': 'screenshot_url',
        'settings': 'settings',
        'total_price': 'total_price',
        'vat_amount': 'vat_amount'
    }

    def __init__(self, campaign_expires_at=None, campaign_price=None, categories=None, current_price=None, data=None, description=None, id=None, is_buyable=None, is_editable=None, is_on_sale=None, name=None, preview_url=None, price=None, product_category=None, product_description=None, product_id=None, product_type=None, screenshot_url=None, settings=None, total_price=None, vat_amount=None):  # noqa: E501
        """Template - a model defined in Swagger"""  # noqa: E501

        self._campaign_expires_at = None
        self._campaign_price = None
        self._categories = None
        self._current_price = None
        self._data = None
        self._description = None
        self._id = None
        self._is_buyable = None
        self._is_editable = None
        self._is_on_sale = None
        self._name = None
        self._preview_url = None
        self._price = None
        self._product_category = None
        self._product_description = None
        self._product_id = None
        self._product_type = None
        self._screenshot_url = None
        self._settings = None
        self._total_price = None
        self._vat_amount = None
        self.discriminator = None

        if campaign_expires_at is not None:
            self.campaign_expires_at = campaign_expires_at
        if campaign_price is not None:
            self.campaign_price = campaign_price
        if categories is not None:
            self.categories = categories
        if current_price is not None:
            self.current_price = current_price
        if data is not None:
            self.data = data
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_buyable is not None:
            self.is_buyable = is_buyable
        if is_editable is not None:
            self.is_editable = is_editable
        if is_on_sale is not None:
            self.is_on_sale = is_on_sale
        if name is not None:
            self.name = name
        if preview_url is not None:
            self.preview_url = preview_url
        if price is not None:
            self.price = price
        if product_category is not None:
            self.product_category = product_category
        if product_description is not None:
            self.product_description = product_description
        if product_id is not None:
            self.product_id = product_id
        if product_type is not None:
            self.product_type = product_type
        if screenshot_url is not None:
            self.screenshot_url = screenshot_url
        if settings is not None:
            self.settings = settings
        if total_price is not None:
            self.total_price = total_price
        if vat_amount is not None:
            self.vat_amount = vat_amount

    @property
    def campaign_expires_at(self):
        """Gets the campaign_expires_at of this Template.  # noqa: E501


        :return: The campaign_expires_at of this Template.  # noqa: E501
        :rtype: datetime
        """
        return self._campaign_expires_at

    @campaign_expires_at.setter
    def campaign_expires_at(self, campaign_expires_at):
        """Sets the campaign_expires_at of this Template.


        :param campaign_expires_at: The campaign_expires_at of this Template.  # noqa: E501
        :type: datetime
        """

        self._campaign_expires_at = campaign_expires_at

    @property
    def campaign_price(self):
        """Gets the campaign_price of this Template.  # noqa: E501


        :return: The campaign_price of this Template.  # noqa: E501
        :rtype: float
        """
        return self._campaign_price

    @campaign_price.setter
    def campaign_price(self, campaign_price):
        """Sets the campaign_price of this Template.


        :param campaign_price: The campaign_price of this Template.  # noqa: E501
        :type: float
        """

        self._campaign_price = campaign_price

    @property
    def categories(self):
        """Gets the categories of this Template.  # noqa: E501


        :return: The categories of this Template.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Template.


        :param categories: The categories of this Template.  # noqa: E501
        :type: list[Category]
        """

        self._categories = categories

    @property
    def current_price(self):
        """Gets the current_price of this Template.  # noqa: E501


        :return: The current_price of this Template.  # noqa: E501
        :rtype: float
        """
        return self._current_price

    @current_price.setter
    def current_price(self, current_price):
        """Sets the current_price of this Template.


        :param current_price: The current_price of this Template.  # noqa: E501
        :type: float
        """

        self._current_price = current_price

    @property
    def data(self):
        """Gets the data of this Template.  # noqa: E501


        :return: The data of this Template.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Template.


        :param data: The data of this Template.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def description(self):
        """Gets the description of this Template.  # noqa: E501


        :return: The description of this Template.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Template.


        :param description: The description of this Template.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Template.  # noqa: E501


        :return: The id of this Template.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Template.


        :param id: The id of this Template.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_buyable(self):
        """Gets the is_buyable of this Template.  # noqa: E501


        :return: The is_buyable of this Template.  # noqa: E501
        :rtype: bool
        """
        return self._is_buyable

    @is_buyable.setter
    def is_buyable(self, is_buyable):
        """Sets the is_buyable of this Template.


        :param is_buyable: The is_buyable of this Template.  # noqa: E501
        :type: bool
        """

        self._is_buyable = is_buyable

    @property
    def is_editable(self):
        """Gets the is_editable of this Template.  # noqa: E501


        :return: The is_editable of this Template.  # noqa: E501
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """Sets the is_editable of this Template.


        :param is_editable: The is_editable of this Template.  # noqa: E501
        :type: bool
        """

        self._is_editable = is_editable

    @property
    def is_on_sale(self):
        """Gets the is_on_sale of this Template.  # noqa: E501


        :return: The is_on_sale of this Template.  # noqa: E501
        :rtype: bool
        """
        return self._is_on_sale

    @is_on_sale.setter
    def is_on_sale(self, is_on_sale):
        """Sets the is_on_sale of this Template.


        :param is_on_sale: The is_on_sale of this Template.  # noqa: E501
        :type: bool
        """

        self._is_on_sale = is_on_sale

    @property
    def name(self):
        """Gets the name of this Template.  # noqa: E501


        :return: The name of this Template.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Template.


        :param name: The name of this Template.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def preview_url(self):
        """Gets the preview_url of this Template.  # noqa: E501


        :return: The preview_url of this Template.  # noqa: E501
        :rtype: object
        """
        return self._preview_url

    @preview_url.setter
    def preview_url(self, preview_url):
        """Sets the preview_url of this Template.


        :param preview_url: The preview_url of this Template.  # noqa: E501
        :type: object
        """

        self._preview_url = preview_url

    @property
    def price(self):
        """Gets the price of this Template.  # noqa: E501


        :return: The price of this Template.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Template.


        :param price: The price of this Template.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def product_category(self):
        """Gets the product_category of this Template.  # noqa: E501


        :return: The product_category of this Template.  # noqa: E501
        :rtype: str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this Template.


        :param product_category: The product_category of this Template.  # noqa: E501
        :type: str
        """

        self._product_category = product_category

    @property
    def product_description(self):
        """Gets the product_description of this Template.  # noqa: E501


        :return: The product_description of this Template.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this Template.


        :param product_description: The product_description of this Template.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def product_id(self):
        """Gets the product_id of this Template.  # noqa: E501


        :return: The product_id of this Template.  # noqa: E501
        :rtype: list[object]
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Template.


        :param product_id: The product_id of this Template.  # noqa: E501
        :type: list[object]
        """

        self._product_id = product_id

    @property
    def product_type(self):
        """Gets the product_type of this Template.  # noqa: E501


        :return: The product_type of this Template.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this Template.


        :param product_type: The product_type of this Template.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def screenshot_url(self):
        """Gets the screenshot_url of this Template.  # noqa: E501


        :return: The screenshot_url of this Template.  # noqa: E501
        :rtype: object
        """
        return self._screenshot_url

    @screenshot_url.setter
    def screenshot_url(self, screenshot_url):
        """Sets the screenshot_url of this Template.


        :param screenshot_url: The screenshot_url of this Template.  # noqa: E501
        :type: object
        """

        self._screenshot_url = screenshot_url

    @property
    def settings(self):
        """Gets the settings of this Template.  # noqa: E501


        :return: The settings of this Template.  # noqa: E501
        :rtype: object
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Template.


        :param settings: The settings of this Template.  # noqa: E501
        :type: object
        """

        self._settings = settings

    @property
    def total_price(self):
        """Gets the total_price of this Template.  # noqa: E501


        :return: The total_price of this Template.  # noqa: E501
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this Template.


        :param total_price: The total_price of this Template.  # noqa: E501
        :type: float
        """

        self._total_price = total_price

    @property
    def vat_amount(self):
        """Gets the vat_amount of this Template.  # noqa: E501


        :return: The vat_amount of this Template.  # noqa: E501
        :rtype: float
        """
        return self._vat_amount

    @vat_amount.setter
    def vat_amount(self, vat_amount):
        """Sets the vat_amount of this Template.


        :param vat_amount: The vat_amount of this Template.  # noqa: E501
        :type: float
        """

        self._vat_amount = vat_amount

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
        if issubclass(Template, dict):
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
        if not isinstance(other, Template):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
