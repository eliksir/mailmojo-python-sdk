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


class NewsletterDetail(object):
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
        'completed': 'datetime',
        'data': 'list[Schema]',
        'editor_html': 'str',
        'html': 'str',
        'id': 'int',
        'is_aborted': 'bool',
        'is_draft': 'bool',
        'is_in_campaign': 'bool',
        'is_scheduled': 'bool',
        'is_sending': 'bool',
        'is_sent': 'bool',
        'list': 'List',
        'meta': 'PageMeta',
        'num_recipients': 'int',
        'plain': 'str',
        'saved': 'datetime',
        'screenshot_url': 'object',
        'segments': 'list[MinimalSegment]',
        'started': 'datetime',
        'statistics': 'Statistics',
        'subject': 'str',
        'template_id': 'int',
        'utm_campaign': 'str',
        'view_url': 'object'
    }

    attribute_map = {
        'completed': 'completed',
        'data': 'data',
        'editor_html': 'editor_html',
        'html': 'html',
        'id': 'id',
        'is_aborted': 'is_aborted',
        'is_draft': 'is_draft',
        'is_in_campaign': 'is_in_campaign',
        'is_scheduled': 'is_scheduled',
        'is_sending': 'is_sending',
        'is_sent': 'is_sent',
        'list': 'list',
        'meta': 'meta',
        'num_recipients': 'num_recipients',
        'plain': 'plain',
        'saved': 'saved',
        'screenshot_url': 'screenshot_url',
        'segments': 'segments',
        'started': 'started',
        'statistics': 'statistics',
        'subject': 'subject',
        'template_id': 'template_id',
        'utm_campaign': 'utm_campaign',
        'view_url': 'view_url'
    }

    def __init__(self, completed=None, data=None, editor_html=None, html=None, id=None, is_aborted=None, is_draft=None, is_in_campaign=None, is_scheduled=None, is_sending=None, is_sent=None, list=None, meta=None, num_recipients=None, plain=None, saved=None, screenshot_url=None, segments=None, started=None, statistics=None, subject=None, template_id=None, utm_campaign=None, view_url=None):  # noqa: E501
        """NewsletterDetail - a model defined in Swagger"""  # noqa: E501

        self._completed = None
        self._data = None
        self._editor_html = None
        self._html = None
        self._id = None
        self._is_aborted = None
        self._is_draft = None
        self._is_in_campaign = None
        self._is_scheduled = None
        self._is_sending = None
        self._is_sent = None
        self._list = None
        self._meta = None
        self._num_recipients = None
        self._plain = None
        self._saved = None
        self._screenshot_url = None
        self._segments = None
        self._started = None
        self._statistics = None
        self._subject = None
        self._template_id = None
        self._utm_campaign = None
        self._view_url = None
        self.discriminator = None

        if completed is not None:
            self.completed = completed
        if data is not None:
            self.data = data
        if editor_html is not None:
            self.editor_html = editor_html
        if html is not None:
            self.html = html
        if id is not None:
            self.id = id
        if is_aborted is not None:
            self.is_aborted = is_aborted
        if is_draft is not None:
            self.is_draft = is_draft
        if is_in_campaign is not None:
            self.is_in_campaign = is_in_campaign
        if is_scheduled is not None:
            self.is_scheduled = is_scheduled
        if is_sending is not None:
            self.is_sending = is_sending
        if is_sent is not None:
            self.is_sent = is_sent
        if list is not None:
            self.list = list
        if meta is not None:
            self.meta = meta
        if num_recipients is not None:
            self.num_recipients = num_recipients
        if plain is not None:
            self.plain = plain
        if saved is not None:
            self.saved = saved
        if screenshot_url is not None:
            self.screenshot_url = screenshot_url
        if segments is not None:
            self.segments = segments
        if started is not None:
            self.started = started
        if statistics is not None:
            self.statistics = statistics
        if subject is not None:
            self.subject = subject
        if template_id is not None:
            self.template_id = template_id
        if utm_campaign is not None:
            self.utm_campaign = utm_campaign
        if view_url is not None:
            self.view_url = view_url

    @property
    def completed(self):
        """Gets the completed of this NewsletterDetail.  # noqa: E501


        :return: The completed of this NewsletterDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this NewsletterDetail.


        :param completed: The completed of this NewsletterDetail.  # noqa: E501
        :type: datetime
        """

        self._completed = completed

    @property
    def data(self):
        """Gets the data of this NewsletterDetail.  # noqa: E501


        :return: The data of this NewsletterDetail.  # noqa: E501
        :rtype: list[Schema]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this NewsletterDetail.


        :param data: The data of this NewsletterDetail.  # noqa: E501
        :type: list[Schema]
        """

        self._data = data

    @property
    def editor_html(self):
        """Gets the editor_html of this NewsletterDetail.  # noqa: E501


        :return: The editor_html of this NewsletterDetail.  # noqa: E501
        :rtype: str
        """
        return self._editor_html

    @editor_html.setter
    def editor_html(self, editor_html):
        """Sets the editor_html of this NewsletterDetail.


        :param editor_html: The editor_html of this NewsletterDetail.  # noqa: E501
        :type: str
        """

        self._editor_html = editor_html

    @property
    def html(self):
        """Gets the html of this NewsletterDetail.  # noqa: E501


        :return: The html of this NewsletterDetail.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this NewsletterDetail.


        :param html: The html of this NewsletterDetail.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def id(self):
        """Gets the id of this NewsletterDetail.  # noqa: E501


        :return: The id of this NewsletterDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewsletterDetail.


        :param id: The id of this NewsletterDetail.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_aborted(self):
        """Gets the is_aborted of this NewsletterDetail.  # noqa: E501


        :return: The is_aborted of this NewsletterDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_aborted

    @is_aborted.setter
    def is_aborted(self, is_aborted):
        """Sets the is_aborted of this NewsletterDetail.


        :param is_aborted: The is_aborted of this NewsletterDetail.  # noqa: E501
        :type: bool
        """

        self._is_aborted = is_aborted

    @property
    def is_draft(self):
        """Gets the is_draft of this NewsletterDetail.  # noqa: E501


        :return: The is_draft of this NewsletterDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_draft

    @is_draft.setter
    def is_draft(self, is_draft):
        """Sets the is_draft of this NewsletterDetail.


        :param is_draft: The is_draft of this NewsletterDetail.  # noqa: E501
        :type: bool
        """

        self._is_draft = is_draft

    @property
    def is_in_campaign(self):
        """Gets the is_in_campaign of this NewsletterDetail.  # noqa: E501


        :return: The is_in_campaign of this NewsletterDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_campaign

    @is_in_campaign.setter
    def is_in_campaign(self, is_in_campaign):
        """Sets the is_in_campaign of this NewsletterDetail.


        :param is_in_campaign: The is_in_campaign of this NewsletterDetail.  # noqa: E501
        :type: bool
        """

        self._is_in_campaign = is_in_campaign

    @property
    def is_scheduled(self):
        """Gets the is_scheduled of this NewsletterDetail.  # noqa: E501


        :return: The is_scheduled of this NewsletterDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_scheduled

    @is_scheduled.setter
    def is_scheduled(self, is_scheduled):
        """Sets the is_scheduled of this NewsletterDetail.


        :param is_scheduled: The is_scheduled of this NewsletterDetail.  # noqa: E501
        :type: bool
        """

        self._is_scheduled = is_scheduled

    @property
    def is_sending(self):
        """Gets the is_sending of this NewsletterDetail.  # noqa: E501


        :return: The is_sending of this NewsletterDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_sending

    @is_sending.setter
    def is_sending(self, is_sending):
        """Sets the is_sending of this NewsletterDetail.


        :param is_sending: The is_sending of this NewsletterDetail.  # noqa: E501
        :type: bool
        """

        self._is_sending = is_sending

    @property
    def is_sent(self):
        """Gets the is_sent of this NewsletterDetail.  # noqa: E501


        :return: The is_sent of this NewsletterDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_sent

    @is_sent.setter
    def is_sent(self, is_sent):
        """Sets the is_sent of this NewsletterDetail.


        :param is_sent: The is_sent of this NewsletterDetail.  # noqa: E501
        :type: bool
        """

        self._is_sent = is_sent

    @property
    def list(self):
        """Gets the list of this NewsletterDetail.  # noqa: E501


        :return: The list of this NewsletterDetail.  # noqa: E501
        :rtype: List
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this NewsletterDetail.


        :param list: The list of this NewsletterDetail.  # noqa: E501
        :type: List
        """

        self._list = list

    @property
    def meta(self):
        """Gets the meta of this NewsletterDetail.  # noqa: E501


        :return: The meta of this NewsletterDetail.  # noqa: E501
        :rtype: PageMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this NewsletterDetail.


        :param meta: The meta of this NewsletterDetail.  # noqa: E501
        :type: PageMeta
        """

        self._meta = meta

    @property
    def num_recipients(self):
        """Gets the num_recipients of this NewsletterDetail.  # noqa: E501


        :return: The num_recipients of this NewsletterDetail.  # noqa: E501
        :rtype: int
        """
        return self._num_recipients

    @num_recipients.setter
    def num_recipients(self, num_recipients):
        """Sets the num_recipients of this NewsletterDetail.


        :param num_recipients: The num_recipients of this NewsletterDetail.  # noqa: E501
        :type: int
        """

        self._num_recipients = num_recipients

    @property
    def plain(self):
        """Gets the plain of this NewsletterDetail.  # noqa: E501


        :return: The plain of this NewsletterDetail.  # noqa: E501
        :rtype: str
        """
        return self._plain

    @plain.setter
    def plain(self, plain):
        """Sets the plain of this NewsletterDetail.


        :param plain: The plain of this NewsletterDetail.  # noqa: E501
        :type: str
        """

        self._plain = plain

    @property
    def saved(self):
        """Gets the saved of this NewsletterDetail.  # noqa: E501


        :return: The saved of this NewsletterDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._saved

    @saved.setter
    def saved(self, saved):
        """Sets the saved of this NewsletterDetail.


        :param saved: The saved of this NewsletterDetail.  # noqa: E501
        :type: datetime
        """

        self._saved = saved

    @property
    def screenshot_url(self):
        """Gets the screenshot_url of this NewsletterDetail.  # noqa: E501


        :return: The screenshot_url of this NewsletterDetail.  # noqa: E501
        :rtype: object
        """
        return self._screenshot_url

    @screenshot_url.setter
    def screenshot_url(self, screenshot_url):
        """Sets the screenshot_url of this NewsletterDetail.


        :param screenshot_url: The screenshot_url of this NewsletterDetail.  # noqa: E501
        :type: object
        """

        self._screenshot_url = screenshot_url

    @property
    def segments(self):
        """Gets the segments of this NewsletterDetail.  # noqa: E501


        :return: The segments of this NewsletterDetail.  # noqa: E501
        :rtype: list[MinimalSegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this NewsletterDetail.


        :param segments: The segments of this NewsletterDetail.  # noqa: E501
        :type: list[MinimalSegment]
        """

        self._segments = segments

    @property
    def started(self):
        """Gets the started of this NewsletterDetail.  # noqa: E501


        :return: The started of this NewsletterDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this NewsletterDetail.


        :param started: The started of this NewsletterDetail.  # noqa: E501
        :type: datetime
        """

        self._started = started

    @property
    def statistics(self):
        """Gets the statistics of this NewsletterDetail.  # noqa: E501


        :return: The statistics of this NewsletterDetail.  # noqa: E501
        :rtype: Statistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this NewsletterDetail.


        :param statistics: The statistics of this NewsletterDetail.  # noqa: E501
        :type: Statistics
        """

        self._statistics = statistics

    @property
    def subject(self):
        """Gets the subject of this NewsletterDetail.  # noqa: E501


        :return: The subject of this NewsletterDetail.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this NewsletterDetail.


        :param subject: The subject of this NewsletterDetail.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def template_id(self):
        """Gets the template_id of this NewsletterDetail.  # noqa: E501


        :return: The template_id of this NewsletterDetail.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this NewsletterDetail.


        :param template_id: The template_id of this NewsletterDetail.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def utm_campaign(self):
        """Gets the utm_campaign of this NewsletterDetail.  # noqa: E501


        :return: The utm_campaign of this NewsletterDetail.  # noqa: E501
        :rtype: str
        """
        return self._utm_campaign

    @utm_campaign.setter
    def utm_campaign(self, utm_campaign):
        """Sets the utm_campaign of this NewsletterDetail.


        :param utm_campaign: The utm_campaign of this NewsletterDetail.  # noqa: E501
        :type: str
        """

        self._utm_campaign = utm_campaign

    @property
    def view_url(self):
        """Gets the view_url of this NewsletterDetail.  # noqa: E501


        :return: The view_url of this NewsletterDetail.  # noqa: E501
        :rtype: object
        """
        return self._view_url

    @view_url.setter
    def view_url(self, view_url):
        """Sets the view_url of this NewsletterDetail.


        :param view_url: The view_url of this NewsletterDetail.  # noqa: E501
        :type: object
        """

        self._view_url = view_url

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
        if issubclass(NewsletterDetail, dict):
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
        if not isinstance(other, NewsletterDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other