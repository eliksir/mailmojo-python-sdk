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


class AccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_account(self, user, **kwargs):  # noqa: E501
        """Create an account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_account(user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCreation user: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_account_with_http_info(user, **kwargs)  # noqa: E501
        else:
            (data) = self.create_account_with_http_info(user, **kwargs)  # noqa: E501
            return data

    def create_account_with_http_info(self, user, **kwargs):  # noqa: E501
        """Create an account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_account_with_http_info(user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCreation user: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in params or
                params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `create_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user' in params:
            body_params = params['user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/accounts/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account_by_username(self, username, **kwargs):  # noqa: E501
        """Retrieve account details.  # noqa: E501

        This endpoint can be used to get details about your own account, or a subuser associated with you as a partner. If the username of your current authenticated user is unknown, you may use the special username 'me' to retrieve details about the authenticated user account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_by_username(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username of the account to get details for, or the special username `me` to get details about your authenticated user. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_account_by_username_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.get_account_by_username_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def get_account_by_username_with_http_info(self, username, **kwargs):  # noqa: E501
        """Retrieve account details.  # noqa: E501

        This endpoint can be used to get details about your own account, or a subuser associated with you as a partner. If the username of your current authenticated user is unknown, you may use the special username 'me' to retrieve details about the authenticated user account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_by_username_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username of the account to get details for, or the special username `me` to get details about your authenticated user. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_by_username" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `get_account_by_username`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

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
            '/v1/accounts/{username}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_domain(self, domain, **kwargs):  # noqa: E501
        """Retrieve domain details and authentication status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_domain(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_domain_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_domain_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def get_domain_with_http_info(self, domain, **kwargs):  # noqa: E501
        """Retrieve domain details and authentication status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_domain_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501

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
            '/v1/domains/{domain}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Domain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_account(self, username, **kwargs):  # noqa: E501
        """Update account details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_account(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username of the user to update. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_account_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.update_account_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def update_account_with_http_info(self, username, **kwargs):  # noqa: E501
        """Update account details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_account_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username of the user to update. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `update_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

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
            '/v1/accounts/{username}/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
