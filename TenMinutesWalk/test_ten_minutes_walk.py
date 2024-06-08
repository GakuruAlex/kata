import pytest
from ten_minutes_walk import is_valid_walk

@pytest.mark.parametrize("walk, result", [
    (['n','s','n','s','n','s','n','s','n','s'], True),
    (['w','e','w','e','w','e','w','e','w','e','w','e'], False),
    (['w'], False),
    (['n','n','n','s','n','s','n','s','n','s'], False),
    (['n','n','n','s','s','s','e','w','w','e'], True),
    (['n','n','n','s','s','s','e','w','w','e','w', 'w','e','e'], False)
])
class TestIsValidWalk:
    def test_is_valid_walk(self, walk, result):
        assert is_valid_walk(walk) == result


@pytest.mark.xfail(reason="This test is supposed to fail.")
def test_is_valid_walk_failure():
    assert is_valid_walk(["n","n","s","s"]) == True