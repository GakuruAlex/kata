import pytest
from camel_case import to_camel_case,to_camel_case_2

class TestToCamelCaseWithDashOnly():
    test_with_dash = "the-stealth-warrior"
    result = "theStealthWarrior"
    def test_to_camel_case_with_dash_only(self):
        assert to_camel_case(self.test_with_dash) == self.result

    def test_to_camel_case_2_with_dash_only(self):
        assert to_camel_case_2(self.test_with_dash) == self.result

class TestToCamelCaseWithUnderscoreOnly():
    test_with_underscore = "the_stealth_warrior"
    result = ""