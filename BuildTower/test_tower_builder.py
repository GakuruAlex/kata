import pytest
from tower_builder import tower_builder

@pytest.mark.parametrize("a, expected", [
    (3, [
  "  *  ",
  " *** ",
  "*****"]),
    (2, [' * ', '***']),
    (1, ['*' ])
])

def test_tower_builder(a, expected):
    assert tower_builder(a) == expected

@pytest.mark.xfail(reason="This test is expected to fail")
def test_tower_builder_failure():
    assert tower_builder(2) == ['***']