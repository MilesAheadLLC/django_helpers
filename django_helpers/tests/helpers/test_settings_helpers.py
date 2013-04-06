import pytest

from django_helpers.helpers.settings import set_default

def test_set_default_returns_value_when_value_exists():
    value = set_default('Ray','Charles')
    assert value == 'Ray'

def test_set_default_returns_the_default_value_when_value_is_empty_string():
    value = set_default("", 'Charles')
    assert value == 'Charles'

def test_set_default_returns_the_default_value_when_value_is_none():
    value = set_default(None, 'Charles')
    assert value == 'Charles'