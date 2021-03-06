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
from mailmojo_sdk.api.segment_api import SegmentApi  # noqa: E501
from mailmojo_sdk.rest import ApiException


class TestSegmentApi(unittest.TestCase):
    """SegmentApi unit test stubs"""

    def setUp(self):
        self.api = mailmojo_sdk.api.segment_api.SegmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_segment(self):
        """Test case for create_segment

        Create a segment in the email list.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
