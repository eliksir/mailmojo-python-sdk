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

import mailmojo
from mailmojo.api.contacts_api import ContactsApi  # noqa: E501
from mailmojo.rest import ApiException


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self):
        self.api = mailmojo.api.contacts_api.ContactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_update_contact(self):
        """Test case for update_contact

        Update details about a contact.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
