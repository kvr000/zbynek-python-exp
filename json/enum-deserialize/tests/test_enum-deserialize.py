from __future__ import annotations
import pytest
import unittest

import enum

from typing import Optional
from dataclasses import dataclass
import json
from json import JSONEncoder
import logging
import jsonpickle
from pydantic import BaseModel, Field


def _default_encoder(self, obj):
    to_serializable = getattr(obj, "to_serializable", None)
    if to_serializable is not None:
        return to_serializable()
    else:
        return _default_encoder.default(self, obj)


_default_encoder.default = JSONEncoder.default
JSONEncoder.default = _default_encoder


Aging_VALUES = {
    "CHILD": 1,
    "ADULT": 2,
}
@dataclass
class Aging(enum.Enum):
    CHILD = "CHILD"
    ADULT = "ADULT"

    def to_serializable(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


class Person(BaseModel):
    firstName: str|None = None
    aging: Aging|None = None

    def to_serializable(self):
        return self.__dict__

    @classmethod
    def decode(cls, s):
        return Person(**json.loads(s))


class EnumDeserializeTest(unittest.TestCase):

    @pytest.mark.timeout(2)
    def test_serialize_enum(self):
        person = Person(firstName='Zbynek', aging=Aging.ADULT)
        serialized = json.dumps(person)
        assert serialized == '{"firstName": "Zbynek", "aging": "ADULT"}'

    @pytest.mark.timeout(2)
    def test_deserialize_enum(self):
        person = json.loads('{"firstName": "Zbynek", "aging": "ADULT"}', cls=Person)
        assert person == Person(firstName='Zbynek', aging=Aging.CHILD)

