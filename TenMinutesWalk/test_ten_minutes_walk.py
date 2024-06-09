import pytest
from ten_minutes_walk import is_valid_walk,is_valid_walk_soln

@pytest.mark.parametrize("walk, result", [
    (['n','s','n','s','n','s','n','s','n','s'], True),
    (['w','e','w','e','w','e','w','e','w','e','w','e'], False),
    (['w'], False),
    (['n','n','n','s','n','s','n','s','n','s'], False),
    (['n','n','n','s','s','s','e','w','w','e'], True),
    (['n','n','n','s','s','s','e','w','w','e','w', 'w','e','e'], False),
    (['n', 's', 'w', 'w', 'e', 's', 'e', 's', 'n', 's'], False),
    (['n', 'e', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], False)
])
class TestIsValidWalk:
    def test_is_valid_walk(self, walk, result):
        walk_test = walk.copy()
        assert is_valid_walk(walk_test) == result
    def test_is_valid_walk_soln(self, walk, result):
        test_walk = walk.copy()
        assert is_valid_walk_soln(test_walk) == result
    


@pytest.mark.xfail(reason="This test is supposed to fail.")
def test_is_valid_walk_failure():
    assert is_valid_walk(["n","n","s","s"]) == True