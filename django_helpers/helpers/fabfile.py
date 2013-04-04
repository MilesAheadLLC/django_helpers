import os
import importlib
from fabric.api import task, local, lcd

"""
    Provides helpers for projects using fabric

    To use these functions import them in your fabfile from django_helpers.helpers.fabfile import <function name>.
    Importing these functions this way ensures that they will list themselves without a namespace.
"""


@task()
def taskhelp(full_function_name, base_module_name='fabfile'):
    """
     Show help for fab task

     usage: fab taskhelp:<name from fab --list>
    """
    """
     Split the fully qualified function name into list[modulename, function_name] this is necessary because of
     how fabric works. We need to add fabfile to the module name to look up the function later
    """
    name_split = full_function_name.rsplit('.', 1)


    if len(name_split) == 1:
        #if only 1 item it must be the function name get reference to the imported base module and set function name
        module_name = base_module_name
        module = importlib.import_module(module_name)
        function_name = name_split[0]
    else:
        #if more than 1 item the add the first item in the the name split to the base_module_name and then import it
        module_name = base_module_name + "." + name_split[0]
        module = importlib.import_module(module_name)
        function_name = name_split[1]

    # get a reference to the function be looking up the name of the function in the module
    function = getattr(module, function_name)

    print function.__doc__

    return function.__doc__


def dev_test_only(fn):
    """
     Helper function to test if function is being called in the dev or test environment
    """

    settings_mod = os.environ.get('DJANGO_SETTINGS_MODULE')

    print settings_mod

    if 'settings.dev'in settings_mod or 'settings.test' in settings_mod:
        fn()
        return fn
    else:
        msg = 'This task only runs on the development and test environments. Believe me you don\'t want to run this in production.'
        print msg
        return msg


def update_master(path):
    """
     Helper function updates master branch of project it takes in the path of the project
    """
    with lcd(path):
        local('git checkout master')
        local('git pull origin master')