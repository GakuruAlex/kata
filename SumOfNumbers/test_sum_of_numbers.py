from sum_of_numbers import get_sum

class TestSumOfNumbersBetween1And0:
    a, b = 1, 0
    result = 1
    def test_get_sum_between_1_and_0(self):
        assert get_sum(self.a, self.b) == self.result
class TestSumOfNumbersBetween1And2:
    a, b = 1, 2
    result = 3
    def test_get_sum_between_1_and_2(self):
        assert get_sum(self.a, self.b) == self.result

class TestSumOfNumbersBetween0And1:
    a, b = 0, 1
    result = 1
    def test_get_sum_between_0_and_1(self):
        assert get_sum(self.a, self.b) == self.result

class TestSumOfNumbersBetween1And1:
    a, b = 1, 1
    result = 1
    def test_get_sum_between_1_and_1(self):
        assert get_sum(self.a, self.b) == self.result

class TestSumOfNumbersBetweenNeg1And0:
    a, b = -1, 0
    result = -1
    def test_get_sum_between_neg1_and_0(self):
        assert get_sum(self.a, self.b) == self.result

class TestSumOfNumbersBetweenNeg1And2:
    a, b = -1, 2
    result = 2
    def test_get_sum_between_neg1_and_2(self):
        assert get_sum(self.a, self.b) == self.result