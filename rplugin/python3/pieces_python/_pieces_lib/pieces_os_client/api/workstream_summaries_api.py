# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pieces_python._pieces_lib.pydantic import validate_arguments, ValidationError

from pieces_python._pieces_lib.typing_extensions import Annotated
from pieces_python._pieces_lib.pydantic import Field, StrictBool, StrictStr

from typing import Optional

from pieces_python._pieces_lib.pieces_os_client.models.search_input import SearchInput
from pieces_python._pieces_lib.pieces_os_client.models.searched_workstream_summaries import SearchedWorkstreamSummaries
from pieces_python._pieces_lib.pieces_os_client.models.seeded_workstream_summary import SeededWorkstreamSummary
from pieces_python._pieces_lib.pieces_os_client.models.workstream_summaries import WorkstreamSummaries
from pieces_python._pieces_lib.pieces_os_client.models.workstream_summary import WorkstreamSummary

from pieces_python._pieces_lib.pieces_os_client.api_client import ApiClient
from pieces_python._pieces_lib.pieces_os_client.api_response import ApiResponse
from pieces_python._pieces_lib.pieces_os_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WorkstreamSummariesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def search_workstream_summaries(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, search_input : Optional[SearchInput] = None, **kwargs) -> SearchedWorkstreamSummaries:  # noqa: E501
        """/workstream_summaries/search [POST]  # noqa: E501

        This will search your workstream_summaries for a specific workstream_summary  note: we will just search the summary value(which is an annotation)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_workstream_summaries(transferables, search_input, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param search_input:
        :type search_input: SearchInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SearchedWorkstreamSummaries
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_workstream_summaries_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_workstream_summaries_with_http_info(transferables, search_input, **kwargs)  # noqa: E501

    @validate_arguments
    def search_workstream_summaries_with_http_info(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, search_input : Optional[SearchInput] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/workstream_summaries/search [POST]  # noqa: E501

        This will search your workstream_summaries for a specific workstream_summary  note: we will just search the summary value(which is an annotation)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_workstream_summaries_with_http_info(transferables, search_input, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param search_input:
        :type search_input: SearchInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SearchedWorkstreamSummaries, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'transferables',
            'search_input'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_workstream_summaries" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('transferables') is not None:  # noqa: E501
            _query_params.append(('transferables', _params['transferables']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['search_input'] is not None:
            _body_params = _params['search_input']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "SearchedWorkstreamSummaries",
            '500': "str",
        }

        return self.api_client.call_api(
            '/workstream_summaries/search', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def workstream_summaries_create_new_workstream_summary(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, seeded_workstream_summary : Optional[SeededWorkstreamSummary] = None, **kwargs) -> WorkstreamSummary:  # noqa: E501
        """/workstream_summaries/create [POST]  # noqa: E501

        This will create a new WorkstreamSummary in the database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.workstream_summaries_create_new_workstream_summary(transferables, seeded_workstream_summary, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param seeded_workstream_summary:
        :type seeded_workstream_summary: SeededWorkstreamSummary
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WorkstreamSummary
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the workstream_summaries_create_new_workstream_summary_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.workstream_summaries_create_new_workstream_summary_with_http_info(transferables, seeded_workstream_summary, **kwargs)  # noqa: E501

    @validate_arguments
    def workstream_summaries_create_new_workstream_summary_with_http_info(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, seeded_workstream_summary : Optional[SeededWorkstreamSummary] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/workstream_summaries/create [POST]  # noqa: E501

        This will create a new WorkstreamSummary in the database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.workstream_summaries_create_new_workstream_summary_with_http_info(transferables, seeded_workstream_summary, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param seeded_workstream_summary:
        :type seeded_workstream_summary: SeededWorkstreamSummary
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WorkstreamSummary, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'transferables',
            'seeded_workstream_summary'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workstream_summaries_create_new_workstream_summary" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('transferables') is not None:  # noqa: E501
            _query_params.append(('transferables', _params['transferables']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['seeded_workstream_summary'] is not None:
            _body_params = _params['seeded_workstream_summary']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "WorkstreamSummary",
            '500': "str",
        }

        return self.api_client.call_api(
            '/workstream_summaries/create', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def workstream_summaries_delete_specific_workstream_summary(self, workstream_summary : Annotated[StrictStr, Field(..., description="This is a identifier that is used to identify a specific workstream_summary.")], **kwargs) -> None:  # noqa: E501
        """/workstream_summaries/{workstream_summary}/delete [POST]  # noqa: E501

        This will delete a specific workstream_summary from the database!  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.workstream_summaries_delete_specific_workstream_summary(workstream_summary, async_req=True)
        >>> result = thread.get()

        :param workstream_summary: This is a identifier that is used to identify a specific workstream_summary. (required)
        :type workstream_summary: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the workstream_summaries_delete_specific_workstream_summary_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.workstream_summaries_delete_specific_workstream_summary_with_http_info(workstream_summary, **kwargs)  # noqa: E501

    @validate_arguments
    def workstream_summaries_delete_specific_workstream_summary_with_http_info(self, workstream_summary : Annotated[StrictStr, Field(..., description="This is a identifier that is used to identify a specific workstream_summary.")], **kwargs) -> ApiResponse:  # noqa: E501
        """/workstream_summaries/{workstream_summary}/delete [POST]  # noqa: E501

        This will delete a specific workstream_summary from the database!  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.workstream_summaries_delete_specific_workstream_summary_with_http_info(workstream_summary, async_req=True)
        >>> result = thread.get()

        :param workstream_summary: This is a identifier that is used to identify a specific workstream_summary. (required)
        :type workstream_summary: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'workstream_summary'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workstream_summaries_delete_specific_workstream_summary" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['workstream_summary'] is not None:
            _path_params['workstream_summary'] = _params['workstream_summary']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/workstream_summaries/{workstream_summary}/delete', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def workstream_summaries_snapshot(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, **kwargs) -> WorkstreamSummaries:  # noqa: E501
        """/workstream_summaries [GET]  # noqa: E501

        This will get a snapshot of all your workstream summaries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.workstream_summaries_snapshot(transferables, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WorkstreamSummaries
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the workstream_summaries_snapshot_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.workstream_summaries_snapshot_with_http_info(transferables, **kwargs)  # noqa: E501

    @validate_arguments
    def workstream_summaries_snapshot_with_http_info(self, transferables : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/workstream_summaries [GET]  # noqa: E501

        This will get a snapshot of all your workstream summaries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.workstream_summaries_snapshot_with_http_info(transferables, async_req=True)
        >>> result = thread.get()

        :param transferables: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferables: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WorkstreamSummaries, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'transferables'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workstream_summaries_snapshot" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('transferables') is not None:  # noqa: E501
            _query_params.append(('transferables', _params['transferables']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "WorkstreamSummaries",
            '500': "str",
        }

        return self.api_client.call_api(
            '/workstream_summaries', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
