# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from pieces_python._pieces_lib.aenum import Enum, no_arg





class PrivacyEnum(str, Enum):
    """
    OPEN: Means that privacy is fully open CLOSED: Means that privacy is fully locked down, and private ANONYMOUS: Means that we are allowed to collect information but it cannot get attached to me as the user.
    """

    """
    allowed enum values
    """
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    ANONYMOUS = 'ANONYMOUS'

    @classmethod
    def from_json(cls, json_str: str) -> PrivacyEnum:
        """Create an instance of PrivacyEnum from a JSON string"""
        return PrivacyEnum(json.loads(json_str))


