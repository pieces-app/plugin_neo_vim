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


from typing import Dict, Optional
from pieces_python._pieces_lib.pydantic import BaseModel, Field, StrictInt, StrictStr
from pieces_python._pieces_lib.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_python._pieces_lib.pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_python._pieces_lib.pieces_os_client.models.flattened_persons import FlattenedPersons
from pieces_python._pieces_lib.pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_python._pieces_lib.pieces_os_client.models.mechanism_enum import MechanismEnum
from pieces_python._pieces_lib.pieces_os_client.models.relationship import Relationship
from pieces_python._pieces_lib.pieces_os_client.models.score import Score
from pieces_python._pieces_lib.pieces_os_client.models.tag_category_enum import TagCategoryEnum

class Tag(BaseModel):
    """
    This represents a fully polinated Tag, that is either attached to an asset or a format that adds additional information \"tags\" to describe itself.Helps improve Search and other contextual information that is useful for the user.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr = Field(default=..., description="UUID that represents the tag.")
    text: StrictStr = Field(default=..., description="represnts the value of a tag.")
    mechanisms: Optional[Dict[str, MechanismEnum]] = Field(default=None, description="This is a Map<String, MechanismEnum> where the the key is an asset id.")
    assets: Optional[FlattenedAssets] = None
    created: GroupedTimestamp = Field(...)
    updated: GroupedTimestamp = Field(...)
    deleted: Optional[GroupedTimestamp] = None
    category: TagCategoryEnum = Field(...)
    relationship: Optional[Relationship] = None
    interactions: Optional[StrictInt] = Field(default=None, description="This is an optional value that will keep track of the number of times this has been interacted with.")
    persons: Optional[FlattenedPersons] = None
    score: Optional[Score] = None
    __properties = ["schema", "id", "text", "mechanisms", "assets", "created", "updated", "deleted", "category", "relationship", "interactions", "persons", "score"]

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
    def from_json(cls, json_str: str) -> Tag:
        """Create an instance of Tag from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relationship
        if self.relationship:
            _dict['relationship'] = self.relationship.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Tag:
        """Create an instance of Tag from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Tag.parse_obj(obj)

        _obj = Tag.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "text": obj.get("text"),
            "mechanisms": dict((_k, _v) for _k, _v in obj.get("mechanisms").items()),
            "assets": FlattenedAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj.get("deleted")) if obj.get("deleted") is not None else None,
            "category": obj.get("category"),
            "relationship": Relationship.from_dict(obj.get("relationship")) if obj.get("relationship") is not None else None,
            "interactions": obj.get("interactions"),
            "persons": FlattenedPersons.from_dict(obj.get("persons")) if obj.get("persons") is not None else None,
            "score": Score.from_dict(obj.get("score")) if obj.get("score") is not None else None
        })
        return _obj


