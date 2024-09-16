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
from pieces_python._pieces_lib.pieces_os_client.models.conversation import Conversation
from pieces_python._pieces_lib.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_python._pieces_lib.pieces_os_client.models.searched_annotations import SearchedAnnotations
from pieces_python._pieces_lib.pieces_os_client.models.searched_conversation_messages import SearchedConversationMessages

class SearchedConversation(BaseModel):
    """
    This is used for the Conversations searching endpoint.  conversation here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    conversation: Optional[Conversation] = None
    messages: Optional[SearchedConversationMessages] = None
    annotations: Optional[SearchedAnnotations] = None
    exact: StrictBool = Field(...)
    similarity: Union[StrictFloat, StrictInt] = Field(...)
    temporal: Optional[StrictBool] = None
    identifier: StrictStr = Field(default=..., description="This is the uuid of the conversation.")
    __properties = ["schema", "conversation", "messages", "annotations", "exact", "similarity", "temporal", "identifier"]

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
    def from_json(cls, json_str: str) -> SearchedConversation:
        """Create an instance of SearchedConversation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict['messages'] = self.messages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict['annotations'] = self.annotations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchedConversation:
        """Create an instance of SearchedConversation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchedConversation.parse_obj(obj)

        _obj = SearchedConversation.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "conversation": Conversation.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None,
            "messages": SearchedConversationMessages.from_dict(obj.get("messages")) if obj.get("messages") is not None else None,
            "annotations": SearchedAnnotations.from_dict(obj.get("annotations")) if obj.get("annotations") is not None else None,
            "exact": obj.get("exact"),
            "similarity": obj.get("similarity"),
            "temporal": obj.get("temporal"),
            "identifier": obj.get("identifier")
        })
        return _obj


