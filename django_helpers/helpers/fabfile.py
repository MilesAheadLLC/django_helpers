import importlib
import sys
from fabric.api import task


'''
    Provides helpers for projects using fabric

    To use these functions import them in your fabfile from django_helpers.helpers.fabfile import <function name>.
    Importing these functions this way ensures that they will list themselves without a namespace.
'''


@task()
def taskhelp(full_function_name, base_module_name='fabfile'):
    """
     Show help for fab task

     usage: fab taskhelp:<name from fab --list>
    """

    name_split = full_function_name.rsplit('.', 1)

    if len(name_split) == 1:
        module_name = base_module_name
        module = importlib.import_module(module_name)
        function_name = name_split[0]
    else:
        module_name = base_module_name + "." + name_split[0]
        module = importlib.import_module(module_name)
        function_name = name_split[1]

    function = getattr(module, function_name)

    print function.__doc__

    return function.__doc__


