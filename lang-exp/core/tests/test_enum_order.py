from enum import Enum
from ordered_enum import OrderedEnum

import pytest
import unittest


class EnumOrderTest(unittest.TestCase):

    class MyEnum(OrderedEnum):
        GREEN = 1
        RED = 2
        BLUE = 3

    @pytest.mark.timeout(2)
    def test_order__any__correct(self):
        assert EnumOrderTest.MyEnum.GREEN < EnumOrderTest.MyEnum.RED
        assert EnumOrderTest.MyEnum.GREEN <= EnumOrderTest.MyEnum.RED
        assert EnumOrderTest.MyEnum.BLUE > EnumOrderTest.MyEnum.RED
        assert EnumOrderTest.MyEnum.BLUE > EnumOrderTest.MyEnum.GREEN
