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
from mailmojo_sdk.api.account_api import AccountApi  # noqa: E501
from mailmojo_sdk.rest import ApiException


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = mailmojo_sdk.api.account_api.AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_account(self):
        """Test case for create_account

        Create an account.  # noqa: E501
        """
        pass

    def test_get_account_by_username(self):
        """Test case for get_account_by_username

        Retrieve account details.  # noqa: E501
        """
        pass

    def test_get_domain(self):
        """Test case for get_domain

        Retrieve domain details and authentication status.  # noqa: E501
        """
        pass

    def test_update_account(self):
        """Test case for update_account

        Update account details.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
