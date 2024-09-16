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
from pieces_python._pieces_lib.pieces_os_client.models.code_analysis import CodeAnalysis
from pieces_python._pieces_lib.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class Analysis(BaseModel):
    """
    This the the MlAnalysis Object, that will go on a format.  this will hold all the different analysis models!  ** keep format just a uuid for now **  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    code: Optional[CodeAnalysis] = None
    id: StrictStr = Field(...)
    format: StrictStr = Field(default=..., description="this is a reference to the format that it belongs too.")
    image: Optional[ImageAnalysis] = None
    __properties = ["schema", "code", "id", "format", "image"]

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
    def from_json(cls, json_str: str) -> Analysis:
        """Create an instance of Analysis from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of code
        if self.code:
            _dict['code'] = self.code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Analysis:
        """Create an instance of Analysis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Analysis.parse_obj(obj)

        _obj = Analysis.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "code": CodeAnalysis.from_dict(obj.get("code")) if obj.get("code") is not None else None,
            "id": obj.get("id"),
            "format": obj.get("format"),
            "image": ImageAnalysis.from_dict(obj.get("image")) if obj.get("image") is not None else None
        })
        return _obj

from pieces_python._pieces_lib.pieces_os_client.models.image_analysis import ImageAnalysis
Analysis.update_forward_refs()

