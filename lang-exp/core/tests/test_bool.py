import pytest
import unittest


class BoolTest(unittest.TestCase):

    class BoolClass:
        value: bool

        def __init__(self, value):
            self.value = value

        def __bool__(self):
            return self.value


    @pytest.mark.timeout(2)
    def test_condition__with_bool_override__expected(self):
        if BoolTest.BoolClass(False):
            assert False
        if not BoolTest.BoolClass(True):
            assert False
