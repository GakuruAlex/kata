from who_likes_it import likes,dict_likes
import pytest
def test_likes_with_no_name():
    assert dict_likes([])=="no one likes this"

def test_likes_with_one_name():
    assert dict_likes(["James"]) == "James likes this"

def test_likes_with_two_names():
    assert dict_likes(["James","John"]) == "James and John like this"

def test_likes_with_three_names():
    assert dict_likes(["John","James","Peter"]) == "John, James and Peter like this"

def test_likes_with_more_than_three_names():
    assert dict_likes(["Peter","John","James","Samuel","Barth","Simon"]) == "Peter, John and 4 others like this"

