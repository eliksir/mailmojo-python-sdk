MailMojo SDK for Python
=======================
v1 of the MailMojo API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 0.1.0
- Build date: 2017-01-12T11:06:02.142+01:00

For more information, please visit [https://mailmojo.gelato.io](https://mailmojo.gelato.io)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/eliksir/mailmojo-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/eliksir/mailmojo-python-sdk.git`)

Then import the package:
```python
import mailmojo
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mailmojo
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mailmojo
from mailmojo.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: mailmojo_auth
mailmojo.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = mailmojo.ListsApi()
list_id = 56 # int | ID of the email list to retrieve.

try:
    # Update an email list partially.
    api_response = api_instance.update_list(list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListsApi->update_list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.mailmojo.no/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**create_account**](docs/AccountsApi.md#create_account) | **POST** /accounts/ | Create an account.
*AccountsApi* | [**get_account_by_username**](docs/AccountsApi.md#get_account_by_username) | **GET** /accounts/{username}/ | Retrieve account details.
*AccountsApi* | [**update_account**](docs/AccountsApi.md#update_account) | **POST** /accounts/{username}/ | Update account details.
*ContactsApi* | [**get_contacts**](docs/ContactsApi.md#get_contacts) | **GET** /contacts/ | Retrieve all contacts across every list.
*ContactsApi* | [**get_subscriber_on_list_by_email**](docs/ContactsApi.md#get_subscriber_on_list_by_email) | **GET** /lists/{list_id}/subscribers/{email}/ | Retrieve a subscriber.
*ContactsApi* | [**get_subscribers_on_list**](docs/ContactsApi.md#get_subscribers_on_list) | **GET** /lists/{list_id}/subscribers/ | Retrieve subscribers on a list.
*ContactsApi* | [**import_subscribers_to_list**](docs/ContactsApi.md#import_subscribers_to_list) | **POST** /lists/{list_id}/subscribers/import/ | Subscribe contacts to the email list.
*ContactsApi* | [**subscribe_contact_to_list**](docs/ContactsApi.md#subscribe_contact_to_list) | **POST** /lists/{list_id}/subscribers/ | Subscribe a contact to the email list.
*ContactsApi* | [**unsubscribe_contact_on_list_by_email**](docs/ContactsApi.md#unsubscribe_contact_on_list_by_email) | **DELETE** /lists/{list_id}/subscribers/{email}/ | Unsubscribe a contact.
*EmbedApi* | [**create_embed_session**](docs/EmbedApi.md#create_embed_session) | **POST** /embed/ | Create a new embedded application session.
*ListsApi* | [**get_list_by_id**](docs/ListsApi.md#get_list_by_id) | **GET** /lists/{list_id}/ | Retrieve an email list.
*ListsApi* | [**get_lists**](docs/ListsApi.md#get_lists) | **GET** /lists/ | Retrieve all email lists.
*ListsApi* | [**update_list**](docs/ListsApi.md#update_list) | **PATCH** /lists/{list_id}/ | Update an email list partially.


## Documentation For Models

 - [Contact](docs/Contact.md)
 - [ContactListAssociations](docs/ContactListAssociations.md)
 - [Contacts](docs/Contacts.md)
 - [Embed](docs/Embed.md)
 - [EmbedOptions](docs/EmbedOptions.md)
 - [ImportResult](docs/ImportResult.md)
 - [List](docs/List.md)
 - [MinimalUser](docs/MinimalUser.md)
 - [Subscriber](docs/Subscriber.md)
 - [User](docs/User.md)


## Documentation For Authorization


## mailmojo_auth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://api.mailmojo.no/oauth/authorize/
- **Scopes**: 
 - **account**: Manage your MailMojo account.
 - **account_creation**: Create new MailMojo accounts.
 - **account_creation.trial_30**: Create new MailMojo accounts with a 30 day trial period.
 - **contacts**: Manage your contacts across all your email lists.
 - **contacts:read**: Retrieve your contacts across all your email lists.
 - **embed**: Give you an embedded MailMojo application with access to your account.
 - **lists**: Manage your email lists, excluding subscribers.
 - **lists:read**: Retrieve your email lists, excluding subscribers.


## Author

hjelp@mailmojo.no

