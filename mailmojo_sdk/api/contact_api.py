# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailmojo_sdk.api_client import ApiClient


class ContactApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_contact_by_email(self, email, **kwargs):  # noqa: E501
        """Retrieve a contact in any list by email.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contact_by_email(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_contact_by_email_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.get_contact_by_email_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def get_contact_by_email_with_http_info(self, email, **kwargs):  # noqa: E501
        """Retrieve a contact in any list by email.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contact_by_email_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contact_by_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `get_contact_by_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/contacts/{email}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contact',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_contacts(self, **kwargs):  # noqa: E501
        """Retrieve all contacts across every list.  # noqa: E501

        This endpoint currently returns all contacts in your account *without any pagination* and should be considered EXPERIMENTAL. The response schema will change without any warning in the near future to account for pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contacts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Contact]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_contacts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_contacts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_contacts_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all contacts across every list.  # noqa: E501

        This endpoint currently returns all contacts in your account *without any pagination* and should be considered EXPERIMENTAL. The response schema will change without any warning in the near future to account for pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contacts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Contact]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contacts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/contacts/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Contact]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_historical_contact_stats(self, **kwargs):  # noqa: E501
        """Retrieve historical stats over contacts across every list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_historical_contact_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date start_date: The starting date to include stats from.
        :return: list[HistoricalContactsStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_historical_contact_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_historical_contact_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_historical_contact_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve historical stats over contacts across every list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_historical_contact_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date start_date: The starting date to include stats from.
        :return: list[HistoricalContactsStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_historical_contact_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/contacts/stats/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[HistoricalContactsStats]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subscriber_on_list_by_email(self, list_id, email, **kwargs):  # noqa: E501
        """Retrieve a subscriber.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscriber_on_list_by_email(list_id, email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list to retrieve the subscriber from. (required)
        :param str email: Email address of the contact to retrieve. (required)
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_subscriber_on_list_by_email_with_http_info(list_id, email, **kwargs)  # noqa: E501
        else:
            (data) = self.get_subscriber_on_list_by_email_with_http_info(list_id, email, **kwargs)  # noqa: E501
            return data

    def get_subscriber_on_list_by_email_with_http_info(self, list_id, email, **kwargs):  # noqa: E501
        """Retrieve a subscriber.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscriber_on_list_by_email_with_http_info(list_id, email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list to retrieve the subscriber from. (required)
        :param str email: Email address of the contact to retrieve. (required)
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscriber_on_list_by_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `get_subscriber_on_list_by_email`")  # noqa: E501
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `get_subscriber_on_list_by_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lists/{list_id}/subscribers/{email}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscriber',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subscribers_on_list(self, list_id, **kwargs):  # noqa: E501
        """Retrieve subscribers on a list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscribers_on_list(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list. (required)
        :param int limit: Limits the result to given count.
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_subscribers_on_list_with_http_info(list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_subscribers_on_list_with_http_info(list_id, **kwargs)  # noqa: E501
            return data

    def get_subscribers_on_list_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Retrieve subscribers on a list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscribers_on_list_with_http_info(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list. (required)
        :param int limit: Limits the result to given count.
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscribers_on_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `get_subscribers_on_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lists/{list_id}/subscribers/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Subscriber]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_unsubscribed_on_list(self, list_id, **kwargs):  # noqa: E501
        """Retrieve unsubscribed contacts on a list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unsubscribed_on_list(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list. (required)
        :param int limit: Limits the result to given count.
        :return: list[Contact]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_unsubscribed_on_list_with_http_info(list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_unsubscribed_on_list_with_http_info(list_id, **kwargs)  # noqa: E501
            return data

    def get_unsubscribed_on_list_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Retrieve unsubscribed contacts on a list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unsubscribed_on_list_with_http_info(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list. (required)
        :param int limit: Limits the result to given count.
        :return: list[Contact]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_unsubscribed_on_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `get_unsubscribed_on_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lists/{list_id}/unsubscribed/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Contact]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscribe_contact_to_list(self, list_id, contact, **kwargs):  # noqa: E501
        """Subscribe a contact to the email list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_contact_to_list(list_id, contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list to subscribe to. (required)
        :param Subscriber contact: (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subscribe_contact_to_list_with_http_info(list_id, contact, **kwargs)  # noqa: E501
        else:
            (data) = self.subscribe_contact_to_list_with_http_info(list_id, contact, **kwargs)  # noqa: E501
            return data

    def subscribe_contact_to_list_with_http_info(self, list_id, contact, **kwargs):  # noqa: E501
        """Subscribe a contact to the email list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_contact_to_list_with_http_info(list_id, contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list to subscribe to. (required)
        :param Subscriber contact: (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'contact']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscribe_contact_to_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `subscribe_contact_to_list`")  # noqa: E501
        # verify the required parameter 'contact' is set
        if ('contact' not in params or
                params['contact'] is None):
            raise ValueError("Missing the required parameter `contact` when calling `subscribe_contact_to_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact' in params:
            body_params = params['contact']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lists/{list_id}/subscribers/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contact',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unsubscribe_contact_on_list_by_email(self, list_id, email, **kwargs):  # noqa: E501
        """Unsubscribe a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsubscribe_contact_on_list_by_email(list_id, email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list to unsubscribe from. (required)
        :param str email: Email address of the contact to unsubscribe. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unsubscribe_contact_on_list_by_email_with_http_info(list_id, email, **kwargs)  # noqa: E501
        else:
            (data) = self.unsubscribe_contact_on_list_by_email_with_http_info(list_id, email, **kwargs)  # noqa: E501
            return data

    def unsubscribe_contact_on_list_by_email_with_http_info(self, list_id, email, **kwargs):  # noqa: E501
        """Unsubscribe a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsubscribe_contact_on_list_by_email_with_http_info(list_id, email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: ID of the email list to unsubscribe from. (required)
        :param str email: Email address of the contact to unsubscribe. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unsubscribe_contact_on_list_by_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `unsubscribe_contact_on_list_by_email`")  # noqa: E501
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `unsubscribe_contact_on_list_by_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lists/{list_id}/subscribers/{email}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contact',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_contact(self, email, **kwargs):  # noqa: E501
        """Update details about a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_contact(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: Email address of contact to update. (required)
        :param BaseContact contact:
        :return: BaseContact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_contact_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.update_contact_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def update_contact_with_http_info(self, email, **kwargs):  # noqa: E501
        """Update details about a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_contact_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: Email address of contact to update. (required)
        :param BaseContact contact:
        :return: BaseContact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email', 'contact']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `update_contact`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact' in params:
            body_params = params['contact']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/contacts/{email}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseContact',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
