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


from typing import Optional
from pieces_python._pieces_lib.pydantic import BaseModel, Field, StrictStr
from pieces_python._pieces_lib.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_python._pieces_lib.pieces_os_client.models.seeded_file import SeededFile
from pieces_python._pieces_lib.pieces_os_client.models.seeded_fragment import SeededFragment
from pieces_python._pieces_lib.pieces_os_client.models.tlp_directed_discovery_filters import TLPDirectedDiscoveryFilters

class SeededDiscoverableAsset(BaseModel):
    """
    Assumption: filters applied in this model will overwrite filters passed in SeededDiscoverableAssets  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    file: Optional[SeededFile] = None
    fragment: Optional[SeededFragment] = None
    directory: Optional[StrictStr] = None
    filters: Optional[TLPDirectedDiscoveryFilters] = None
    __properties = ["schema", "file", "fragment", "directory", "filters"]

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
    def from_json(cls, json_str: str) -> SeededDiscoverableAsset:
        """Create an instance of SeededDiscoverableAsset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fragment
        if self.fragment:
            _dict['fragment'] = self.fragment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededDiscoverableAsset:
        """Create an instance of SeededDiscoverableAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededDiscoverableAsset.parse_obj(obj)

        _obj = SeededDiscoverableAsset.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "file": SeededFile.from_dict(obj.get("file")) if obj.get("file") is not None else None,
            "fragment": SeededFragment.from_dict(obj.get("fragment")) if obj.get("fragment") is not None else None,
            "directory": obj.get("directory"),
            "filters": TLPDirectedDiscoveryFilters.from_dict(obj.get("filters")) if obj.get("filters") is not None else None
        })
        return _obj


