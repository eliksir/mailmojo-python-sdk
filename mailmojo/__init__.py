# coding: utf-8

# flake8: noqa

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from mailmojo.api.accounts_api import AccountsApi
from mailmojo.api.automation_api import AutomationApi
from mailmojo.api.campaign_api import CampaignApi
from mailmojo.api.contacts_api import ContactsApi
from mailmojo.api.embed_api import EmbedApi
from mailmojo.api.lists_api import ListsApi
from mailmojo.api.newsletter_api import NewsletterApi

# import ApiClient
from mailmojo.api_client import ApiClient
from mailmojo.configuration import Configuration
# import models into sdk package
from mailmojo.models.campaign_detail import CampaignDetail
from mailmojo.models.campaign_detail_statistics import CampaignDetailStatistics
from mailmojo.models.contact import Contact
from mailmojo.models.contact_list_associations import ContactListAssociations
from mailmojo.models.contacts import Contacts
from mailmojo.models.embed import Embed
from mailmojo.models.embed_options import EmbedOptions
from mailmojo.models.import_result import ImportResult
from mailmojo.models.inline_response200 import InlineResponse200
from mailmojo.models.list import List
from mailmojo.models.minimal_contact import MinimalContact
from mailmojo.models.minimal_user import MinimalUser
from mailmojo.models.newsletter import Newsletter
from mailmojo.models.newsletter_creation import NewsletterCreation
from mailmojo.models.newsletter_segments import NewsletterSegments
from mailmojo.models.newsletter_send import NewsletterSend
from mailmojo.models.newsletter_send_test import NewsletterSendTest
from mailmojo.models.newsletter_statistics import NewsletterStatistics
from mailmojo.models.page_meta import PageMeta
from mailmojo.models.subscriber import Subscriber
from mailmojo.models.user import User
