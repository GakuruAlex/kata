from camel_case import to_camel_case,to_camel_case_2

class TestToCamelCaseWithDash:
    test_with_dash = "the-stealth-warrior"
    result = "theStealthWarrior"
    
    def test_to_camel_case_with_dash_only(self):
        assert to_camel_case(self.test_with_dash) == self.result

    def test_to_camel_case_2_with_dash_only(self):
        assert to_camel_case_2(self.test_with_dash) == self.result

class TestToCamelCaseWithUnderscore:
    test_with_underscore = "the_stealth_warrior"
    result = "theStealthWarrior"
    
    def test_to_camel_case_with_underscore_only(self):
        assert to_camel_case(self.test_with_underscore) == self.result
    
    def test_to_camel_case_2_with_underscore_only(self):
        assert to_camel_case_2(self.test_with_underscore) == self.result

class TestToCamelCaseWithDashAndUnderscore:
    test_with_underscore_and_dash = "The-stealth_warrior"
    result = "TheStealthWarrior"
    
    def test_to_camel_case_with_dash_and_underscore(self):
        assert to_camel_case(self.test_with_underscore_and_dash) == self.result
        
    def test_to_camel_case_2_with_dash_and_underscore(self):
        assert to_camel_case_2(self.test_with_underscore_and_dash) == self.result

class TestToCamelCaseWithLongerText:
    test_with_longer_text = "the-stealth_ninja-warrior_Hero"
    result = "theStealthNinjaWarriorHero"
    
    def test_to_camel_case_with_longer_text(self):
        assert to_camel_case(self.test_with_longer_text) == self.result
    def test_to_camel_case_2_with_longer_text(self):
        assert to_camel_case_2(self.test_with_longer_text) == self.result