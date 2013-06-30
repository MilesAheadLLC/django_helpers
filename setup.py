from setuptools import setup, find_packages

setup(
    name = "django_helpers",
    version = "0.2",
    description = "Helpers for Django Apps",
    packages = find_packages('.'),
    package_dir = {"":"."},
    package_data ={},
    install_requires = [
        'Django >= 1.5.1',
        'pytest >= 2.3.4',
        'pytest-django >= 2.3.0',
        'fabric >= 1.6.1',
        'pycrypto >= 2.6',
        'selenium >= 2.32.0',
        'webtest >= 2.0.6',
        'django-webtest >= 1.7.2',
    ]
)