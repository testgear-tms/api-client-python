"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from testgear_api_client.api_client import ApiClient, Endpoint as _Endpoint
from testgear_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from testgear_api_client.model.configuration_by_parameters_model import ConfigurationByParametersModel
from testgear_api_client.model.configuration_model import ConfigurationModel
from testgear_api_client.model.configuration_post_model import ConfigurationPostModel
from testgear_api_client.model.configuration_put_model import ConfigurationPutModel
from testgear_api_client.model.configuration_select_model import ConfigurationSelectModel
from testgear_api_client.model.problem_details import ProblemDetails
from testgear_api_client.model.validation_problem_details import ValidationProblemDetails


class ConfigurationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.api_v2_configurations_create_by_parameters_post_endpoint = _Endpoint(
            settings={
                'response_type': ([str],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/configurations/createByParameters',
                'operation_id': 'api_v2_configurations_create_by_parameters_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'configuration_by_parameters_model',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'configuration_by_parameters_model':
                        (ConfigurationByParametersModel,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'configuration_by_parameters_model': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.api_v2_configurations_search_post_endpoint = _Endpoint(
            settings={
                'response_type': ([ConfigurationModel],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/configurations/search',
                'operation_id': 'api_v2_configurations_search_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'skip',
                    'take',
                    'order_by',
                    'search_field',
                    'search_value',
                    'configuration_select_model',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'skip':
                        (int,),
                    'take':
                        (int,),
                    'order_by':
                        (str,),
                    'search_field':
                        (str,),
                    'search_value':
                        (str,),
                    'configuration_select_model':
                        (ConfigurationSelectModel,),
                },
                'attribute_map': {
                    'skip': 'Skip',
                    'take': 'Take',
                    'order_by': 'OrderBy',
                    'search_field': 'SearchField',
                    'search_value': 'SearchValue',
                },
                'location_map': {
                    'skip': 'query',
                    'take': 'query',
                    'order_by': 'query',
                    'search_field': 'query',
                    'search_value': 'query',
                    'configuration_select_model': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (ConfigurationModel,),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/configurations',
                'operation_id': 'create_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'configuration_post_model',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'configuration_post_model':
                        (ConfigurationPostModel,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'configuration_post_model': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_configuration_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (ConfigurationModel,),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/configurations/{id}',
                'operation_id': 'get_configuration_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_configuration_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/configurations',
                'operation_id': 'update_configuration',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'configuration_put_model',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'configuration_put_model':
                        (ConfigurationPutModel,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'configuration_put_model': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def api_v2_configurations_create_by_parameters_post(
        self,
        **kwargs
    ):
        """Create Configurations by parameters  # noqa: E501

        <br>Use case  <br>User sets request model (listed in the request example)  <br>User runs method execution  <br>System creates configurations  <br>System returns created configuration ids (listed in the response example)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_configurations_create_by_parameters_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            configuration_by_parameters_model (ConfigurationByParametersModel): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [str]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.api_v2_configurations_create_by_parameters_post_endpoint.call_with_http_info(**kwargs)

    def api_v2_configurations_search_post(
        self,
        **kwargs
    ):
        """Search for configurations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_configurations_search_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            skip (int): Amount of items to be skipped (offset). [optional]
            take (int): Amount of items to be taken (limit). [optional]
            order_by (str): SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC). [optional]
            search_field (str): Property name for searching. [optional]
            search_value (str): Value for searching. [optional]
            configuration_select_model (ConfigurationSelectModel): Model containing all the filters. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [ConfigurationModel]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.api_v2_configurations_search_post_endpoint.call_with_http_info(**kwargs)

    def create_configuration(
        self,
        **kwargs
    ):
        """Create Configuration  # noqa: E501

        <br>Use case  <br>User sets configuration model (listed in the request example)  <br>User runs method execution  <br>System creates configuration  <br>System returns created configuration (listed in the response example)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_configuration(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            configuration_post_model (ConfigurationPostModel): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ConfigurationModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.create_configuration_endpoint.call_with_http_info(**kwargs)

    def get_configuration_by_id(
        self,
        id,
        **kwargs
    ):
        """Get configuration by internal or global ID  # noqa: E501

        <br>Use case  <br>User sets configuration internal (guid format) or global (integer format) identifier  <br>User runs method execution  <br>System search configuration using the identifier  <br>System returns configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_configuration_by_id(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ConfigurationModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['id'] = \
            id
        return self.get_configuration_by_id_endpoint.call_with_http_info(**kwargs)

    def update_configuration(
        self,
        **kwargs
    ):
        """Update Configuration  # noqa: E501

        <br>Use case  <br>User sets configuration updated properties(listed in the request example)  <br>User runs method execution  <br>System updated configuration using updated properties  <br>System returns no content response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_configuration(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            configuration_put_model (ConfigurationPutModel): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.update_configuration_endpoint.call_with_http_info(**kwargs)

