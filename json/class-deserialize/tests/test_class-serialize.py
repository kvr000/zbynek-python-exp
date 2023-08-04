import pytest
from pydantic import BaseModel
import unittest
import logging
import json
from json import JSONEncoder


def _default_encoder(self, obj):
    to_serializable = getattr(obj, "to_serializable", None)
    if to_serializable is not None:
        return to_serializable()
    else:
        return _default_encoder.default(self, obj)


_default_encoder.default = JSONEncoder.default
JSONEncoder.default = _default_encoder


class Person:
    firstName: str|None
    lastName: str|None

    def __init__(self, firstName: str|None = None, lastName: str|None = None):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return jsonpickle.encode(self)

    def to_serializable(self):
        return self.__dict__


class ClassSerializeTest(unittest.TestCase):

    @pytest.mark.timeout(2)
    def test_serialize_full(self):
        person = Person(firstName="Zbynek", lastName="Vyskovsky")
        result = json.dumps(person)
        logging.error(result)
        assert result == '{"firstName": "Zbynek", "lastName": "Vyskovsky"}'

