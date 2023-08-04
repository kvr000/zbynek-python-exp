import pytest
import unittest

from typing import Optional
from dataclasses import dataclass
import json
import logging
import jsonpickle
from pydantic import BaseModel, Field


@dataclass
class Person:
    firstName: Optional[str]
    lastName: Optional[str]

    def __init__(self, firstName: Optional[str] = None, lastName: Optional[str] = None):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return jsonpickle.encode(self)


class ClassDeserializeTest(unittest.TestCase):

    @pytest.mark.timeout(2)
    def test_deserialize_full(self):
        input = """{
            "firstName": "Zbynek",
            "lastName": "Vyskovsky"
        }"""
        loaded = json.loads(input)
        person = Person(**loaded)
        logging.error(str(person))

    @pytest.mark.timeout(2)
    def test_deserialize_partial(self):
        input = """{
            "lastName": "Vyskovsky"
        }"""
        loaded = json.loads(input)
        person = Person(**loaded)
        logging.error(str(person))

    @pytest.mark.timeout(2)
    def test_deserialize_unknown(self):
        input = """{
            "lastName": "Vyskovsky",
            "age": 46
        }"""
        try:
            loaded = json.loads(input)
            person = Person(**loaded)
            assert false
        except TypeError:
            pass
