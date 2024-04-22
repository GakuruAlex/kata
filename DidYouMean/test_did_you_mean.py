from didyoumean import Dictionary
import pytest

@pytest.fixture
    
def fruits_dictionary():
    """Initialize fruits dictionary via Dictionary constructor """
    fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])
    return fruits
def things_dictionary():
    """Initialize things dictionary via Dictionary constructor """
    things =Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars'])
    return things
def languages_dictionary():
    """Initialize languages dictionary via Dictionary constructor """
    languages =Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript'])
    return languages

def test_find_most_similar_for_fruits_with_strawbery(fruit_dictionary):
    assert fruit_dictionary.find_most_similar("strawbery")== "strawberry"

def test_find_most_similar_for_fruits_with_berry(fruit_dictionary):
    assert fruit_dictionary.find_most_similar("berry")== "cherry"

def test_find_most_similar_for_things(things_dictionary):
    assert things_dictionary.find_most_similar("coddwars") == "codewars"

def test_find_most_similar_for_languages_with_heaven(languages_dictionary):
    assert languages_dictionary.find_most_similar("heaven") == "java"

def test_find_most_similar_for_languages_with_heaven(languages_dictionary):
    assert languages_dictionary.find_most_similar("javascript") == "javascript"