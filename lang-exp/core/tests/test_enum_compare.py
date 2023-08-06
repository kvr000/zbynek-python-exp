from enum import Enum

import pytest
import unittest


class EnumCompareTest(unittest.TestCase):

    class MyEnum(Enum):
        GREEN = 1
        RED = 2
        BLUE = 3

        def __lt__(self, other):
            return self.value < other.value

        def __le__(self, other):
            return self.value <= other.value

    @pytest.mark.timeout(2)
    def test_compare__any__correct(self):
        assert EnumCompareTest.MyEnum.GREEN < EnumCompareTest.MyEnum.RED
        assert EnumCompareTest.MyEnum.GREEN <= EnumCompareTest.MyEnum.RED
        assert EnumCompareTest.MyEnum.RED <= EnumCompareTest.MyEnum.RED
        assert EnumCompareTest.MyEnum.BLUE > EnumCompareTest.MyEnum.RED
        assert EnumCompareTest.MyEnum.BLUE > EnumCompareTest.MyEnum.GREEN
        assert EnumCompareTest.MyEnum.BLUE >= EnumCompareTest.MyEnum.GREEN
        assert EnumCompareTest.MyEnum.RED >= EnumCompareTest.MyEnum.RED
