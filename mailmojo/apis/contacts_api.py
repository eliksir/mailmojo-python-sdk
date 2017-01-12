# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API

    OpenAPI spec version: 1.0.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ContactsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_contacts(self, **kwargs):
        """
        Retrieve all contacts across every list.
        This endpoint currently returns all contacts in your account *without any pagination* and should be considered EXPERIMENTAL. The response schema will change without any warning in the near future to account for pagination. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contacts(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Contact]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_contacts_with_http_info(**kwargs)
        else:
            (data) = self.get_contacts_with_http_info(**kwargs)
            return data

    def get_contacts_with_http_info(self, **kwargs):
        """
        Retrieve all contacts across every list.
        This endpoint currently returns all contacts in your account *without any pagination* and should be considered EXPERIMENTAL. The response schema will change without any warning in the near future to account for pagination. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contacts_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Contact]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contacts" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/contacts/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['mailmojo_auth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Contact]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_subscriber_on_list_by_email(self, list_id, email, **kwargs):
        """
        Retrieve a subscriber.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscriber_on_list_by_email(list_id, email, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list to retrieve the subscriber from.  (required)
        :param str email: Email address of the contact to retrieve. (required)
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscriber_on_list_by_email_with_http_info(list_id, email, **kwargs)
        else:
            (data) = self.get_subscriber_on_list_by_email_with_http_info(list_id, email, **kwargs)
            return data

    def get_subscriber_on_list_by_email_with_http_info(self, list_id, email, **kwargs):
        """
        Retrieve a subscriber.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscriber_on_list_by_email_with_http_info(list_id, email, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list to retrieve the subscriber from.  (required)
        :param str email: Email address of the contact to retrieve. (required)
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'email']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscriber_on_list_by_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `get_subscriber_on_list_by_email`")
        # verify the required parameter 'email' is set
        if ('email' not in params) or (params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `get_subscriber_on_list_by_email`")

        resource_path = '/lists/{list_id}/subscribers/{email}/'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']
        if 'email' in params:
            path_params['email'] = params['email']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['mailmojo_auth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Subscriber]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_subscribers_on_list(self, list_id, **kwargs):
        """
        Retrieve subscribers on a list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscribers_on_list(list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list. (required)
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscribers_on_list_with_http_info(list_id, **kwargs)
        else:
            (data) = self.get_subscribers_on_list_with_http_info(list_id, **kwargs)
            return data

    def get_subscribers_on_list_with_http_info(self, list_id, **kwargs):
        """
        Retrieve subscribers on a list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscribers_on_list_with_http_info(list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list. (required)
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscribers_on_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `get_subscribers_on_list`")

        resource_path = '/lists/{list_id}/subscribers/'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['mailmojo_auth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Subscriber]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def import_subscribers_to_list(self, list_id, **kwargs):
        """
        Subscribe contacts to the email list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_subscribers_to_list(list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list to subscribe to. (required)
        :param list[Contacts] contacts: 
        :return: ImportResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.import_subscribers_to_list_with_http_info(list_id, **kwargs)
        else:
            (data) = self.import_subscribers_to_list_with_http_info(list_id, **kwargs)
            return data

    def import_subscribers_to_list_with_http_info(self, list_id, **kwargs):
        """
        Subscribe contacts to the email list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_subscribers_to_list_with_http_info(list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list to subscribe to. (required)
        :param list[Contacts] contacts: 
        :return: ImportResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'contacts']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_subscribers_to_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `import_subscribers_to_list`")

        resource_path = '/lists/{list_id}/subscribers/import/'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contacts' in params:
            body_params = params['contacts']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/csv'])

        # Authentication setting
        auth_settings = ['mailmojo_auth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ImportResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def subscribe_contact_to_list(self, list_id, **kwargs):
        """
        Subscribe a contact to the email list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscribe_contact_to_list(list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list to subscribe to. (required)
        :param Contact contact: 
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.subscribe_contact_to_list_with_http_info(list_id, **kwargs)
        else:
            (data) = self.subscribe_contact_to_list_with_http_info(list_id, **kwargs)
            return data

    def subscribe_contact_to_list_with_http_info(self, list_id, **kwargs):
        """
        Subscribe a contact to the email list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscribe_contact_to_list_with_http_info(list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list to subscribe to. (required)
        :param Contact contact: 
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'contact']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscribe_contact_to_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `subscribe_contact_to_list`")

        resource_path = '/lists/{list_id}/subscribers/'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact' in params:
            body_params = params['contact']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['mailmojo_auth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Contact',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def unsubscribe_contact_on_list_by_email(self, list_id, email, **kwargs):
        """
        Unsubscribe a contact.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unsubscribe_contact_on_list_by_email(list_id, email, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list to unsubscribe from. (required)
        :param str email: Email address of the contact to unsubscribe. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.unsubscribe_contact_on_list_by_email_with_http_info(list_id, email, **kwargs)
        else:
            (data) = self.unsubscribe_contact_on_list_by_email_with_http_info(list_id, email, **kwargs)
            return data

    def unsubscribe_contact_on_list_by_email_with_http_info(self, list_id, email, **kwargs):
        """
        Unsubscribe a contact.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unsubscribe_contact_on_list_by_email_with_http_info(list_id, email, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int list_id: ID of the email list to unsubscribe from. (required)
        :param str email: Email address of the contact to unsubscribe. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'email']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unsubscribe_contact_on_list_by_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `unsubscribe_contact_on_list_by_email`")
        # verify the required parameter 'email' is set
        if ('email' not in params) or (params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `unsubscribe_contact_on_list_by_email`")

        resource_path = '/lists/{list_id}/subscribers/{email}/'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']
        if 'email' in params:
            path_params['email'] = params['email']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['mailmojo_auth']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Contact',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
