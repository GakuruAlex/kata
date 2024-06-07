import pytest
from binary_2_number import binary_array_to_number_2, binary_array_to_number_3, binary_array_to_number

@pytest.mark.parametrize("a, result", [([0, 0, 0, 1], 1),
                                       ([0, 0, 1, 0], 2),
                                       ([0, 1, 0, 1], 5),
                                       ([1, 0, 0, 1], 9),
                                       ([0, 0, 1, 0], 2),
                                       ([0, 1, 1, 0], 6),
                                       ([1, 1, 1, 1], 15),
                                       ([1, 0, 1, 1], 11)

                                   ])
class TestBinaryArrayToNumber:
    def test_binary_array_to_number(self, a, result):
        a1 = a.copy()
        assert binary_array_to_number(a1) == result

    def test_binary_array_to_number_2(self, a, result):
        a2 = a.copy()
        assert binary_array_to_number_2(a2) == result

    def test_binary_array_to_number_3(self, a, result):
        a3 = a.copy()
        assert binary_array_to_number_3(a3) == result
