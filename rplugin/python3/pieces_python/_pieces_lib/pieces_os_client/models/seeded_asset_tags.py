# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pieces_python._pieces_lib.pydantic import BaseModel, Field, conlist
from pieces_python._pieces_lib.pieces_os_client.models.seeded_asset_tag import SeededAssetTag

class SeededAssetTags(BaseModel):
    """
    SeededAssetTags
    """
    iterable: conlist(SeededAssetTag) = Field(...)
    __properties = ["iterable"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SeededAssetTags:
        """Create an instance of SeededAssetTags from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in iterable (list)
        _items = []
        if self.iterable:
            for _item in self.iterable:
                if _item:
                    _items.append(_item.to_dict())
            _dict['iterable'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededAssetTags:
        """Create an instance of SeededAssetTags from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededAssetTags.parse_obj(obj)

        _obj = SeededAssetTags.parse_obj({
            "iterable": [SeededAssetTag.from_dict(_item) for _item in obj.get("iterable")] if obj.get("iterable") is not None else None
        })
        return _obj


