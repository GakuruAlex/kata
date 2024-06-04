from persistent_bugger import persistence
import pytest

def test_persistence_with_999():
    assert persistence(999) == 4

def test_persistence_with_39():
    assert persistence(39) == 3

def test_persistence_with_4():
    assert persistence(4) == 0

