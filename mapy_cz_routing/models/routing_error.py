# coding: utf-8

"""
    REST API Mapy.cz routing methods

    Service for finding/planning a route between two or more points.   Api is based on common principles described in the document [Common principles of REST API Mapy.cz](/v1/docs/commons/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RoutingError(BaseModel):
    """
    RoutingError
    """ # noqa: E501
    msg: Optional[Any] = None
    error_code: Optional[Any] = Field(default=None, alias="errorCode")
    __properties: ClassVar[List[str]] = ["msg", "errorCode"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RoutingError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if msg (nullable) is None
        # and model_fields_set contains the field
        if self.msg is None and "msg" in self.model_fields_set:
            _dict['msg'] = None

        # set to None if error_code (nullable) is None
        # and model_fields_set contains the field
        if self.error_code is None and "error_code" in self.model_fields_set:
            _dict['errorCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RoutingError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "msg": obj.get("msg"),
            "errorCode": obj.get("errorCode")
        })
        return _obj


