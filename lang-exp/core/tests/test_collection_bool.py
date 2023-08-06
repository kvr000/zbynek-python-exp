import pytest
import unittest


class CollectionBoolTest(unittest.TestCase):

    @pytest.mark.timeout(2)
    def test_bool__empty_list__return_false(self):
        if []:
            assert False


    @pytest.mark.timeout(2)
    def test_bool__populated_list__return_true(self):
        if not [ 0 ]:
            assert False


    @pytest.mark.timeout(2)
    def test_bool__empty_dict__return_false(self):
        if {}:
            assert False

