import os

from fabric.api import task

from django_helpers.helpers.fabfile import runtest, mod_test

DJANGO_HELPERS_BASE = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0] # django_helpers/django_helpers
DJANGO_HELPERS_TEST_LOCATION = os.path.join(DJANGO_HELPERS_BASE, 'tests') # django_helpers/django_helpers/tests

@task
def all():
    '''
     Runs all tests for django_helpers

     usage: forefab build.all

    '''
    runtest(DJANGO_HELPERS_TEST_LOCATION)

@task
def django_helper(module):
    '''
     Runs test for specific django_helper module e.g. helpers

     usage: forefab django_helper:<module name>
    '''
    if module is None:
        print "You must pass in a module name"
    else:
        mod_test(DJANGO_HELPERS_TEST_LOCATION, module_name=module)