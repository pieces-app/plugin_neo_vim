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
from pieces_python._pieces_lib.pieces_os_client.models.access_enum import AccessEnum
from pieces_python._pieces_lib.pieces_os_client.models.accessors import Accessors
from pieces_python._pieces_lib.pieces_os_client.models.distributions import Distributions
from pieces_python._pieces_lib.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_python._pieces_lib.pieces_os_client.models.flattened_asset import FlattenedAsset
from pieces_python._pieces_lib.pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_python._pieces_lib.pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_python._pieces_lib.pieces_os_client.models.score import Score

class Share(BaseModel):
    """
    This represents what information that is relavent to anything and every sharing related. v1 will look very bare and will add more and more data as we go!  if user is undefined && access is public then we have an asset that is publicly available.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr = Field(default=..., description="This is the uuid that represents this share model.")
    user: Optional[StrictStr] = Field(default=None, description="this is the uuid of the user that the share is created for.")
    asset: Optional[FlattenedAsset] = None
    assets: Optional[FlattenedAssets] = None
    link: StrictStr = Field(default=..., description="This is the prebuilt link.")
    access: AccessEnum = Field(...)
    accessors: Accessors = Field(...)
    created: GroupedTimestamp = Field(...)
    short: StrictStr = Field(default=..., description="This is a shortened version of our uuid.")
    name: Optional[StrictStr] = Field(default=None, description="this is an optional name we can give to the link, ie ?p=JAVASCRIPT or what ever the user wants as long as it is available.")
    distributions: Optional[Distributions] = None
    score: Optional[Score] = None
    __properties = ["schema", "id", "user", "asset", "assets", "link", "access", "accessors", "created", "short", "name", "distributions", "score"]

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
    def from_json(cls, json_str: str) -> Share:
        """Create an instance of Share from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accessors
        if self.accessors:
            _dict['accessors'] = self.accessors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of distributions
        if self.distributions:
            _dict['distributions'] = self.distributions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Share:
        """Create an instance of Share from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Share.parse_obj(obj)

        _obj = Share.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "user": obj.get("user"),
            "asset": FlattenedAsset.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "assets": FlattenedAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "link": obj.get("link"),
            "access": obj.get("access"),
            "accessors": Accessors.from_dict(obj.get("accessors")) if obj.get("accessors") is not None else None,
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "short": obj.get("short"),
            "name": obj.get("name"),
            "distributions": Distributions.from_dict(obj.get("distributions")) if obj.get("distributions") is not None else None,
            "score": Score.from_dict(obj.get("score")) if obj.get("score") is not None else None
        })
        return _obj


