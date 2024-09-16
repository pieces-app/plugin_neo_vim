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
from pieces_python._pieces_lib.pieces_os_client.models.flattened_share import FlattenedShare
from pieces_python._pieces_lib.pieces_os_client.models.git_hub_distribution import GitHubDistribution
from pieces_python._pieces_lib.pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_python._pieces_lib.pieces_os_client.models.mailgun_distribution import MailgunDistribution

class Distribution(BaseModel):
    """
    This is a fully referenced version of a Distribution. TODO add additional distributions such as slack, google_chat, ...etc  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr = Field(...)
    share: FlattenedShare = Field(...)
    created: GroupedTimestamp = Field(...)
    updated: GroupedTimestamp = Field(...)
    deleted: Optional[GroupedTimestamp] = None
    mailgun: Optional[MailgunDistribution] = None
    github: Optional[GitHubDistribution] = None
    __properties = ["schema", "id", "share", "created", "updated", "deleted", "mailgun", "github"]

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
    def from_json(cls, json_str: str) -> Distribution:
        """Create an instance of Distribution from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of share
        if self.share:
            _dict['share'] = self.share.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mailgun
        if self.mailgun:
            _dict['mailgun'] = self.mailgun.to_dict()
        # override the default output from pydantic by calling `to_dict()` of github
        if self.github:
            _dict['github'] = self.github.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Distribution:
        """Create an instance of Distribution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Distribution.parse_obj(obj)

        _obj = Distribution.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "share": FlattenedShare.from_dict(obj.get("share")) if obj.get("share") is not None else None,
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj.get("deleted")) if obj.get("deleted") is not None else None,
            "mailgun": MailgunDistribution.from_dict(obj.get("mailgun")) if obj.get("mailgun") is not None else None,
            "github": GitHubDistribution.from_dict(obj.get("github")) if obj.get("github") is not None else None
        })
        return _obj


