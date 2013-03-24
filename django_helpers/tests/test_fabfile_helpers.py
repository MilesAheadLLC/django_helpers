import pytest

from django_helpers.helpers.fabfile import taskhelp

def test_get_docstring_for_function_in_fabfile():
    out = taskhelp('level_one_fab_test', base_module_name='django_helpers.test_fixtures.fabfile')
    assert out == 'Level One Test'

def test_get_docstring_for_function_in_fabfile_submodule():
    out = taskhelp('level_two_fab_test', base_module_name='django_helpers.test_fixtures.fabfile.deploy')
    assert out == 'Level Two Test'
