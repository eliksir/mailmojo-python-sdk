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
from mailmojo_sdk.api.template_api import TemplateApi  # noqa: E501
from mailmojo_sdk.rest import ApiException


class TestTemplateApi(unittest.TestCase):
    """TemplateApi unit test stubs"""

    def setUp(self):
        self.api = mailmojo_sdk.api.template_api.TemplateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_templates(self):
        """Test case for get_templates

        Retrieve all templates.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
