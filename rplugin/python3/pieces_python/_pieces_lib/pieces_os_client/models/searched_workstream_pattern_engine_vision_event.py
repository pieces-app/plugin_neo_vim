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


from typing import Optional, Union
from pieces_python._pieces_lib.pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from pieces_python._pieces_lib.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_python._pieces_lib.pieces_os_client.models.workstream_pattern_engine_vision_event import WorkstreamPatternEngineVisionEvent

class SearchedWorkstreamPatternEngineVisionEvent(BaseModel):
    """
    This will return a list of the returned events.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    event: Optional[WorkstreamPatternEngineVisionEvent] = None
    exact: Optional[StrictBool] = None
    similarity: Optional[Union[StrictFloat, StrictInt]] = None
    temporal: Optional[StrictBool] = None
    application: Optional[StrictStr] = None
    identifier: StrictStr = Field(default=..., description="This is the uuid of the event.")
    __properties = ["schema", "event", "exact", "similarity", "temporal", "application", "identifier"]

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
    def from_json(cls, json_str: str) -> SearchedWorkstreamPatternEngineVisionEvent:
        """Create an instance of SearchedWorkstreamPatternEngineVisionEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchedWorkstreamPatternEngineVisionEvent:
        """Create an instance of SearchedWorkstreamPatternEngineVisionEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchedWorkstreamPatternEngineVisionEvent.parse_obj(obj)

        _obj = SearchedWorkstreamPatternEngineVisionEvent.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "event": WorkstreamPatternEngineVisionEvent.from_dict(obj.get("event")) if obj.get("event") is not None else None,
            "exact": obj.get("exact"),
            "similarity": obj.get("similarity"),
            "temporal": obj.get("temporal"),
            "application": obj.get("application"),
            "identifier": obj.get("identifier")
        })
        return _obj


