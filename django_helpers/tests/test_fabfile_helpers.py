import os
import types

import pytest

from django_helpers.test_fixtures import fake_fn

from django_helpers.helpers.fabfile import taskhelp, dev_test_only

def test_get_docstring_for_function_in_fabfile():
    """
     Test that taskhelp can produce doc string for a function in a fabfile
    """
    out = taskhelp('level_one_fab_test', base_module_name='django_helpers.test_fixtures.fabfile')
    assert out == 'Level One Test'

def test_get_docstring_for_function_in_fabfile_submodule():
    """
     Test that taskhelp can produce a doc string for a function in fabfile submodule
    """
    out = taskhelp('level_two_fab_test', base_module_name='django_helpers.test_fixtures.fabfile.deploy')
    assert out == 'Level Two Test'

def test_dev_test_only_runs_if_env_is_dev_or_test():
    """
     Test that dev test only will run for dev and test environments
    """
    original_settings = os.environ['DJANGO_SETTINGS_MODULE']

    os.environ['DJANGO_SETTINGS_MODULE'] = 'rapidresearchregistry.settings.dev'
    result = dev_test_only(fake_fn)
    assert isinstance(result, types.FunctionType)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'rapidresearchregistry.settings.test'
    result = dev_test_only(fake_fn)
    assert isinstance(result, types.FunctionType)

    #reset setting module to original
    os.environ['DJANGO_SETTINGS_MODULE'] = original_settings

def test_dev_test_only_does_not_run_it_env_is_not_dev_or_test():
    """
     Test that dev test only will not run for anything other than dev or test
    """
    original_settings = os.environ['DJANGO_SETTINGS_MODULE']

    os.environ['DJANGO_SETTINGS_MODULE'] = 'rapidresearchregistry.settings.wrong'
    result = dev_test_only(fake_fn)
    assert result == "This task only runs on the development and test environments. Believe me you don\'t want to run this in production."

    #reset setting module to original
    os.environ['DJANGO_SETTINGS_MODULE'] = original_settings