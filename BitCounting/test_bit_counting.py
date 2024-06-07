import pytest
from bit_counting import count_bits

pytest.mark.parametrize("n, result",[(0, 0),
                                     (4, 1),
                                     (7, 3),
                                     (9, 2),
                                     (10, 2),
                                     (1234, 5),
                                     (4536, 6),
                                     (85961, 10)
                                     ])

class TestCountBits:
    def test_count_bits(self, n, result):
        assert count_bits(n) == result