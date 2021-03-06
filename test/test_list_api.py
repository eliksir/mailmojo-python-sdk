# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mailmojo_sdk
from mailmojo_sdk.api.list_api import ListApi  # noqa: E501
from mailmojo_sdk.rest import ApiException


class TestListApi(unittest.TestCase):
    """ListApi unit test stubs"""

    def setUp(self):
        self.api = mailmojo_sdk.api.list_api.ListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_list_by_id(self):
        """Test case for get_list_by_id

        Retrieve an email list.  # noqa: E501
        """
        pass

    def test_get_lists(self):
        """Test case for get_lists

        Retrieve all email lists.  # noqa: E501
        """
        pass

    def test_get_subscriber_on_list_by_email(self):
        """Test case for get_subscriber_on_list_by_email

        Retrieve a subscriber.  # noqa: E501
        """
        pass

    def test_get_subscribers_on_list(self):
        """Test case for get_subscribers_on_list

        Retrieve subscribers on a list.  # noqa: E501
        """
        pass

    def test_get_unsubscribed_on_list(self):
        """Test case for get_unsubscribed_on_list

        Retrieve unsubscribed contacts on a list.  # noqa: E501
        """
        pass

    def test_import_subscribers_to_list(self):
        """Test case for import_subscribers_to_list

        Subscribe contacts to the email list.  # noqa: E501
        """
        pass

    def test_subscribe_contact_to_list(self):
        """Test case for subscribe_contact_to_list

        Subscribe a contact to the email list.  # noqa: E501
        """
        pass

    def test_unsubscribe_contact_on_list_by_email(self):
        """Test case for unsubscribe_contact_on_list_by_email

        Unsubscribe a contact.  # noqa: E501
        """
        pass

    def test_update_list(self):
        """Test case for update_list

        Update an email list partially.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
